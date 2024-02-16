# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwZgGqQ.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import resources.icons_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(703, 579)
        LoginWindow.setMinimumSize(QSize(703, 578))
        self.widget = QWidget(LoginWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 80, 330, 400))
        self.widget.setMinimumSize(QSize(330, 400))
        self.widget.setStyleSheet(u"QWidget#widget {\n"
"	background: qlineargradient(\n"
"    	x1: 0, y1: 1, x2: 0, y2: 0,\n"
"    	stop: 0.0 hsl(39, 76%, 75%),\n"
"    	stop: 0.31 hsl(39, 28%, 55%),\n"
"    	stop: 1.0 hsl(216, 18%, 16%)\n"
"  );\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 60, -1, -1)
        self.logo_img = QLabel(self.widget)
        self.logo_img.setObjectName(u"logo_img")
        self.logo_img.setMaximumSize(QSize(161, 161))
        self.logo_img.setStyleSheet(u"")
        self.logo_img.setPixmap(QPixmap(u":/icons/icons/logo.png"))
        self.logo_img.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.logo_img, 0, Qt.AlignHCenter)

        self.logo_label = QLabel(self.widget)
        self.logo_label.setObjectName(u"logo_label")
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(28)
        font.setBold(True)
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet(u"color: #222831;")

        self.verticalLayout_3.addWidget(self.logo_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_2 = QWidget(LoginWindow)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(350, 110, 320, 350))
        self.widget_2.setMinimumSize(QSize(320, 350))
        self.widget_2.setMaximumSize(QSize(16777215, 350))
        self.widget_2.setStyleSheet(u"QWidget#widget_2 {\n"
"	background-color: #EEEEEE;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(36, 0, -1, -1)
        self.top_frame = QFrame(self.widget_2)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.frame_3 = QFrame(self.top_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"color: rgba(0, 0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame_3)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMinimumSize(QSize(15, 15))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        self.minimize_window_button.setFont(font1)
        self.minimize_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_window_button.setStyleSheet(u"QPushButton#minimize_window_button {\n"
"	background-color: #00CA4E;\n"
"	border-radius: 7px;\n"
"	text-align: center;\n"
"	margin-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton#minimize_window_button:hover {\n"
"	background-color: #00ff62;\n"
"}\n"
"\n"
"QPushButton#minimize_window_button:pressed {\n"
"	background-color: #1EB859;\n"
"}")

        self.horizontalLayout.addWidget(self.minimize_window_button)

        self.close_window_button = QPushButton(self.frame_3)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(15, 15))
        self.close_window_button.setFont(font1)
        self.close_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_window_button.setStyleSheet(u"QPushButton#close_window_button {\n"
"	background-color: #FF605C;\n"
"	border-radius: 7px;\n"
"	text-align: center;\n"
"	margin-bottom: 1px;\n"
"}\n"
"\n"
"QPushButton#close_window_button:hover {\n"
"	background-color: #FF8C89;\n"
"}\n"
"\n"
"QPushButton#close_window_button:pressed {\n"
"	background-color: #B7221F;\n"
"}")

        self.horizontalLayout.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.top_frame, 0, Qt.AlignTop)

        self.page = QStackedWidget(self.widget_2)
        self.page.setObjectName(u"page")
        self.log_in_page = QWidget()
        self.log_in_page.setObjectName(u"log_in_page")
        self.frame_2 = QFrame(self.log_in_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 275, 310))
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgba(0, 0, 0, 0);\n"
"	border-bottom-color: #2F4858;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.log_in_label = QLabel(self.frame_2)
        self.log_in_label.setObjectName(u"log_in_label")
        self.log_in_label.setGeometry(QRect(10, 10, 251, 55))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.log_in_label.setFont(font2)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 252, 191))
        self.login_form = QVBoxLayout(self.layoutWidget)
        self.login_form.setObjectName(u"login_form")
        self.login_form.setContentsMargins(0, 0, 0, 0)
        self.login_field = QLineEdit(self.layoutWidget)
        self.login_field.setObjectName(u"login_field")
        self.login_field.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(10)
        self.login_field.setFont(font3)
        self.login_field.setStyleSheet(u"")

        self.login_form.addWidget(self.login_field)

        self.password_field = QLineEdit(self.layoutWidget)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setMinimumSize(QSize(0, 40))
        self.password_field.setFont(font3)
        self.password_field.setStyleSheet(u"")
        self.password_field.setEchoMode(QLineEdit.Password)

        self.login_form.addWidget(self.password_field)

        self.remember_me_ckbox = QCheckBox(self.layoutWidget)
        self.remember_me_ckbox.setObjectName(u"remember_me_ckbox")
        self.remember_me_ckbox.setCursor(QCursor(Qt.PointingHandCursor))

        self.login_form.addWidget(self.remember_me_ckbox)

        self.login_error_label = QLabel(self.layoutWidget)
        self.login_error_label.setObjectName(u"login_error_label")
        self.login_error_label.setMaximumSize(QSize(250, 15))
        self.login_error_label.setFont(font1)
        self.login_error_label.setStyleSheet(u"color: red;")

        self.login_form.addWidget(self.login_error_label)

        self.sign_in_btn = QPushButton(self.layoutWidget)
        self.sign_in_btn.setObjectName(u"sign_in_btn")
        self.sign_in_btn.setMinimumSize(QSize(250, 40))
        self.sign_in_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sign_in_btn.setStyleSheet(u"QPushButton#sign_in_btn {\n"
"	background-color: #F0CF90;\n"
"	color: black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#sign_in_btn:hover {\n"
"	background-color: #F3D8A5;\n"
"}\n"
"\n"
"QPushButton#sign_in_btn:pressed {\n"
"	background-color: #C3943C;\n"
"}")

        self.login_form.addWidget(self.sign_in_btn)

        self.create_acc_btn = QPushButton(self.frame_2)
        self.create_acc_btn.setObjectName(u"create_acc_btn")
        self.create_acc_btn.setGeometry(QRect(10, 280, 101, 24))
        self.create_acc_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_acc_btn.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.page.addWidget(self.log_in_page)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.frame_4 = QFrame(self.register_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 295, 326))
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgba(0, 0, 0, 0);\n"
"	border-bottom-color: #2F4858;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.register_label = QLabel(self.frame_4)
        self.register_label.setObjectName(u"register_label")
        self.register_label.setGeometry(QRect(10, 10, 251, 55))
        self.register_label.setFont(font2)
        self.layoutWidget_2 = QWidget(self.frame_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 50, 252, 244))
        self.register_form = QVBoxLayout(self.layoutWidget_2)
        self.register_form.setObjectName(u"register_form")
        self.register_form.setContentsMargins(0, 0, 0, 0)
        self.login_register_field = QLineEdit(self.layoutWidget_2)
        self.login_register_field.setObjectName(u"login_register_field")
        self.login_register_field.setMinimumSize(QSize(0, 40))
        self.login_register_field.setFont(font3)
        self.login_register_field.setStyleSheet(u"")

        self.register_form.addWidget(self.login_register_field)

        self.login_warning_label = QLabel(self.layoutWidget_2)
        self.login_warning_label.setObjectName(u"login_warning_label")
        self.login_warning_label.setEnabled(True)
        self.login_warning_label.setMaximumSize(QSize(250, 15))
        self.login_warning_label.setFont(font1)
        self.login_warning_label.setStyleSheet(u"color: red;")
        self.login_warning_label.setInputMethodHints(Qt.ImhNone)

        self.register_form.addWidget(self.login_warning_label)

        self.password_1_field = QLineEdit(self.layoutWidget_2)
        self.password_1_field.setObjectName(u"password_1_field")
        self.password_1_field.setMinimumSize(QSize(0, 40))
        self.password_1_field.setFont(font3)
        self.password_1_field.setStyleSheet(u"")
        self.password_1_field.setEchoMode(QLineEdit.Password)

        self.register_form.addWidget(self.password_1_field)

        self.password_2_field = QLineEdit(self.layoutWidget_2)
        self.password_2_field.setObjectName(u"password_2_field")
        self.password_2_field.setMinimumSize(QSize(0, 40))
        self.password_2_field.setFont(font3)
        self.password_2_field.setStyleSheet(u"")
        self.password_2_field.setEchoMode(QLineEdit.Password)

        self.register_form.addWidget(self.password_2_field)

        self.passwd_warning_label = QLabel(self.layoutWidget_2)
        self.passwd_warning_label.setObjectName(u"passwd_warning_label")
        self.passwd_warning_label.setMaximumSize(QSize(250, 16))
        self.passwd_warning_label.setFont(font1)
        self.passwd_warning_label.setStyleSheet(u"color: red;")

        self.register_form.addWidget(self.passwd_warning_label)

        self.register_btn = QPushButton(self.layoutWidget_2)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setMinimumSize(QSize(250, 40))
        self.register_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_btn.setStyleSheet(u"QPushButton#register_btn {\n"
"	background-color: #F0CF90;\n"
"	color: black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#register_btn:hover {\n"
"	background-color: #F3D8A5;\n"
"}\n"
"\n"
"QPushButton#register_btn:pressed {\n"
"	background-color: #C3943C;\n"
"}")

        self.register_form.addWidget(self.register_btn)

        self.login_warning_label.raise_()
        self.login_register_field.raise_()
        self.password_1_field.raise_()
        self.password_2_field.raise_()
        self.register_btn.raise_()
        self.passwd_warning_label.raise_()
        self.alrdy_have_acc_btn = QPushButton(self.frame_4)
        self.alrdy_have_acc_btn.setObjectName(u"alrdy_have_acc_btn")
        self.alrdy_have_acc_btn.setGeometry(QRect(10, 290, 131, 24))
        self.alrdy_have_acc_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.alrdy_have_acc_btn.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.page.addWidget(self.register_page)

        self.verticalLayout.addWidget(self.page)

        self.widget_2.raise_()
        self.widget.raise_()

        self.retranslateUi(LoginWindow)

        self.page.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Form", None))
        self.logo_img.setText("")
        self.logo_label.setText(QCoreApplication.translate("LoginWindow", u"FitWrap", None))
        self.minimize_window_button.setText(QCoreApplication.translate("LoginWindow", u".", None))
        self.close_window_button.setText(QCoreApplication.translate("LoginWindow", u".", None))
        self.log_in_label.setText(QCoreApplication.translate("LoginWindow", u"Log In", None))
        self.login_field.setInputMask("")
        self.login_field.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.password_field.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.remember_me_ckbox.setText(QCoreApplication.translate("LoginWindow", u"Remember me", None))
        self.login_error_label.setText(QCoreApplication.translate("LoginWindow", u"  The login or password is incorrect.", None))
        self.sign_in_btn.setText(QCoreApplication.translate("LoginWindow", u"Sign in", None))
        self.create_acc_btn.setText(QCoreApplication.translate("LoginWindow", u"Create an account", None))
        self.register_label.setText(QCoreApplication.translate("LoginWindow", u"Register", None))
        self.login_register_field.setInputMask("")
        self.login_register_field.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.login_warning_label.setText(QCoreApplication.translate("LoginWindow", u"  Login warning placeholder.", None))
        self.password_1_field.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.password_2_field.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Confirm password", None))
        self.passwd_warning_label.setText(QCoreApplication.translate("LoginWindow", u"  Password warning placeholder", None))
        self.register_btn.setText(QCoreApplication.translate("LoginWindow", u"Register", None))
        self.alrdy_have_acc_btn.setText(QCoreApplication.translate("LoginWindow", u"Already have an account", None))
    # retranslateUi

