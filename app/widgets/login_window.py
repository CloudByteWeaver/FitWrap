import json
from pathlib import Path
from typing import Tuple, Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QTextEdit, QCheckBox
from cryptography.fernet import Fernet

from database.db_operations import is_login_available, add_user, verify_user, get_user_id
from app.interface import Interface
from app.ui.ui_login import Ui_LoginWindow


class LoginWindow(QWidget, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.login = None
        self.setupUi(self)
        self.main_window = None
        self.mouseClickPosition = None

        self.setWindowTitle('FitWrap')
        self.setWindowIcon(QIcon(':/icons/icons/logo.png'))

        # Hide warning labels
        self.login_error_label.hide()
        self.login_warning_label.hide()
        self.passwd_warning_label.hide()

        # Remove window title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Minimize window
        self.minimize_window_button.clicked.connect(self.showMinimized)

        # Close window
        self.close_window_button.clicked.connect(self.close)

        # Add click event/mouse event/drap event to the top header to move the window
        self.top_frame.mouseMoveEvent = self.move_window

        # Set page index
        self.alrdy_have_acc_btn.clicked.connect(lambda: self.page.setCurrentIndex(0))
        self.create_acc_btn.clicked.connect(lambda: self.page.setCurrentIndex(1))

        # Login page events
        self.sign_in_btn.clicked.connect(self.log_in)
        self.login_field.returnPressed.connect(self.log_in)
        self.password_field.returnPressed.connect(self.log_in)

        # Register page events
        self.register_btn.clicked.connect(self.register)
        self.login_register_field.returnPressed.connect(self.register)
        self.password_1_field.returnPressed.connect(self.register)
        self.password_2_field.returnPressed.connect(self.register)

    def get_login(self) -> str:
        if self.login is None:
            self.login = self.load_credentials()[0]
        return self.login

    def get_users_id(self) -> int:
        login = self.get_login()
        id = get_user_id(login)
        return id

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

    def open_main_window(self) -> None:
        """
        Opens the main window by hiding the current window and displaying the main interface.

        :return: None
        """
        # Hide the current window
        self.hide()

        # Set log in page as the current page
        self.page.setCurrentIndex(0)

        # Reset fields' values
        self.reset_widgets()

        # Create and display the main interface window
        if self.main_window is None:
            self.main_window = Interface(self)

        self.main_window.load_devices_data()
        self.main_window.show()

    def check_login(self) -> bool:
        """
        Check if the login is valid and available.

        :return: True if the login is valid and available, False otherwise.
        :rtype: bool
        """
        # Get the login input from the text field
        login = self.login_register_field.text()

        # Check if the login is at least 3 characters long
        if len(login) < 3:
            self._display_warning_message('At least 3 characters')
            return False
        # Check if the login is available
        elif is_login_available(login):
            self._hide_warning_message()
            return True
        else:
            self._display_warning_message('Login already taken.')
            return False

    def _display_warning_message(self, message: str) -> None:
        """
        Display a warning message.

        :param message: The warning message to display.
        :type message: str

        :return: None
        """
        self.login_warning_label.setText('  ' + message)
        self.login_warning_label.show()

    def _hide_warning_message(self) -> None:
        """
        Hide the warning message.

        :return: None
        """
        self.login_warning_label.hide()

    def check_password(self) -> bool:
        """
        Check if the password is valid.

        :return: True if the password is valid, False otherwise.
        :rtype: bool
        """
        # Get the text from password fields
        password1 = self.password_1_field.text()
        password2 = self.password_2_field.text()
        # Check if password length is less than 8 characters
        if len(password1) < 8:
            self.passwd_warning_label.setText('  At least 8 characters')
            if not self.passwd_warning_label.isVisible():
                self.passwd_warning_label.show()
            # Show password warning label if it's not visible
            if not self.passwd_warning_label.isVisible():
                self.passwd_warning_label.show()
        # Check if passwords do not match
        elif password1 != password2:
            self.passwd_warning_label.setText('  The passwords entered do not match.')
            # Show password warning label if it's not visible
            if not self.passwd_warning_label.isVisible():
                self.passwd_warning_label.show()
        else:
            # Hide password warning label
            if self.passwd_warning_label.isVisible():
                self.passwd_warning_label.hide()
            return True
        return False

    def register(self) -> None:
        """
        Registers the user using the provided login and password.

        :return: None
        """
        # Check if the login and password are correct
        correct_login = self.check_login()
        correct_password = self.check_password()

        # If both the login and password are correct, add the user and open the main window
        if correct_login and correct_password:
            login = self.login_register_field.text()
            password = self.password_1_field.text()
            add_user(login, password)
            self.open_main_window()

    def log_in(self) -> None:
        """
        Logs in the user using the provided login and password.
        
        :return: None
        """
        # Get the login, password, and remember me status
        login = self.login_field.text()
        password = self.password_field.text()
        remember_me = self.remember_me_ckbox.isChecked()

        # Check if login and password are provided
        if login != "" and password != "":
            # Verify the user's credentials
            if verify_user(login, password):
                self.login = login
                # Save credentials if 'remember me' is checked
                if remember_me:
                    self.save_credentials(login, password)

                # Hide the login error label if it's visible
                if self.login_error_label.isVisible():
                    self.login_error_label.hide()

                # Open the main window
                self.open_main_window()
            else:
                # Show the login error label if the credentials are invalid
                if not self.login_error_label.isVisible():
                    self.login_error_label.show()
        else:
            # Show the login error label if login or password are not provided
            if not self.login_error_label.isVisible():
                self.login_error_label.show()

    @staticmethod
    def generate_key() -> None:
        """
        Generate a key for encryption and save it into a file.
        
        :return: None
        """
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    def load_key(self) -> bytes:
        """
        Load the previously generated key.

        :return: The key.
        :rtype: bytes
        """
        try:
            with open("secret.key", "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            print("Encryption key not found. Generating a new key.")
            # Generate a new key:
            self.generate_key()
            with open("secret.key", "rb") as key_file:
                return key_file.read()
        except Exception as e:
            print("An error occurred while loading the key:", str(e))

    def save_credentials(self, login: str, password: str) -> None:
        """
        Encrypt the login and password and save them in a JSON file.

        :param login: The user's login.
        :type login: str
        :param password: The user's password.
        :type password: str

        :return: None
        """
        key = self.load_key()
        fernet = Fernet(key)

        # Encrypt the credentials
        encrypted_login = fernet.encrypt(login.encode())
        encrypted_password = fernet.encrypt(password.encode())

        # Save the encrypted credentials to a JSON file
        with open("credentials.json", "w") as file:
            json.dump({
                "login": encrypted_login.decode(),
                "password": encrypted_password.decode()
            }, file)

    def load_credentials(self) -> Tuple[Optional[str], Optional[str]]:
        """
        Load and decrypt the login and password from the JSON file.

        :return: The decrypted login and password.
        :rtype: Tuple[Optional[str], Optional[str]]
        """

        # Load the encryption key
        key = self.load_key()

        # Create a Fernet object with the encryption key
        fernet = Fernet(key)

        # Check if the credentials file exists
        if not Path("credentials.json").exists():
            return None, None

        # Load the encrypted credentials from the JSON file
        with open("credentials.json", "r") as file:
            credentials = json.load(file)

        # Decrypt the login and password
        decrypted_login = fernet.decrypt(credentials["login"].encode()).decode()
        decrypted_password = fernet.decrypt(credentials["password"].encode()).decode()

        return decrypted_login, decrypted_password

    @staticmethod
    def auto_login(saved_login: str, saved_password: str) -> bool:
        """
        Attempt to log the user in automatically with the saved credentials.

        :param saved_login: The saved login credentials.
        :type saved_login: str
        :param saved_password: The saved password credentials.
        :type saved_password: str

        :return: True if the user is successfully logged in, False otherwise.
        :rtype: bool
        """
        if saved_login and saved_password:
            return verify_user(saved_login, saved_password)
        return False
