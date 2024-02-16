# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_deviceAuVxjS.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources.icons_rc

class Ui_AddDeviceWindow(object):
    def setupUi(self, AddDeviceWindow):
        if not AddDeviceWindow.objectName():
            AddDeviceWindow.setObjectName(u"AddDeviceWindow")
        AddDeviceWindow.resize(580, 436)
        AddDeviceWindow.setMinimumSize(QSize(580, 436))
        AddDeviceWindow.setStyleSheet(u"color: #EEE;\n"
"border: none;")
        self.verticalLayout = QVBoxLayout(AddDeviceWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QWidget(AddDeviceWindow)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"#header_frame {\n"
"	background-color: #222831;\n"
"	border-top-right-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"}\n"
"\n"
"#header_frame * {\n"
"	color: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.app_icon = QLabel(self.header_frame)
        self.app_icon.setObjectName(u"app_icon")
        self.app_icon.setMinimumSize(QSize(0, 0))
        self.app_icon.setMaximumSize(QSize(20, 20))
        self.app_icon.setPixmap(QPixmap(u":/icons/icons/logo.png"))
        self.app_icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.app_icon)

        self.window_title = QLabel(self.header_frame)
        self.window_title.setObjectName(u"window_title")
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        self.window_title.setFont(font)
        self.window_title.setStyleSheet(u"color: #EEE;")

        self.horizontalLayout.addWidget(self.window_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minimize_window_btn = QPushButton(self.header_frame)
        self.minimize_window_btn.setObjectName(u"minimize_window_btn")
        self.minimize_window_btn.setMinimumSize(QSize(15, 15))
        self.minimize_window_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_window_btn.setStyleSheet(u"#minimize_window_btn {\n"
"	background-color: #00CA4E;\n"
"	border-radius: 7px;\n"
"	text-align: center;\n"
"	margin-bottom: 1px;\n"
"}\n"
"\n"
"#minimize_window_btn:hover {\n"
"	background-color: #00ff62;\n"
"}\n"
"\n"
"#minimize_window_btn:pressed {\n"
"	background-color: #1EB859;\n"
"}")

        self.horizontalLayout.addWidget(self.minimize_window_btn)

        self.close_window_btn = QPushButton(self.header_frame)
        self.close_window_btn.setObjectName(u"close_window_btn")
        self.close_window_btn.setMinimumSize(QSize(15, 15))
        self.close_window_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_window_btn.setStyleSheet(u"#close_window_btn {\n"
"	background-color: #FF605C;\n"
"	border-radius: 7px;\n"
"	text-align: center;\n"
"	margin-bottom: 1px;\n"
"}\n"
"\n"
"#close_window_btn:hover {\n"
"	background-color: #FF8C89;\n"
"}\n"
"\n"
"#close_window_btn:pressed {\n"
"	background-color: #B7221F;\n"
"}")

        self.horizontalLayout.addWidget(self.close_window_btn)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QWidget(AddDeviceWindow)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setStyleSheet(u"#main_body_frame {\n"
"	background-color: #393E46;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	border: 2px solid #222831;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.main_body_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.widget_3 = QWidget(self.main_body_frame)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.select_device_icon_btn = QPushButton(self.widget)
        self.select_device_icon_btn.setObjectName(u"select_device_icon_btn")
        self.select_device_icon_btn.setMinimumSize(QSize(150, 30))
        self.select_device_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_device_icon_btn.setStyleSheet(u"QPushButton {	\n"
"	color: #222831;\n"
"	background-color: #F0CF90;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #C3943C;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/folder-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.select_device_icon_btn.setIcon(icon)

        self.verticalLayout_4.addWidget(self.select_device_icon_btn, 0, Qt.AlignHCenter)

        self.selected_devic_icon_preview = QLabel(self.widget)
        self.selected_devic_icon_preview.setObjectName(u"selected_devic_icon_preview")
        self.selected_devic_icon_preview.setMaximumSize(QSize(250, 250))
        self.selected_devic_icon_preview.setStyleSheet(u"")
        self.selected_devic_icon_preview.setPixmap(QPixmap(u":/icons/icons/default_device_icon.jpg"))
        self.selected_devic_icon_preview.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.selected_devic_icon_preview, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #40464F;\n"
"	border-bottom-color: #F0CF90;\n"
"	background-color: #40464F;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, 30, 30)
        self.brand_label = QLabel(self.widget_2)
        self.brand_label.setObjectName(u"brand_label")
        self.brand_label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_5.addWidget(self.brand_label, 0, Qt.AlignBottom)

        self.brand_field = QLineEdit(self.widget_2)
        self.brand_field.setObjectName(u"brand_field")

        self.verticalLayout_5.addWidget(self.brand_field)

        self.model_label = QLabel(self.widget_2)
        self.model_label.setObjectName(u"model_label")
        self.model_label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_5.addWidget(self.model_label, 0, Qt.AlignBottom)

        self.model_field = QLineEdit(self.widget_2)
        self.model_field.setObjectName(u"model_field")

        self.verticalLayout_5.addWidget(self.model_field)

        self.type_label = QLabel(self.widget_2)
        self.type_label.setObjectName(u"type_label")
        self.type_label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_5.addWidget(self.type_label, 0, Qt.AlignBottom)

        self.type_field = QLineEdit(self.widget_2)
        self.type_field.setObjectName(u"type_field")

        self.verticalLayout_5.addWidget(self.type_field, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.main_body_frame)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.add_device_warning_label = QLabel(self.widget_4)
        self.add_device_warning_label.setObjectName(u"add_device_warning_label")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(10)
        self.add_device_warning_label.setFont(font1)
        self.add_device_warning_label.setStyleSheet(u"color: #FF605C;")
        self.add_device_warning_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.add_device_warning_label, 0, Qt.AlignVCenter)

        self.add_device_btn = QPushButton(self.widget_4)
        self.add_device_btn.setObjectName(u"add_device_btn")
        self.add_device_btn.setMinimumSize(QSize(130, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.add_device_btn.setFont(font2)
        self.add_device_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_device_btn.setStyleSheet(u"QPushButton {	\n"
"	color: #222831;\n"
"	background-color: #F0CF90;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #C3943C;\n"
"}")

        self.verticalLayout_3.addWidget(self.add_device_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_4, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.main_body_frame)


        self.retranslateUi(AddDeviceWindow)

        QMetaObject.connectSlotsByName(AddDeviceWindow)
    # setupUi

    def retranslateUi(self, AddDeviceWindow):
        AddDeviceWindow.setWindowTitle(QCoreApplication.translate("AddDeviceWindow", u"Form", None))
        self.app_icon.setText("")
        self.window_title.setText(QCoreApplication.translate("AddDeviceWindow", u"FitWrap - Add device", None))
        self.minimize_window_btn.setText(QCoreApplication.translate("AddDeviceWindow", u".", None))
        self.close_window_btn.setText(QCoreApplication.translate("AddDeviceWindow", u".", None))
        self.select_device_icon_btn.setText(QCoreApplication.translate("AddDeviceWindow", u"Select icon (optional)", None))
        self.selected_devic_icon_preview.setText("")
        self.brand_label.setText(QCoreApplication.translate("AddDeviceWindow", u"Brand:", None))
        self.model_label.setText(QCoreApplication.translate("AddDeviceWindow", u"Model:", None))
        self.type_label.setText(QCoreApplication.translate("AddDeviceWindow", u"Type:", None))
        self.add_device_warning_label.setText(QCoreApplication.translate("AddDeviceWindow", u"Fields cannot be empty.", None))
        self.add_device_btn.setText(QCoreApplication.translate("AddDeviceWindow", u"Add", None))
    # retranslateUi

