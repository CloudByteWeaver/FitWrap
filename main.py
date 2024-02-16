import sys
from PySide6.QtWidgets import QApplication
from app.widgets.login_window import LoginWindow


if __name__ == '__main__':
    app = QApplication([])

    window = LoginWindow()

    saved_login, saved_password = window.load_credentials()
    if window.auto_login(saved_login, saved_password):
        window.open_main_window()
    else:
        window.show()

    sys.exit(app.exec())
