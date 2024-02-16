import sys  # Only needed for access to command line arguments
from PySide6.QtWidgets import QApplication
from app.widgets.login_window import LoginWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Pass in sys.argv to allow command line arguments or if not just []

    window = LoginWindow()

    saved_login, saved_password = window.load_credentials()
    if window.auto_login(saved_login, saved_password):
        window.open_main_window()
    else:
        window.show()

    # app.exec()
    sys.exit(app.exec())
