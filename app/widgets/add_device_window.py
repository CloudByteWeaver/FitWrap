import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QFileDialog, QLineEdit, QTextEdit

from database.db_operations import add_device
from app.ui.ui_add_device import Ui_AddDeviceWindow


class AddDeviceWindow(QWidget, Ui_AddDeviceWindow):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.mouseClickPosition = None
        self.setupUi(self)
        self.main_window = main_window
        self.selected_file_path = ""

        self.add_device_warning_label.hide()

        # Set window title and icon
        self.setWindowTitle('FitWrap - Add device')
        self.setWindowIcon(QIcon(':/icons/icons/logo.png'))

        # Remove window title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Minimize window
        self.minimize_window_btn.clicked.connect(self.showMinimized)

        # Close window
        self.close_window_btn.clicked.connect(self.close)

        self.header_frame.mouseMoveEvent = self.move_window
        self.select_device_icon_btn.clicked.connect(self.browse_files)
        self.add_device_btn.clicked.connect(self.check_fields)

    def check_fields(self) -> None:
        """
        Check if the text fields are empty and show a warning label if necessary.

        :return: None
        """
        # Check if any of the text fields are empty
        if (self.brand_field.text().strip() == "" or self.model_field.text().strip() == ""
                or self.type_field.text().strip() == ""):
            # Show the warning label if any text field is empty
            self.add_device_warning_label.show()
        else:
            # Hide the warning label if it's visible
            if self.add_device_warning_label.isVisible():
                self.add_device_warning_label.hide()

            # Prepare parameters for adding a new device
            params = {
                'user_id': self.main_window.login_window.get_users_id(),
                'icon_path': self.selected_file_path if self.selected_file_path != "" else QIcon(
                    ":/icons/icons/default_device_icon.jpg"),
                'brand': self.brand_field.text(),
                'model': self.model_field.text(),
                'type': self.type_field.text()
            }
            # Call the add_device function with the prepared parameters
            add_device(**params)
            # Close the current window
            self.close()
            self.reset_widgets()
            self.main_window.load_devices_data()

    def browse_files(self) -> None:
        """
        Opens a file dialog to browse and select an image file.

        :return: None
        """
        # Set the default directory to the user's Pictures folder
        pictures_path = os.path.expanduser("~/Pictures")

        # Open the file dialog to select an image file
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', pictures_path, 'Images (*.png *.jpeg *.jpg)')
        # If a file is selected, display the image on the UI and store the file path
        if file_name:
            self.selected_devic_icon_preview.setPixmap(QPixmap(file_name))
            self.selected_file_path = file_name

    def move_window(self, event: QMouseEvent) -> None:
        """
        Function to move window on mouse drag event on the title bar

        :param event: The mouse event that triggers the window movement. This event contains the current position of the
        mouse cursor.

        :return: None
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

    def reset_widgets(self) -> None:
        """
        Resets all the QLineEdit, QTextEdit, and QCheckBox widgets found as children.

        :return: None
        """
        self.selected_file_path = ""
        self.selected_devic_icon_preview.setPixmap(QPixmap(":/icons/icons/default_device_icon.jpg"))
        for widget in self.findChildren(QWidget):
            if isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QTextEdit):
                widget.clear()
