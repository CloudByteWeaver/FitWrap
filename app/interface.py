import defusedxml.ElementTree as ET
import json
import os
from datetime import datetime
from functools import partial
from pathlib import Path

import gpxpy
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QValueAxis, QDateTimeAxis, QAreaSeries
from PySide6.QtCore import Qt, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve, QSize, QDateTime, QMetaObject
from PySide6.QtGui import QIcon, QResizeEvent, QMouseEvent, QPixmap, QPainter, QColor, QPen, QBrush, QFont, \
    QLinearGradient, QGradient
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import QMainWindow, QSizeGrip, QFrame, QWidget, QLineEdit, QTextEdit, QCheckBox, \
    QTableWidgetItem, QLabel, QHeaderView, QMessageBox, QPushButton, QFileDialog, QListWidgetItem, QVBoxLayout
from garmin_fit_sdk import Stream, Decoder

from app.widgets.add_device_window import AddDeviceWindow
from app.ui.ui_interface import Ui_MainWindow
from app.widgets.grip import Grip
from database.db_operations import update_password, verify_current_password, get_user_devices, save_changes_to_database, \
    delete_device, add_activity_from_json, get_user_activities, get_activity_count_for_device, delete_activity
from .widgets.ActivityWidget import ActivityWidget


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        self.add_device_window = AddDeviceWindow(self)
        self.mouseClickPosition = None
        self.last_clicked_btn = None
        self.setupUi(self)
        self.grips = []
        self.init_grips()
        self.is_editing_mode = False
        self.table_modified = False

        self.password_changed_label.hide()

        self.edit_devices_warning_label.hide()
        self.unsaved_changes_label.hide()

        # Set window title and icon
        self.setWindowTitle('FitWrap')
        self.setWindowIcon(QIcon(':/icons/icons/logo.png'))

        # Remove window title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Window size grip to resize window
        QSizeGrip(self.size_grip)

        self.selected_device_cbox.currentIndexChanged.connect(self.load_activities)

        # Minimize window
        self.minimize_window_button.clicked.connect(self.showMinimized)

        # Maximize/Restore window
        self.maximize_window_button.clicked.connect(self.restore_or_maximize_window)

        # Close window
        self.close_window_button.clicked.connect(self.close)

        # Log out
        self.log_out_btn.clicked.connect(self.log_out)

        # Change password
        self.change_password_btn.clicked.connect(self.change_password)
        self.wrong_password_warning_label.hide()
        self.change_password_warning_label.hide()

        # Add click event/mouse event/drap event to the top header to move the window
        self.control_buttons.mouseMoveEvent = self.move_window
        self.left_header_side.mouseMoveEvent = self.move_window
        self.right_header_side.mouseMoveEvent = self.move_window

        # Side menu toggle
        self.show_side_menu_button.clicked.connect(self.slide_side_menu)

        # Change screen page and set side menu buttons background after being clicked
        buttons = [self.account_btn, self.home_btn, self.add_activity_btn, self.manage_devices_btn, self.map_btn,
                   self.activities_btn, self.compare_btn, self.faq_btn, self.settings_btn]
        for index, button in enumerate(buttons):
            button.clicked.connect(partial(self.attempt_page_change, index, button))

        # Add activity page
        self.select_activity_file_btn.clicked.connect(self.select_activity_file)
        self.no_device_selected_label.hide()
        self.error_while_loading_data_label.hide()
        self.activity_added_label.hide()

        # Manage devices page
        self.add_device_btn.clicked.connect(self.show_add_device_window)
        self.load_devices_data()
        self.edit_device_table_btn.clicked.connect(self.edit_devices)
        self.save_edited_table_btn.clicked.connect(self.save_edited_table)
        self.delete_device_btn.clicked.connect(self.delete_selected_device)

        self.search_device_field.textChanged.connect(self.filter_table)

        # Activities page
        self.currently_viewed_activity_id = None
        self.activities_list.itemClicked.connect(lambda item: self.show_activity_details(item))
        self.back_to_activities_list_btn.clicked.connect(self.back_to_activities_list)
        self.delete_activity_btn.clicked.connect(self.delete_activity)

        # Compare page
        self.compare_chart = QChart()
        self.compare_chart_view = QChartView(self.compare_chart)
        self.heart_rate_comparison_chart_setup()
        self.heart_rate_radio_btn.toggled.connect(lambda: self.compare_pages.setCurrentIndex(0))
        self.route_radio_btn.toggled.connect(lambda: self.compare_pages.setCurrentIndex(1))
        self.activity_1_cbox.currentIndexChanged.connect(self.update_comparison_page)
        self.activity_2_cbox.currentIndexChanged.connect(self.update_comparison_page)

        # Hide unused items
        self.map_btn.hide()
        self.faq_btn.hide()
        self.settings_btn.hide()

    ############################################################################################################
    # Account page functions
    ############################################################################################################
    def log_out(self):
        """
        Log the user out by clearing the saved credentials.
        """
        # Delete the credentials file
        credentials_path = Path("credentials.json")
        if credentials_path.exists():
            credentials_path.unlink()

        # Delete the secret key file to invalidate the key
        key_path = Path("secret.key")
        if key_path.exists():
            key_path.unlink()

        # Hide main window
        self.hide()
        self.reset_widgets()
        self.login_window.show()

    def change_password(self):
        """
        Changes the password for the user.
        """
        # Get the current and new passwords
        current_password = self.current_password_field.text()
        password_1 = self.new_password_1_field.text()
        password_2 = self.new_password_2_field.text()

        # Verify the current password
        if not verify_current_password(self.login_window.get_login(), current_password):
            # Show warning if current password is incorrect
            self.wrong_password_warning_label.show()
        else:
            # Hide warning label if it's currently visible
            if self.wrong_password_warning_label.isVisible():
                self.wrong_password_warning_label.hide()

        # Check password length and match
        if len(password_1) < 8:
            self._display_warning_message(self.change_password_warning_label, 'At least 8 characters.')
        elif password_1 != password_2:
            self._display_warning_message(self.change_password_warning_label, 'The passwords entered do not match.')
        else:
            # Hide warning label if it's currently visible
            if self.change_password_warning_label.isVisible():
                self.change_password_warning_label.hide()

            # Update password and show success message
            if update_password(self.login_window.get_login(), password_1):
                self.password_changed_label.show()

    @staticmethod
    def _display_warning_message(label: QLabel, message: str) -> None:
        """
        Display a warning message on a QLabel.

        :param label: The QLabel on which to display the warning message.
        :type label: QLabel
        :param message: The warning message to display.
        :type message: str

        :return: None
        """
        # Set the text of the label to the warning message
        label.setText(message)
        label.show()

    ############################################################################################################
    # Add activity page functions
    ############################################################################################################

    def select_activity_file(self) -> None:
        """
        Opens a file dialog to browse and select an activity file.

        :return: None
        """
        # Check if a device is selected
        if self.selected_device_cbox.currentIndex() == -1:
            # Show a message if no device is selected
            self.no_device_selected_label.show()
            return
        else:
            # Hide the message if a device is selected
            if self.no_device_selected_label.isVisible():
                self.no_device_selected_label.hide()

        if self.activity_added_label.isVisible():
            self.activity_added_label.hide()

        # Set the default directory to the user's Downloads folder
        path = os.path.expanduser("~/Downloads")

        # Open the file dialog to select an activity file
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', path,
                                                   'Activity files (*.gpx *.fit *.tcx)')

        if file_name and os.path.getsize(file_name) > 0:
            # Get the file extension
            file_extension = os.path.splitext(file_name)[1]

            # Load data based on the file extension
            if file_extension == ".fit":
                json_data, file_extension = self.load_fit_data(file_name)
            elif file_extension == ".gpx":
                json_data, file_extension = self.load_gpx_data(file_name)
            elif file_extension == ".tcx":
                json_data, file_extension = self.load_tcx_data(file_name)

            # Add the activity data and show/hide labels accordingly
            if add_activity_from_json(json_data, file_extension, self.selected_device_cbox.currentData()):
                if self.error_while_loading_data_label.isVisible():
                    self.error_while_loading_data_label.hide()
                self.activity_added_label.show()
            else:
                if self.activity_added_label.isVisible():
                    self.activity_added_label.hide()
                self.error_while_loading_data_label.show()

        self.load_devices_data()
        self.load_activities()

    def load_fit_data(self, file_name: str) -> (str, str):
        """
        Load and decode data from a file and return it as JSON.

        :param file_name: The name of the file to load.
        :type file_name: str

        :return: The decoded data in JSON format and the file extension.
        :rtype: (str, str)
        """
        # Load data from file
        stream = Stream.from_file(file_name)

        # Decode data
        decoder = Decoder(stream)
        messages, errors = decoder.read()

        # Check for errors and print them if any
        if errors:
            print(errors)
            return
        else:
            # Convert messages to JSON
            json_data = json.dumps(messages, default=self.datetime_converter)
            print(json_data)
            return json_data, '.fit'

    def load_gpx_data(self, file_name) -> (str, str):
        """
        Load GPX data from a file and convert it to JSON format.

        :param file_name: The name of the GPX file to load.
        :type file_name: str

        :return: The JSON representation of the GPX data and the file extension.
        :rtype: (str, str)
        """
        try:
            with open(file_name, 'r') as gpx_file:
                try:
                    gpx = gpxpy.parse(gpx_file)  # Parse the GPX file
                    json_data = self.gpx_to_json(gpx)  # Convert the parsed GPX data to JSON
                    return json_data, '.gpx'  # Return the JSON data and the file extension
                except gpxpy.gpx.GPXXMLSyntaxException as e:
                    print(f"Error parsing GPX data: {e}")
                    return None, None  # Return None for both JSON data and file extension
        except FileNotFoundError as e:
            print(f"Error loading GPX file: {e}")
            return None, None  # Return None for both JSON data and file extension

    def load_tcx_data(self, file_name) -> tuple[str, str]:
        """
        Load data from a TCX file and return it as JSON format.

        :param file_name: The name of the TCX file to load.
        :type file_name: str

        :return: A tuple containing the converted JSON data and a string with the file extension.
        :rtype: (dict, str)
        """
        # Convert TCX file to JSON format
        json_data = self.tcx_to_json(file_name)
        return json_data, '.tcx'

    @staticmethod
    def tcx_to_dict(tcx_file):
        """
        Parses a TCX file and returns the data as a dictionary.

        :param tcx_file: The path to the TCX file.
        :type tcx_file: str

        :return: A list of dictionaries containing the parsed data.
        :rtype: list[dict[str, list | None]]
        """
        # Define XML namespaces
        ns_tcd = '{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}'
        ns_act_ext = '{http://www.garmin.com/xmlschemas/ActivityExtension/v2}'

        tree = ET.parse(tcx_file)
        root = tree.getroot()

        # Przetwarzanie danych
        activities_data = []

        for activity in root.findall(f'.//{ns_tcd}Activity'):
            activity_data = {
                'Sport': activity.get('Sport'),
                'Id': activity.find(f'{ns_tcd}Id').text,
                'Notes': activity.find(f'{ns_tcd}Notes').text if activity.find(f'{ns_tcd}Notes') is not None else None,
                'Lap': []
            }

            for lap in activity.findall(f'{ns_tcd}Lap'):
                lap_data = {
                    'StartTime': lap.get('StartTime'),
                    'TotalTimeSeconds': lap.find(f'{ns_tcd}TotalTimeSeconds').text,
                    'DistanceMeters': lap.find(f'{ns_tcd}DistanceMeters').text,
                    'Calories': lap.find(f'{ns_tcd}Calories').text,
                    'AverageHeartRateBpm': lap.find(f'.//{ns_tcd}AverageHeartRateBpm/{ns_tcd}Value').text if lap.find(
                        f'.//{ns_tcd}AverageHeartRateBpm/{ns_tcd}Value') is not None else None,
                    'MaximumHeartRateBpm': lap.find(f'.//{ns_tcd}MaximumHeartRateBpm/{ns_tcd}Value').text if lap.find(
                        f'.//{ns_tcd}MaximumHeartRateBpm/{ns_tcd}Value') is not None else None,
                    'Track': []
                }

                for track in lap.findall(f'{ns_tcd}Track'):
                    for trackpoint in track.findall(f'{ns_tcd}Trackpoint'):
                        tp_data = {
                            'Time': trackpoint.find(f'{ns_tcd}Time').text if trackpoint.find(
                                f'{ns_tcd}Time') is not None else None,
                            'DistanceMeters': trackpoint.find(f'{ns_tcd}DistanceMeters').text if trackpoint.find(
                                f'{ns_tcd}DistanceMeters') is not None else None,
                            'HeartRateBpm': trackpoint.find(
                                f'.//{ns_tcd}HeartRateBpm/{ns_tcd}Value').text if trackpoint.find(
                                f'.//{ns_tcd}HeartRateBpm/{ns_tcd}Value') is not None else None
                        }
                        # Dodanie danych pozycji, jeśli istnieją
                        position = trackpoint.find(f'.//{ns_tcd}Position')
                        if position is not None:
                            tp_data['Position'] = {
                                'LatitudeDegrees': position.find(f'{ns_tcd}LatitudeDegrees').text,
                                'LongitudeDegrees': position.find(f'{ns_tcd}LongitudeDegrees').text
                            }
                        # Wyszukanie i dodanie prędkości z Extensions
                        extensions = trackpoint.find(f'.//{ns_act_ext}TPX')
                        if extensions is not None:
                            speed = extensions.find(f'{ns_act_ext}Speed')
                            if speed is not None:
                                tp_data['Speed'] = speed.text

                        lap_data['Track'].append(tp_data)

                activity_data['Lap'].append(lap_data)

            activities_data.append(activity_data)

        return activities_data

    def tcx_to_json(self, tcx_file):
        """
        Convert TCX file to JSON format.

        :param tcx_file: The path to the TCX file.
        :type tcx_file: str

        :return: The JSON representation of the TCX file.
        :rtype: str
        """
        tcx_dict = self.tcx_to_dict(tcx_file)
        return json.dumps(tcx_dict)

    def gpx_to_json(self, gpx: gpxpy.gpx.GPX) -> str:
        """
        Converts GPX data to JSON format using gpxpy library.

        :param gpx: The GPX object to be converted to JSON.
        :type gpx: gpxpy.gpx.GPX

        :return: The JSON representation of the GPX data.
        :rtype: str
        """

        # Initialize the JSON data structure
        json_data = {
            'tracks': [],
            'waypoints': [],
            'routes': []
        }

        # Convert tracks
        for track in gpx.tracks:
            json_track = {
                'name': track.name,
                'segments': []
            }

            for segment in track.segments:
                segment_data = []

                for point in segment.points:
                    point_data = {
                        'latitude': point.latitude,
                        'longitude': point.longitude,
                        'elevation': point.elevation,
                        'time': point.time.isoformat() if point.time else None,
                        'extensions': {}
                    }

                    if point.extensions:
                        print("Extensions found for point:", point)
                    else:
                        print("No extensions found for point:", point)

                    # Convert extensions
                    for extension in point.extensions:
                        extension_data = {}

                        for field in extension:
                            # Remove namespace URI from tag name
                            tag_name = field.tag[field.tag.find('}') + 1:]  # Removes everything up to '}'

                            # Try to convert value to float or int if possible
                            value = self.change_to_number(field.text)

                            extension_data[tag_name] = value

                        point_data['extensions'] = extension_data

                    segment_data.append(point_data)

                json_track['segments'].append({
                    'points': segment_data
                })

            json_data['tracks'].append(json_track)

        # Convert waypoints
        for waypoint in gpx.waypoints:
            json_waypoint = {
                'lat': waypoint.latitude,
                'lon': waypoint.longitude,
                'name': waypoint.name,
                'ele': waypoint.elevation,
                'time': waypoint.time.isoformat() if waypoint.time else None
            }
            json_data['waypoints'].append(json_waypoint)

        # Convert routes
        for route in gpx.routes:
            json_route = {
                'name': route.name,
                'points': [{'lat': point.latitude, 'lon': point.longitude, 'ele': point.elevation,
                            'time': point.time.isoformat() if point.time else None} for point in route.points]
            }
            json_data['routes'].append(json_route)

        return json.dumps(json_data)

    @staticmethod
    def change_to_number(value):
        """
        Tries to convert the input value to a number.

        :param value: The input value to be converted.
        :type value: str

        :return: The converted value or the original value if conversion fails.
        :rtype: int, float, or str
        """
        try:
            # First, check if the value is an integer
            if value.isdigit():
                value = int(value)
            else:
                # If it's not an integer, try to convert to float
                value = float(value)
        except ValueError:
            # If conversion fails, leave it as a string
            pass

        return value

    @staticmethod
    def datetime_converter(o):
        """
        Convert datetime object to its string representation.

        :param o: The input object to be converted.

        :return: The string representation of the input datetime object.
        :rtype: str
        """
        if isinstance(o, datetime):
            return o.__str__()

    ############################################################################################################
    # Manage devices page functions
    ############################################################################################################

    def load_devices_data(self) -> None:
        """
        Load data for devices into the table.

        :return: None
        """

        # Get the devices data
        devices = get_user_devices(self.login_window.get_users_id())
        ID_COLUMN_INDEX = 6

        # Set the number of rows in the table and the icon size
        self.device_table.setRowCount(len(devices))
        self.device_table.setIconSize(QSize(64, 64))

        self.device_table.insertColumn(ID_COLUMN_INDEX)
        self.device_table.setColumnHidden(ID_COLUMN_INDEX, True)

        # Iterate through the devices to populate the table
        for row_num, device in enumerate(devices):
            # Load the device icon and scale it
            icon_pixmap = QPixmap()
            icon_pixmap.loadFromData(device.Icon)
            icon_pixmap = icon_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Create a label for the icon and set its alignment
            icon_label = QLabel()
            icon_label.setPixmap(icon_pixmap)
            icon_label.setAlignment(Qt.AlignCenter)

            # Set the icon label in the table
            self.device_table.setCellWidget(row_num, 0, icon_label)

            # Populate the table cells with device information
            for col_num, field in enumerate([device.Brand, device.Model, device.Type, device.LastUpdate,
                                             "activity_count", device.DeviceID]):
                if field == device.LastUpdate:
                    field = device.LastUpdate.strftime('%Y-%m-%d %H:%M:%S')  # format the datetime as a string
                elif field == "activity_count":
                    field = get_activity_count_for_device(device.DeviceID)
                elif field == device.DeviceID:
                    field = str(device.DeviceID)

                # Create a table item
                item = QTableWidgetItem(field)
                self.device_table.setItem(row_num, col_num + 1, item)

        # Set the stretch policy for the remaining columns
        self.device_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.align_cells()

        self.disable_table_editing()
        self.load_devices_into_combobox()

    def toggle_editing(self) -> None:
        """
        Toggle editing for the 'Brand', 'Model', and 'Type' columns in the table.

        :return: None
        """
        # Sprawdzamy, czy pierwsza komórka w pierwszym edytowalnym wierszu jest edytowalna
        if self.device_table.item(0, 1) is not None:
            if self.device_table.item(0, 1).flags() & Qt.ItemIsEditable:
                self.disable_table_editing()
            else:
                self.enable_editing_for_selected_columns()

    def disable_table_editing(self) -> None:
        """
        Disables editing for all fields in the table.

        :return: None
        """
        # Iterate through each row
        for row_num in range(self.device_table.rowCount()):
            # Iterate through each column
            for col_num in range(1, self.device_table.columnCount()):
                # Get the item at the current row and column
                item = self.device_table.item(row_num, col_num)
                # If the item exists, remove the editable flag
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def enable_editing_for_selected_columns(self) -> None:
        """
        Enable editing for the 'Brand', 'Model', and 'Type' columns in the table.

        :return: None
        """
        editable_columns = [1, 2, 3]  # Numery kolumn, które mają być edytowalne (Brand, Model, Type)

        for row_num in range(self.device_table.rowCount()):
            for col_num in editable_columns:
                item = self.device_table.item(row_num, col_num)
                if item is not None:
                    # Włączamy edytowalność poprzez dodanie flagi Qt.ItemIsEditable
                    item.setFlags(item.flags() | Qt.ItemIsEditable)

    def align_cells(self) -> None:
        """
        Set the height of each row to 64 and align the text in each cell to the center.

        :return: None
        """
        for row_num in range(self.device_table.rowCount()):  # Loop through each row
            self.device_table.setRowHeight(row_num, 64)  # Set the height of the current row to 64
            for col_num in range(self.device_table.columnCount()):  # Loop through each column
                item = self.device_table.item(row_num, col_num)  # Get the item in the current cell
                if item is not None:  # Check if the cell is not empty
                    item.setTextAlignment(Qt.AlignCenter)  # Align the text in the cell to the center

    def show_add_device_window(self) -> None:
        """
        Show the add device window.

        :return: None
        """
        self.add_device_window.show()

    def edit_devices(self) -> None:
        """
        Toggles editing mode for devices and updates UI accordingly.

        :return: None
        """
        # Toggle editing mode
        self.is_editing_mode = not self.is_editing_mode

        if self.is_editing_mode:
            # Show warning label
            self.edit_devices_warning_label.show()
            # Enable editing for selected columns
            self.enable_editing_for_selected_columns()
            # Connect signal for table content change
            self.device_table.itemChanged.connect(self.changed_table_content)
            # Show unsaved changes label if table has been modified
            if self.table_modified:
                self.unsaved_changes_label.show()
        else:
            # Hide warning label
            self.edit_devices_warning_label.hide()
            # Disable table editing
            self.disable_table_editing()
            # Disconnect signal for table content change
            self.device_table.itemChanged.disconnect(self.changed_table_content)

    def save_edited_table(self) -> None:
        """
        Save the edited table if it has been modified.

        :return: None
        """
        if self.table_modified:
            save_changes_to_database(self.device_table)
            self.table_modified = False
            self.unsaved_changes_label.hide()
            self.load_devices_data()

    def changed_table_content(self) -> None:
        """
        Update table content and indicate unsaved changes if in editing mode.

        :return: None
        """
        # Check if in editing mode
        if self.is_editing_mode:
            # Set table modification flag
            self.table_modified = True
            # Show unsaved changes label
            self.unsaved_changes_label.show()

    def confirm_unsaved_changes(self) -> bool:
        """
        Display a confirmation dialog if there are unsaved changes in the devices table.
        Return True if the user confirms to proceed without saving, False otherwise.
        """
        if self.table_modified:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Unsaved Changes")
            msg_box.setText("You have unsaved changes in the Devices table.")
            msg_box.setInformativeText("Do you want to save your changes?")
            msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msg_box.setDefaultButton(QMessageBox.Save)
            response = msg_box.exec()

            if response == QMessageBox.Save:
                self.save_edited_table()
                return True
            elif response == QMessageBox.Discard:
                self.load_devices_data()
                self.table_modified = False
                self.unsaved_changes_label.hide()
                return True
            elif response == QMessageBox.Cancel:
                return False
        return True

    def attempt_page_change(self, page_index: int, button: QPushButton) -> None:
        """
        Attempt to change the page. If there are unsaved changes, confirm with the user before changing the page.
        """
        if self.confirm_unsaved_changes():
            self.page.setCurrentIndex(page_index)
            self.side_button_released(button)  # Pass the button to handle style changes

    def delete_selected_device(self) -> None:
        """
        Delete the selected device or devices from the database.

        :return: None
        """
        selected_rows = self.device_table.selectedItems()
        if not selected_rows:
            print("Nie zaznaczono żadnego wiersza")
            return

        delete_device(selected_rows, self.device_table)
        self.load_devices_data()

    def filter_table(self, text: str) -> None:
        """
        Filters the table based on the given text.

        :param text: The text to filter the table with.
        :type text: str

        :return: None
        """
        # Iterate through each row in the table
        for row in range(self.device_table.rowCount()):
            item_visible = False  # Assume the row is not visible
            # Iterate through each column in the row
            for column in range(self.device_table.columnCount()):
                item = self.device_table.item(row, column)
                # Check if the item exists and if the text is found in the item
                if item and text.lower() in item.text().lower():
                    item_visible = True  # If the text matches, mark the row as visible
                    break  # Exit the loop, as one matching item is enough
            # Set the visibility of the row based on the item visibility
            self.device_table.setRowHidden(row, not item_visible)

    ############################################################################################################
    # Activities page functions
    ############################################################################################################

    def load_activities(self) -> None:
        """
        Clear the activities list and populate it with activities for the selected device.
        :return: None
        """
        # Clear the activities list
        self.activities_list.clear()

        # Get activities for the selected device
        activities = get_user_activities(self.selected_device_cbox.currentData())

        # Iterate through activities and add them to the list
        for activity in activities:
            # Create a list item for the activity
            list_item = QListWidgetItem(self.activities_list)

            # Create a widget for the activity
            activity_widget = ActivityWidget(activity)

            # Set the size hint for the list item
            list_item.setSizeHint(activity_widget.sizeHint() + QSize(0, 20))

            # Add the list item to the activities list
            self.activities_list.addItem(list_item)

            # Set the widget for the list item
            self.activities_list.setItemWidget(list_item, activity_widget)

            # Load the activity for comparison
            if activities[0] == activity:
                self.load_activity_to_compare(activity_widget, reload=True)
            else:
                self.load_activity_to_compare(activity_widget)

    def show_activity_details(self, item: QListWidgetItem) -> None:
        """
        Show details of the selected activity.

        :param item: The selected item in the activities list.
        :type item: QListWidgetItem

        :return: None
        """

        # Scroll to the top of the page
        self.scroll_to_top()

        # Get the activity widget for the selected item
        activity_widget = self.activities_list.itemWidget(item)

        # Set the currently viewed activity ID
        self.currently_viewed_activity_id = activity_widget.activity.WorkoutID

        # Set summary labels
        self.activity_time_label.setText(activity_widget.duration_time)
        self.avg_heart_rate_label.setText(activity_widget.avg_heart_rate)
        self.distance_label.setText(activity_widget.distance_km)
        self.avg_pace_label.setText(activity_widget.avg_pace)
        self.avg_speed_label.setText(activity_widget.average_speed)
        self.max_speed_label.setText(activity_widget.max_speed)

        # Set up heart rate chart
        self.chart_avg_hr_label.setText(activity_widget.avg_heart_rate)
        self.chart_max_hr_label.setText(activity_widget.max_heart_rate)

        # Create a heart rate chart
        self.create_heart_rate_chart(activity_widget.points_for_heart_rate_chart)

        # Place route on map
        self.place_route_on_map(activity_widget.route, self.details_map)

        # Hide the activities header and switch to the activity details page
        self.activities_header.hide()
        self.activities_sub_pages.setCurrentIndex(1)

    def scroll_to_top(self) -> None:
        """
        Scrolls the scroll area to the top.
        :return: None
        """
        # Set the vertical scroll bar to its minimum value
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().minimum())

    def create_heart_rate_chart(self, points) -> None:
        """
        Create a heart rate chart based on the given points.

        :param points: List of dictionaries containing time and heart rate data.
        :type points: list

        :return: None
        """
        if points is None or len(points) == 0:
            return

        # Create the line series
        series = QLineSeries()
        for point in points:
            time = QDateTime.fromString(point['time'], "yyyy-MM-ddTHH:mm:ss")
            series.append(time.toMSecsSinceEpoch(), point['heart_rate'])

        # Customize the line series
        series.setColor(QColor("#DD353D"))  # Set the color of the line to red
        series.setPen(QPen(QBrush(QColor("#DD353D")), 2))  # Set the line thickness

        # Create the area series and assign the line series to it
        area_series = QAreaSeries(series)
        area_series.setColor(QColor("#dd353d"))

        # Create a gradient for the area series fill
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setColorAt(0.0, QColor("#8C2F27"))  # Red with some transparency
        gradient.setColorAt(1.0, QColor("#1C1C1C00"))  # Transparent red at the bottom
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        area_series.setBrush(gradient)

        # Create the chart as before and add the area series
        chart = QChart()
        chart.addSeries(area_series)  # Add the area series to the chart
        chart.addSeries(series)  # Add the line series to the chart as well
        chart.createDefaultAxes()
        chart.setTitleBrush(QBrush(QColor("#EEE")))  # Set the title color
        chart.setTitleFont(QFont("Sans", 10))  # Customize title font

        # Customize the chart background
        chart.setBackgroundBrush(QBrush(QColor("#1C1C1C")))

        # Customize the axes as before
        axis_x = QDateTimeAxis()
        axis_x.setFormat("H:mm:ss")
        axis_x.setTitleText('Time')
        axis_y = QValueAxis()
        axis_y.setTitleText('Heart rate (bpm)')

        axis_x.setLabelsColor(QColor("#EEE"))  # Set the color of X axis labels
        axis_y.setLabelsColor(QColor("#EEE"))  # Set the color of Y axis labels

        axis_x.setLinePenColor(QColor("#EEE"))  # Set the color of X axis line
        axis_y.setLinePenColor(QColor("#EEE"))  # Set the color of Y axis line

        axis_x.setGridLineVisible(False)  # Hide the X axis grid
        axis_y.setGridLineVisible(False)  # Hide the Y axis grid

        chart.setAxisX(axis_x, series)
        chart.setAxisY(axis_y, series)

        # Hide the legend
        chart.legend().setVisible(False)

        # Create the chart view as before
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.clear_layout(self.heart_rate_chart.layout())

        # Set up the layout as before
        if self.heart_rate_chart.layout() is None:
            layout = QVBoxLayout()
            layout.addWidget(chart_view)
            self.heart_rate_chart.setLayout(layout)
        else:
            self.heart_rate_chart.layout().addWidget(chart_view)

    def clear_layout(self, layout) -> None:
        """
        Clears the given layout by removing all its child widgets and layouts.

        :param layout: The layout to be cleared.
        :type layout: QLayout

        :return: None
        """
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                elif item.layout() is not None:
                    self.clear_layout(item.layout())

    def place_route_on_map(self, route: list, map: QQuickWidget, compare_to_route: list = None) -> None:
        """
        Places the given route on the map.

        :param route: The route to be placed on the map.
        :type route: list
        :param map: The QQuickWidget representing the map.
        :type map: QQuickWidget
        :param compare_to_route: Optional parameter to compare routes.
        :type compare_to_route: list

        :return: None
        """

        # Connect statusChanged signal to on_status_changed method to see error messages
        map.statusChanged.connect(self.on_status_changed)

        # Set the routePoints property of the map's root object
        map.rootObject().setProperty("route1Points", route)

        # Set the compareRoutePoints property if compare_to_route is provided
        if compare_to_route is not None:
            map.rootObject().setProperty("route2Points", compare_to_route)

        # Update the map view
        self.update_map_view(map)

    @staticmethod
    def update_map_view(map) -> None:
        """
        Update the map view if the root object of details_map is not None.

        :param map: The map object
        :type map: QtCore.QObject

        :return: None
        """
        if map.rootObject() is not None:
            # Invoke the 'updateMapView' method of the root object of details_map using QMetaObject.
            QMetaObject.invokeMethod(map.rootObject(), "updateMapView")

    def on_status_changed(self, status):
        if status == QQuickWidget.Error:
            errors = self.details_map.errors()
            for error in errors:
                print(error.toString())

    def back_to_activities_list(self) -> None:
        """
        A function to navigate back to the activities list, hiding the header and setting the current
        index of sub-pages to 0.

        :return: None
        """
        self.activities_header.show()
        self.activities_sub_pages.setCurrentIndex(0)

    def delete_activity(self) -> None:
        """
        Function to prompt the user to confirm the deletion of an activity.
        If confirmed, the activity will be deleted and related data will be reloaded.

        :return: None
        """
        # Prompt the user to confirm the deletion
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Delete activity")
        msg_box.setText("You are about to delete an activity.")
        msg_box.setWindowIcon(QIcon(':/icons/icons/logo.png'))
        msg_box.setInformativeText("Do you want to continue?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        response = msg_box.exec()

        # If user confirms, delete the activity and reload related data
        if response == QMessageBox.Yes:
            delete_activity(self.currently_viewed_activity_id)
            self.load_activities()
            self.load_devices_data()
            self.back_to_activities_list()

    ############################################################################################################
    # Compare page functions
    ############################################################################################################

    def heart_rate_comparison_chart_setup(self) -> None:
        """
        Set up the heart rate comparison chart with initial settings.
        :return: None
        """
        # Set chart title
        self.compare_chart.setTitle("Heart Rate Comparison")

        # Set chart title appearance
        self.compare_chart.setTitleBrush(QBrush(QColor("#EEE")))
        self.compare_chart.setTitleFont(QFont("Sans", 10))

        # Set chart background
        self.compare_chart.setBackgroundBrush(QBrush(QColor("#1C1C1C")))

        # Create default axes
        self.compare_chart.createDefaultAxes()

        # Customize X axis
        axis_x = QDateTimeAxis()
        axis_x.setFormat("H:mm:ss")
        axis_x.setTitleText('Time')
        self.compare_chart.setAxisX(axis_x)

        # Customize Y axis
        axis_y = QValueAxis()
        axis_y.setTitleText('Heart rate (bpm)')
        self.compare_chart.setAxisY(axis_y)

        # Set chart view rendering
        self.compare_chart_view.setRenderHint(QPainter.Antialiasing)

        # Add chart view to layout
        layout = QVBoxLayout()
        layout.addWidget(self.compare_chart_view)
        self.compare_heart_rate_page.setLayout(layout)

    def load_activity_to_compare(self, activity_widget: ActivityWidget, reload=False) -> None:
        """
        Load activity data to compare in activity combo boxes.

        :param activity_widget: The activity widget containing the activity data
        :type activity_widget: ActivityWidget
        :param reload: A boolean indicating whether to reload the combo boxes
        :type reload: bool

        :return: None
        """
        # Clear the combo boxes if reload is True
        if reload:
            self.activity_1_cbox.clear()
            self.activity_2_cbox.clear()

        # Add the activity to the combo boxes
        self.activity_1_cbox.addItem(activity_widget.activity_name_label.text(),
                                     activity_widget)
        self.activity_2_cbox.addItem(activity_widget.activity_name_label.text(),
                                     activity_widget)

    def update_comparison_page(self) -> None:
        """
        Updates the comparison page by updating the chart and the route.
        """
        self.update_chart()
        self.update_route()

    def update_chart(self) -> None:
        """
        Update the chart with new data for two activities.
        :return: None
        """
        self.compare_chart.removeAllSeries()  # Clear previous data
        points_activity1 = None
        points_activity2 = None

        if self.activity_1_cbox.currentData() is not None:
            points_activity1 = self.activity_1_cbox.currentData().points_for_heart_rate_chart

        if self.activity_2_cbox.currentData() is not None:
            points_activity2 = self.activity_2_cbox.currentData().points_for_heart_rate_chart

        if points_activity1 is None or len(points_activity1) == 0 or points_activity2 is None or len(
                points_activity2) == 0:
            return

        def create_series(points: list, color: str) -> QLineSeries:
            """
            Create and customize series for the chart.

            :param points: List of data points for the series.
            :type points: list
            :param color: Color code for the series.
            :type color: str

            :return: The created series.
            :rtype: QLineSeries
            """
            series = QLineSeries()
            for index, point in enumerate(points):
                # Use index as X value
                series.append(index, point['heart_rate'])
            series.setColor(QColor(color))
            series.setPen(QPen(QBrush(QColor(color)), 2))
            self.compare_chart.addSeries(series)  # Add series to the chart
            return series

        # Create and add new series for both activities
        series_activity1 = create_series(points_activity1, "#DD353D")
        series_activity2 = create_series(points_activity2, "#3572DD")

        # Recreate default axes to adjust for new data ranges
        self.compare_chart.createDefaultAxes()

        # Customizing the X axis to use numeric labels if necessary
        axis_x = QValueAxis()
        axis_x.setTitleText('Data Points')
        axis_x.setLabelFormat("%i")
        self.compare_chart.setAxisX(axis_x, series_activity1)
        self.compare_chart.setAxisX(axis_x, series_activity2)

        # Update the legend
        self.compare_chart.legend().setVisible(True)
        series_activity1.setName("Activity 1")
        series_activity2.setName("Activity 2")

    def update_route(self) -> None:
        """
        Update the route on the map based on the selected activities.
        :return: None
        """
        if self.activity_1_cbox.currentData() is not None and self.activity_2_cbox.currentData() is not None:
            """
            If both activity 1 and activity 2 have route data, 
            place the route on the map by calling place_route_on_map method.
            """
            self.place_route_on_map(self.activity_1_cbox.currentData().route, self.compare_route_map,
                                    self.activity_2_cbox.currentData().route)

    ############################################################################################################
    # Main window functions
    ############################################################################################################
    def load_devices_into_combobox(self) -> None:
        """
        Load devices from the database and add them to the QComboBox with the icon
        set as the item icon and the brand and model concatenated as the item text.

        :return: None
        """
        current_selected_device_index = -1
        if self.selected_device_cbox.currentIndex() != -1:
            current_selected_device_index = self.selected_device_cbox.currentIndex()

        # Clear the current items in the QComboBox
        self.selected_device_cbox.clear()

        # Fetch devices from the database
        devices = get_user_devices(self.login_window.get_users_id())
        if len(devices) == 0:
            current_selected_device_index = -1

        # Iterate through the devices and add them to the QComboBox
        for device in devices:
            # Load the device icon
            icon_pixmap = QPixmap()
            icon_pixmap.loadFromData(device.Icon)
            icon_pixmap = icon_pixmap.scaled(37, 37, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon = QIcon(icon_pixmap)

            # Concatenate brand and model
            brand_model = f"{device.Brand} {device.Model}"

            # Add the item to the QComboBox
            self.selected_device_cbox.addItem(icon, brand_model, device.DeviceID)

        self.selected_device_cbox.setCurrentIndex(current_selected_device_index)

    def reset_widgets(self) -> None:
        """
        Resets all the QLineEdit, QTextEdit, and QCheckBox widgets found as children.

        :return: None
        """
        for widget in self.findChildren(QWidget):
            if isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QTextEdit):
                widget.clear()
            elif isinstance(widget, QCheckBox):
                widget.setChecked(False)

    def side_button_released(self, button: QPushButton = None) -> None:
        """
        Handles the styling and state change of sidebar buttons upon release.

        :param button: The button that triggered the release event.

        :return: None
        """
        if button is not None:
            sender = button
        else:
            sender = self.sender()

        if sender is not None:
            if self.last_clicked_btn is None:
                # Set last clicked button and add background color for pressed button
                self.last_clicked_btn = sender
                css_string = sender.styleSheet() + 'background-color: #393E46;'
                sender.setStyleSheet(css_string)
            elif self.last_clicked_btn != sender:
                # Remove background color for previous button and set new last clicked button
                css_string = self.last_clicked_btn.styleSheet()[:-26]
                self.last_clicked_btn.setStyleSheet(css_string)
                self.last_clicked_btn = sender

                # Add background color for clicked button
                css_string = sender.styleSheet() + 'background-color: #393E46;'
                sender.setStyleSheet(css_string)
        else:
            return

    def restore_or_maximize_window(self) -> None:
        """
        Toggle the window between its maximized and normal states.
        """
        # If window is maximized
        if self.isMaximized():
            self.showNormal()
            self.show_grips()
            # Change icon
            self.maximize_window_button.setIcon(QIcon(':/icons/icons/arrow-increase-svgrepo-com.svg'))
        else:
            self.showMaximized()
            self.hide_grips()
            # Change icon
            self.maximize_window_button.setIcon(QIcon(':/icons/icons/arrow-decrease-svgrepo-com.svg'))

    def move_window(self, event: QMouseEvent) -> None:
        """
        Function to move window on mouse drag event on the title bar

        :param event: The mouse event that triggers the window movement. This event contains the current position of the
        mouse cursor.
        """
        # Detect if the window is normal size
        if not self.isMaximized():
            # Move window only when window is normal size
            if event.buttons() == Qt.LeftButton:
                # Move window
                self.move(self.pos() + event.globalPos() - self.mouseClickPosition)
                self.mouseClickPosition = event.globalPos()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handle the mouse press event.

        This method is called when a mouse button is pressed within the window.
        It retrieves the current position of the mouse and stores it in `self.mouseClickPosition`.
        """
        # Check if the window is not maximized
        if not self.isMaximized():
            # Get current position of the mouse
            self.mouseClickPosition = event.globalPos()

    def slide_side_menu(self) -> None:
        """
        Slide the side menu in or out.
        """
        # Get current side menu width
        width = self.side_menu_container.width()

        # If hidden or partially shown
        if width == 60:
            # Expand side menu
            new_width = 200
            new_logo_width = 182
            is_side_menu_expanded = True
        else:
            # Hide side menu
            new_width = 60
            new_logo_width = 136
            is_side_menu_expanded = False

        # Update UI
        self.update_side_menu_icon(is_side_menu_expanded)

        # Animate the transition
        self.animate_side_menu(new_width, new_logo_width)

    def animate_side_menu(self, new_width: int, new_logo_width: int) -> None:
        """
        Animate the side menu transition.

        :param new_width: The new width of the side menu.
        :param new_logo_width: The new width of the logo.
        """
        self.animation = self.create_animation(self.side_menu_container, b"minimumWidth",
                                               self.side_menu_container.width(), new_width, 500,
                                               QEasingCurve.InOutQuart)
        self.logo_animation = self.create_animation(self.frame_logo, b"maximumWidth",
                                                    self.frame_logo.width(), new_logo_width, 500,
                                                    QEasingCurve.InOutQuart)

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animation)
        self.anim_group.addAnimation(self.logo_animation)
        self.anim_group.start()

    @staticmethod
    def create_animation(target: QFrame, property_name: bytes, start_value: int, end_value: int, duration: int,
                         easing_curve: QEasingCurve):
        """
        Create a QPropertyAnimation with the given parameters.

        :param target: The target object to animate.
        :param property_name: The name of the property to animate.
        :param start_value: The start value of the animation.
        :param end_value: The end value of the animation.
        :param duration: The duration of the animation in milliseconds.
        :param easing_curve: The easing curve for the animation.
        :return: The created QPropertyAnimation.
        """
        animation = QPropertyAnimation(target, property_name)
        animation.setDuration(duration)
        animation.setStartValue(start_value)
        animation.setEndValue(end_value)
        animation.setEasingCurve(easing_curve)
        return animation

    def update_side_menu_icon(self, is_side_menu_expanded: bool) -> None:
        """
        Update the side menu icon based on its expanded state.

        :param is_side_menu_expanded: Flag indicating whether the side menu is expanded or not.
        """
        if is_side_menu_expanded:
            icon = ':/icons/icons/arrow-prev-svgrepo-com.svg'
        else:
            icon = ':/icons/icons/align-left-svgrepo-com.svg'

        self.show_side_menu_button.setIcon(QIcon(icon))

    def resizeEvent(self, event: QResizeEvent) -> None:
        """
        Handle the resize event of the window.

        This method is called when the window is resized. It updates the positions of the grip widgets to match the
        new size of the window.
        """
        # Update grip positions when the window is resized
        if self.grips:
            for grip in self.grips:
                grip.set_grip_position()

    def init_grips(self) -> None:
        """
        Initialize grip instances and add them to list of grips
        """
        # Create a list of edge values
        edge_values = [Qt.LeftEdge, Qt.RightEdge, Qt.TopEdge, Qt.BottomEdge]

        # Iterate over the edge values and create grip instances
        for edge in edge_values:
            grip = Grip(self, edge)
            self.grips.append(grip)

    def hide_grips(self) -> None:
        """
        Hide the grips.
        """
        for grip in self.grips:
            grip.hide()

    def show_grips(self) -> None:
        """
        Show the grips.
        """
        for grip in self.grips:
            grip.show()
