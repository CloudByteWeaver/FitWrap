# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceCWzkLF.ui'
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
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import resources.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1135, 732)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	color: #EEEEEE;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 10px 0 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #F0CF90;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"     background: none;\n"
"}\n"
"\n"
"QScro"
                        "llBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 10px 0 10px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {	\n"
"	background: #F0CF90;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	 background: rgb(52, 59, 72);\n"
"     height: 20px;\n"
"	 border-bottom-left-radius: 4px;\n"
"     border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"    height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     ba"
                        "ckground: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 23px;\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(\":/icons/icons/arrow-down-svgrepo-com.svg\");\n"
"    width: 23px;\n"
"    height: 23px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	border-top: 2px solid #393E46;\n"
"	height: 41px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(57, 62, 70, 0.5);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_container = QFrame(self.centralwidget)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setEnabled(True)
        self.side_menu_container.setMinimumSize(QSize(60, 0))
        self.side_menu_container.setMaximumSize(QSize(0, 16777215))
        self.side_menu_container.setSizeIncrement(QSize(0, 0))
        self.side_menu_container.setStyleSheet(u"#side_menu_container {\n"
"	background-color: #222831;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"}")
        self.side_menu_container.setFrameShape(QFrame.NoFrame)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.side_menu_container)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.side_menu_container)
        self.side_menu.setObjectName(u"side_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy)
        self.side_menu.setMinimumSize(QSize(0, 0))
        self.side_menu.setStyleSheet(u".QPushButton {\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border-left: 16px solid transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"	background-color: #393E46;\n"
"}\n"
"\n"
".QPushButton:pressed {	\n"
"	background-color: #858585;\n"
"}")
        self.side_menu.setFrameShape(QFrame.NoFrame)
        self.side_menu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.side_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.side_menu)
        self.frame_logo.setObjectName(u"frame_logo")
        sizePolicy.setHeightForWidth(self.frame_logo.sizePolicy().hasHeightForWidth())
        self.frame_logo.setSizePolicy(sizePolicy)
        self.frame_logo.setMinimumSize(QSize(130, 45))
        self.frame_logo.setMaximumSize(QSize(16777215, 45))
        self.frame_logo.setSizeIncrement(QSize(0, 0))
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 4, 0, 4)
        self.logo = QLabel(self.frame_logo)
        self.logo.setObjectName(u"logo")
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(0, 0))
        self.logo.setMaximumSize(QSize(130, 60))
        self.logo.setPixmap(QPixmap(u":/icons/icons/fitwrap-low-resolution-logo-color-on-transparent-background.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)


        self.verticalLayout_4.addWidget(self.frame_logo)

        self.frame_8 = QFrame(self.side_menu)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.frame_8)
        self.home_btn.setObjectName(u"home_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy2)
        self.home_btn.setMinimumSize(QSize(0, 45))
        self.home_btn.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.home_btn.setFont(font)
        self.home_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn.setStyleSheet(u"background-image: url(:/icons/icons/house-03-svgrepo-com.svg);")
        self.home_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_6.addWidget(self.home_btn)

        self.add_activity_btn = QPushButton(self.frame_8)
        self.add_activity_btn.setObjectName(u"add_activity_btn")
        sizePolicy2.setHeightForWidth(self.add_activity_btn.sizePolicy().hasHeightForWidth())
        self.add_activity_btn.setSizePolicy(sizePolicy2)
        self.add_activity_btn.setMinimumSize(QSize(0, 45))
        self.add_activity_btn.setFont(font)
        self.add_activity_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_activity_btn.setStyleSheet(u"background-image: url(:/icons/icons/file-plus-alt-1-svgrepo-com.svg);")
        self.add_activity_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_6.addWidget(self.add_activity_btn)

        self.manage_devices_btn = QPushButton(self.frame_8)
        self.manage_devices_btn.setObjectName(u"manage_devices_btn")
        sizePolicy2.setHeightForWidth(self.manage_devices_btn.sizePolicy().hasHeightForWidth())
        self.manage_devices_btn.setSizePolicy(sizePolicy2)
        self.manage_devices_btn.setMinimumSize(QSize(0, 45))
        self.manage_devices_btn.setFont(font)
        self.manage_devices_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.manage_devices_btn.setStyleSheet(u"background-image: url(:/icons/icons/smartwatch-1-svgrepo-com.svg);")
        self.manage_devices_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_6.addWidget(self.manage_devices_btn)

        self.activities_btn = QPushButton(self.frame_8)
        self.activities_btn.setObjectName(u"activities_btn")
        sizePolicy2.setHeightForWidth(self.activities_btn.sizePolicy().hasHeightForWidth())
        self.activities_btn.setSizePolicy(sizePolicy2)
        self.activities_btn.setMinimumSize(QSize(0, 45))
        self.activities_btn.setMaximumSize(QSize(16777215, 16777215))
        self.activities_btn.setFont(font)
        self.activities_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.activities_btn.setStyleSheet(u"background-image: url(:/icons/icons/running-svgrepo-com.svg);")
        self.activities_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_6.addWidget(self.activities_btn)

        self.map_btn = QPushButton(self.frame_8)
        self.map_btn.setObjectName(u"map_btn")
        sizePolicy2.setHeightForWidth(self.map_btn.sizePolicy().hasHeightForWidth())
        self.map_btn.setSizePolicy(sizePolicy2)
        self.map_btn.setMinimumSize(QSize(0, 45))
        self.map_btn.setFont(font)
        self.map_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.map_btn.setStyleSheet(u"background-image: url(:/icons/icons/map-location-pin-svgrepo-com.svg);")
        self.map_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_6.addWidget(self.map_btn)

        self.compare_btn = QPushButton(self.frame_8)
        self.compare_btn.setObjectName(u"compare_btn")
        sizePolicy2.setHeightForWidth(self.compare_btn.sizePolicy().hasHeightForWidth())
        self.compare_btn.setSizePolicy(sizePolicy2)
        self.compare_btn.setMinimumSize(QSize(0, 45))
        self.compare_btn.setFont(font)
        self.compare_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.compare_btn.setStyleSheet(u"background-image: url(:/icons/icons/code-compare-svgrepo-com.svg);")
        self.compare_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_6.addWidget(self.compare_btn)


        self.verticalLayout_4.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.side_buttons_container = QFrame(self.side_menu)
        self.side_buttons_container.setObjectName(u"side_buttons_container")
        self.side_buttons_container.setMinimumSize(QSize(0, 0))
        self.side_buttons_container.setStyleSheet(u"")
        self.side_buttons_container.setFrameShape(QFrame.StyledPanel)
        self.side_buttons_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.side_buttons_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.faq_btn = QPushButton(self.side_buttons_container)
        self.faq_btn.setObjectName(u"faq_btn")
        sizePolicy2.setHeightForWidth(self.faq_btn.sizePolicy().hasHeightForWidth())
        self.faq_btn.setSizePolicy(sizePolicy2)
        self.faq_btn.setMinimumSize(QSize(0, 45))
        self.faq_btn.setFont(font)
        self.faq_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.faq_btn.setStyleSheet(u"background-image: url(:/icons/icons/faq-svgrepo-com.svg);")
        self.faq_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.faq_btn)

        self.settings_btn = QPushButton(self.side_buttons_container)
        self.settings_btn.setObjectName(u"settings_btn")
        sizePolicy2.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy2)
        self.settings_btn.setMinimumSize(QSize(0, 45))
        self.settings_btn.setMaximumSize(QSize(16777215, 16777215))
        self.settings_btn.setFont(font)
        self.settings_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_btn.setStyleSheet(u"background-image: url(:/icons/icons/gear-svgrepo-com.svg);")
        self.settings_btn.setIconSize(QSize(28, 28))

        self.verticalLayout_5.addWidget(self.settings_btn)


        self.verticalLayout_4.addWidget(self.side_buttons_container, 0, Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.side_menu)


        self.horizontalLayout.addWidget(self.side_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy1.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy1)
        self.header_frame.setMinimumSize(QSize(0, 45))
        self.header_frame.setMaximumSize(QSize(16777215, 45))
        self.header_frame.setStyleSheet(u"#header_frame {\n"
"	border-top-right-radius: 7px;\n"
"	background-color: #222831;\n"
"}\n"
"\n"
"#header_frame * {\n"
"	background-color: #222831;\n"
"	color: #EEEEEE;\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.header_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(6, 2, 6, 2)
        self.right_header_side = QWidget(self.header_frame)
        self.right_header_side.setObjectName(u"right_header_side")
        self.horizontalLayout_9 = QHBoxLayout(self.right_header_side)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.user_buttons = QFrame(self.right_header_side)
        self.user_buttons.setObjectName(u"user_buttons")
        self.user_buttons.setMinimumSize(QSize(0, 41))
        self.user_buttons.setStyleSheet(u"QFrame#user_buttons {\n"
"	border: 2px solid rgba(0, 0, 0, 0);\n"
"	border-right-color: #393E46;\n"
"	padding-right: 7px;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393E46;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #858585;\n"
"}")
        self.user_buttons.setFrameShape(QFrame.StyledPanel)
        self.user_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.user_buttons)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notifications_btn = QPushButton(self.user_buttons)
        self.notifications_btn.setObjectName(u"notifications_btn")
        self.notifications_btn.setMaximumSize(QSize(27, 27))
        self.notifications_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/bell-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notifications_btn.setIcon(icon)
        self.notifications_btn.setIconSize(QSize(21, 21))

        self.horizontalLayout_6.addWidget(self.notifications_btn)

        self.account_btn = QPushButton(self.user_buttons)
        self.account_btn.setObjectName(u"account_btn")
        self.account_btn.setMaximumSize(QSize(27, 27))
        self.account_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.account_btn.setIcon(icon1)
        self.account_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_6.addWidget(self.account_btn)


        self.horizontalLayout_9.addWidget(self.user_buttons, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.right_header_side, 0, 2, 1, 1)

        self.select_device_frame = QFrame(self.header_frame)
        self.select_device_frame.setObjectName(u"select_device_frame")
        self.select_device_frame.setStyleSheet(u"#select_device_frame {\n"
"	border-left: 2px solid #393E46;\n"
"	border-right: 2px solid #393E46;\n"
"	padding-left: 7px;\n"
"	padding-right: 7px;\n"
"}")
        self.select_device_frame.setFrameShape(QFrame.StyledPanel)
        self.select_device_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.select_device_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.selected_device_cbox = QComboBox(self.select_device_frame)
        icon2 = QIcon()
        icon2.addFile(u":/watch icon/watch icons/HAUWEI-GT3-Pro.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.selected_device_cbox.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/watch icon/watch icons/Samsung-Watch-6-44mm-graphite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selected_device_cbox.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/watch icon/watch icons/garmin_forerunner_955.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.selected_device_cbox.addItem(icon4, "")
        self.selected_device_cbox.setObjectName(u"selected_device_cbox")
        self.selected_device_cbox.setMinimumSize(QSize(0, 41))
        self.selected_device_cbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.selected_device_cbox.setStyleSheet(u"QComboBox::drop-down {\n"
"    width: 23px;\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(\":/icons/icons/arrow-down-svgrepo-com.svg\");\n"
"    width: 23px;\n"
"    height: 23px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	border-top: 2px solid #393E46;\n"
"	height: 41px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: rgba(57, 62, 70, 0.5);\n"
"}")
        self.selected_device_cbox.setIconSize(QSize(41, 41))
        self.selected_device_cbox.setFrame(True)

        self.horizontalLayout_7.addWidget(self.selected_device_cbox)


        self.gridLayout.addWidget(self.select_device_frame, 0, 1, 1, 1)

        self.left_header_side = QFrame(self.header_frame)
        self.left_header_side.setObjectName(u"left_header_side")
        self.left_header_side.setFrameShape(QFrame.StyledPanel)
        self.left_header_side.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.left_header_side)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.show_side_menu_button = QPushButton(self.left_header_side)
        self.show_side_menu_button.setObjectName(u"show_side_menu_button")
        self.show_side_menu_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/align-left-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.show_side_menu_button.setIcon(icon5)
        self.show_side_menu_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.show_side_menu_button, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.gridLayout.addWidget(self.left_header_side, 0, 0, 1, 1)

        self.control_buttons = QFrame(self.header_frame)
        self.control_buttons.setObjectName(u"control_buttons")
        self.control_buttons.setMinimumSize(QSize(90, 41))
        self.control_buttons.setMaximumSize(QSize(90, 21))
        self.control_buttons.setStyleSheet(u"#control_buttons {\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"#close_window_button {\n"
"	background-color: #FF605C;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#close_window_button:hover {\n"
"	background-color: #FF8C89;\n"
"}\n"
"\n"
"#close_window_button:pressed {\n"
"	background-color: #B7221F;\n"
"}\n"
"\n"
"#maximize_window_button {\n"
"	background-color: #FFAD14;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#maximize_window_button:hover {\n"
"	background-color: #FFC789;\n"
"}\n"
"\n"
"#maximize_window_button:pressed {\n"
"	background-color: #B7821F;\n"
"}\n"
"\n"
"#minimize_window_button {\n"
"	background-color: #00CA4E;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#minimize_window_button:hover {\n"
"	background-color: #00ff62;\n"
"}\n"
"\n"
"#minimize_window_button:pressed {\n"
"	background-color: #1EB859;\n"
"}")
        self.control_buttons.setFrameShape(QFrame.StyledPanel)
        self.control_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.control_buttons)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.control_buttons)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMaximumSize(QSize(22, 22))
        self.minimize_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/arrow-income-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon6)
        self.minimize_window_button.setIconSize(QSize(21, 21))

        self.horizontalLayout_5.addWidget(self.minimize_window_button, 0, Qt.AlignLeft)

        self.maximize_window_button = QPushButton(self.control_buttons)
        self.maximize_window_button.setObjectName(u"maximize_window_button")
        self.maximize_window_button.setMaximumSize(QSize(22, 22))
        self.maximize_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/arrow-increase-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_window_button.setIcon(icon7)
        self.maximize_window_button.setIconSize(QSize(21, 21))

        self.horizontalLayout_5.addWidget(self.maximize_window_button, 0, Qt.AlignHCenter)

        self.close_window_button = QPushButton(self.control_buttons)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(0, 0))
        self.close_window_button.setMaximumSize(QSize(22, 22))
        self.close_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_window_button.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/close-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon8)
        self.close_window_button.setIconSize(QSize(21, 21))

        self.horizontalLayout_5.addWidget(self.close_window_button, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.control_buttons, 0, 3, 1, 1, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy3)
        self.main_body_contents.setStyleSheet(u"background-color: #393E46;")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.page = QStackedWidget(self.main_body_contents)
        self.page.setObjectName(u"page")
        self.account_page = QWidget()
        self.account_page.setObjectName(u"account_page")
        self.verticalLayout_9 = QVBoxLayout(self.account_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.account_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 15, 20, 15)
        self.log_out_btn = QPushButton(self.frame)
        self.log_out_btn.setObjectName(u"log_out_btn")
        self.log_out_btn.setMinimumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.log_out_btn.setFont(font1)
        self.log_out_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.log_out_btn.setStyleSheet(u"#log_out_btn {\n"
"	color: #222831;\n"
"	background-color: #FF605C;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"#log_out_btn:pressed {\n"
"	background-color: #B7221F;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/log-out-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.log_out_btn.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.log_out_btn, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.account_page)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 60)
        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(491, 241))
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_4.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_4)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid #40464F;\n"
"	border-bottom-color: #F0CF90;\n"
"	background-color: #40464F;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}")
        self.formLayout = QFormLayout(self.widget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.current_password_field = QLineEdit(self.widget_3)
        self.current_password_field.setObjectName(u"current_password_field")
        self.current_password_field.setMinimumSize(QSize(0, 25))
        self.current_password_field.setFont(font1)
        self.current_password_field.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.current_password_field)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.new_password_1_field = QLineEdit(self.widget_3)
        self.new_password_1_field.setObjectName(u"new_password_1_field")
        self.new_password_1_field.setMinimumSize(QSize(0, 25))
        self.new_password_1_field.setFont(font1)
        self.new_password_1_field.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.new_password_1_field)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.new_password_2_field = QLineEdit(self.widget_3)
        self.new_password_2_field.setObjectName(u"new_password_2_field")
        self.new_password_2_field.setMinimumSize(QSize(0, 25))
        self.new_password_2_field.setFont(font1)
        self.new_password_2_field.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.new_password_2_field)

        self.change_password_warning_label = QLabel(self.widget_3)
        self.change_password_warning_label.setObjectName(u"change_password_warning_label")
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setPointSize(10)
        self.change_password_warning_label.setFont(font3)
        self.change_password_warning_label.setStyleSheet(u"color: #FF605C;")
        self.change_password_warning_label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.change_password_warning_label)

        self.wrong_password_warning_label = QLabel(self.widget_3)
        self.wrong_password_warning_label.setObjectName(u"wrong_password_warning_label")
        self.wrong_password_warning_label.setFont(font3)
        self.wrong_password_warning_label.setStyleSheet(u"color: #FF605C;")
        self.wrong_password_warning_label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.wrong_password_warning_label)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.password_changed_label = QLabel(self.widget_4)
        self.password_changed_label.setObjectName(u"password_changed_label")
        self.password_changed_label.setFont(font3)
        self.password_changed_label.setStyleSheet(u"color: #00CA4E;")
        self.password_changed_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.password_changed_label)

        self.change_password_btn = QPushButton(self.widget_4)
        self.change_password_btn.setObjectName(u"change_password_btn")
        self.change_password_btn.setMinimumSize(QSize(100, 30))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.change_password_btn.setFont(font4)
        self.change_password_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_password_btn.setStyleSheet(u"#change_password_btn {	\n"
"	color: #222831;\n"
"	background-color: #F0CF90;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"#change_password_btn:pressed {\n"
"	background-color: #C3943C;\n"
"}")

        self.verticalLayout_11.addWidget(self.change_password_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.widget_4, 0, Qt.AlignBottom)


        self.verticalLayout_12.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.page.addWidget(self.account_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_15 = QVBoxLayout(self.home_page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 30, 0, 0)
        self.label_6 = QLabel(self.home_page)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(30)
        self.label_6.setFont(font5)

        self.verticalLayout_15.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)

        self.label_5 = QLabel(self.home_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(350, 350))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/logo.png"))
        self.label_5.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.page.addWidget(self.home_page)
        self.add_activity_page = QWidget()
        self.add_activity_page.setObjectName(u"add_activity_page")
        self.verticalLayout_16 = QVBoxLayout(self.add_activity_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_7 = QLabel(self.add_activity_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget = QStackedWidget(self.add_activity_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.select_file = QWidget()
        self.select_file.setObjectName(u"select_file")
        self.verticalLayout_17 = QVBoxLayout(self.select_file)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget = QWidget(self.select_file)
        self.widget.setObjectName(u"widget")
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.verticalLayout_18 = QVBoxLayout(self.widget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_3)

        self.select_activity_file_btn = QPushButton(self.widget)
        self.select_activity_file_btn.setObjectName(u"select_activity_file_btn")
        self.select_activity_file_btn.setMinimumSize(QSize(150, 40))
        self.select_activity_file_btn.setFont(font)
        self.select_activity_file_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_activity_file_btn.setStyleSheet(u"#select_activity_file_btn {	\n"
"	color: #222831;\n"
"	background-color: #F0CF90;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"#select_activity_file_btn:pressed {\n"
"	background-color: #C3943C;\n"
"}")

        self.verticalLayout_18.addWidget(self.select_activity_file_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.no_device_selected_label = QLabel(self.widget)
        self.no_device_selected_label.setObjectName(u"no_device_selected_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.no_device_selected_label.sizePolicy().hasHeightForWidth())
        self.no_device_selected_label.setSizePolicy(sizePolicy4)
        self.no_device_selected_label.setFont(font3)
        self.no_device_selected_label.setStyleSheet(u"color: #FF605C;")

        self.verticalLayout_18.addWidget(self.no_device_selected_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.error_while_loading_data_label = QLabel(self.widget)
        self.error_while_loading_data_label.setObjectName(u"error_while_loading_data_label")
        self.error_while_loading_data_label.setFont(font3)
        self.error_while_loading_data_label.setStyleSheet(u"color: #FF605C;")

        self.verticalLayout_18.addWidget(self.error_while_loading_data_label, 0, Qt.AlignHCenter)

        self.activity_added_label = QLabel(self.widget)
        self.activity_added_label.setObjectName(u"activity_added_label")
        self.activity_added_label.setFont(font3)
        self.activity_added_label.setStyleSheet(u"color: #00CA4E;")

        self.verticalLayout_18.addWidget(self.activity_added_label, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)


        self.verticalLayout_17.addWidget(self.widget)

        self.stackedWidget.addWidget(self.select_file)
        self.file_summary = QWidget()
        self.file_summary.setObjectName(u"file_summary")
        self.stackedWidget.addWidget(self.file_summary)

        self.verticalLayout_16.addWidget(self.stackedWidget)

        self.page.addWidget(self.add_activity_page)
        self.manage_devices_page = QWidget()
        self.manage_devices_page.setObjectName(u"manage_devices_page")
        self.verticalLayout_13 = QVBoxLayout(self.manage_devices_page)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.manage_devices_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QPushButton {	\n"
"	color: #222831;\n"
"	background-color: #F0CF90;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #C3943C;\n"
"}")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_10.setSpacing(70)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.add_device_btn = QPushButton(self.widget_5)
        self.add_device_btn.setObjectName(u"add_device_btn")
        self.add_device_btn.setMinimumSize(QSize(130, 30))
        self.add_device_btn.setFont(font1)
        self.add_device_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.add_device_btn)

        self.edit_device_table_btn = QPushButton(self.widget_5)
        self.edit_device_table_btn.setObjectName(u"edit_device_table_btn")
        self.edit_device_table_btn.setMinimumSize(QSize(130, 30))
        self.edit_device_table_btn.setFont(font1)
        self.edit_device_table_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.edit_device_table_btn)

        self.save_edited_table_btn = QPushButton(self.widget_5)
        self.save_edited_table_btn.setObjectName(u"save_edited_table_btn")
        self.save_edited_table_btn.setMinimumSize(QSize(130, 30))
        self.save_edited_table_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_edited_table_btn.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.save_edited_table_btn)

        self.delete_device_btn = QPushButton(self.widget_5)
        self.delete_device_btn.setObjectName(u"delete_device_btn")
        self.delete_device_btn.setMinimumSize(QSize(130, 30))
        self.delete_device_btn.setFont(font1)
        self.delete_device_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_device_btn.setStyleSheet(u"#delete_device_btn {\n"
"	background-color: #FF605C;\n"
"}\n"
"\n"
"#delete_device_btn:pressed {\n"
"	background-color: #B7221F;\n"
"}")

        self.horizontalLayout_10.addWidget(self.delete_device_btn)


        self.verticalLayout_13.addWidget(self.widget_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_6 = QWidget(self.manage_devices_page)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(70, 0, 70, -1)
        self.edit_devices_warning_label = QLabel(self.widget_6)
        self.edit_devices_warning_label.setObjectName(u"edit_devices_warning_label")
        self.edit_devices_warning_label.setFont(font3)
        self.edit_devices_warning_label.setStyleSheet(u"color: #FFAD14;")

        self.verticalLayout_14.addWidget(self.edit_devices_warning_label, 0, Qt.AlignHCenter)

        self.unsaved_changes_label = QLabel(self.widget_6)
        self.unsaved_changes_label.setObjectName(u"unsaved_changes_label")
        self.unsaved_changes_label.setFont(font3)
        self.unsaved_changes_label.setStyleSheet(u"color: #FF605C;")

        self.verticalLayout_14.addWidget(self.unsaved_changes_label, 0, Qt.AlignHCenter)

        self.search_device_field = QLineEdit(self.widget_6)
        self.search_device_field.setObjectName(u"search_device_field")
        self.search_device_field.setMinimumSize(QSize(800, 0))
        self.search_device_field.setMaximumSize(QSize(16777215, 16777215))
        self.search_device_field.setStyleSheet(u"border: 2px solid #40464F;\n"
"background-color: #40464F;\n"
"border-radius: 5px;\n"
"padding: 5px;")

        self.verticalLayout_14.addWidget(self.search_device_field)

        self.device_table = QTableWidget(self.widget_6)
        if (self.device_table.columnCount() < 6):
            self.device_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.device_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.device_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.device_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.device_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.device_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.device_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.device_table.rowCount() < 6):
            self.device_table.setRowCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.device_table.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.device_table.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.device_table.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.device_table.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.device_table.setItem(0, 4, __qtablewidgetitem10)
        self.device_table.setObjectName(u"device_table")
        self.device_table.setStyleSheet(u"QTableWidget {\n"
"	color: #EEE;\n"
"	border-radius: 5px;\n"
"    gridline-color: #555;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2E3642;\n"
"    padding: 4px;\n"
"	border: none;\n"
"    border-bottom: 2px solid #F0CF90;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: #2E3642;\n"
"	border: none;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #F0CF90; \n"
"	color: #222831;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 10px 0 10px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #F0CF90;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right"
                        ";\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"     background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 10px 0 10px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {	\n"
"	background: #F0CF90;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	 background: rgb(52, 59, 72);\n"
"     height: 20px;\n"
"	 border-bottom-left-radius: 4px;\n"
"     border-bottom-right-radi"
                        "us: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background: rgb(52, 59, 72);\n"
"    height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.device_table.setShowGrid(True)
        self.device_table.horizontalHeader().setDefaultSectionSize(130)
        self.device_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.device_table)


        self.verticalLayout_13.addWidget(self.widget_6)

        self.page.addWidget(self.manage_devices_page)
        self.activity_map_page = QWidget()
        self.activity_map_page.setObjectName(u"activity_map_page")
        self.textEdit_5 = QTextEdit(self.activity_map_page)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(230, 220, 104, 71))
        self.page.addWidget(self.activity_map_page)
        self.activities_page = QWidget()
        self.activities_page.setObjectName(u"activities_page")
        self.verticalLayout_19 = QVBoxLayout(self.activities_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.activities_header = QWidget(self.activities_page)
        self.activities_header.setObjectName(u"activities_header")
        self.verticalLayout_20 = QVBoxLayout(self.activities_header)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_8 = QLabel(self.activities_header)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.verticalLayout_20.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_19.addWidget(self.activities_header)

        self.activities_sub_pages = QStackedWidget(self.activities_page)
        self.activities_sub_pages.setObjectName(u"activities_sub_pages")
        self.select_activity_page = QWidget()
        self.select_activity_page.setObjectName(u"select_activity_page")
        self.select_activity_page.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.select_activity_page)
        self.verticalLayout_21.setSpacing(15)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.activities_list = QListWidget(self.select_activity_page)
        self.activities_list.setObjectName(u"activities_list")
        self.activities_list.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.activities_list.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.activities_list)

        self.activities_sub_pages.addWidget(self.select_activity_page)
        self.activity_details_page = QWidget()
        self.activity_details_page.setObjectName(u"activity_details_page")
        self.verticalLayout_22 = QVBoxLayout(self.activity_details_page)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(10, 0, 10, 0)
        self.widget_8 = QWidget(self.activity_details_page)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 20)
        self.back_to_activities_list_btn = QPushButton(self.widget_8)
        self.back_to_activities_list_btn.setObjectName(u"back_to_activities_list_btn")
        self.back_to_activities_list_btn.setMinimumSize(QSize(60, 30))
        self.back_to_activities_list_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_activities_list_btn.setStyleSheet(u"QPushButton#back_to_activities_list_btn {\n"
"	background-color: #F0CF90;\n"
"	color: black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#back_to_activities_list_btn:hover {\n"
"	background-color: #F3D8A5;\n"
"}\n"
"\n"
"QPushButton#back_to_activities_list_btn:pressed {\n"
"	background-color: #C3943C;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/flip-backward-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.back_to_activities_list_btn.setIcon(icon10)

        self.horizontalLayout_11.addWidget(self.back_to_activities_list_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.delete_activity_btn = QPushButton(self.widget_8)
        self.delete_activity_btn.setObjectName(u"delete_activity_btn")
        self.delete_activity_btn.setMinimumSize(QSize(100, 30))
        self.delete_activity_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_activity_btn.setStyleSheet(u"#delete_activity_btn {\n"
"	color: #222831;\n"
"	background-color: #FF605C;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"#delete_activity_btn:pressed {\n"
"	background-color: #B7221F;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/trash-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_activity_btn.setIcon(icon11)

        self.horizontalLayout_11.addWidget(self.delete_activity_btn)


        self.verticalLayout_22.addWidget(self.widget_8, 0, Qt.AlignTop)

        self.widget_9 = QWidget(self.activity_details_page)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy3.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy3)
        self.verticalLayout_23 = QVBoxLayout(self.widget_9)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 0, -1, -1)
        self.scrollArea = QScrollArea(self.widget_9)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 252, 1438))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_24.setSpacing(40)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 20, 0)
        self.activity_summary_table = QFrame(self.scrollAreaWidgetContents)
        self.activity_summary_table.setObjectName(u"activity_summary_table")
        self.activity_summary_table.setStyleSheet(u"#activity_summary_table {\n"
"	border: 2px solid #222831;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"* {\n"
"	background-color: #2E3642\n"
"}")
        self.verticalLayout_25 = QVBoxLayout(self.activity_summary_table)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(4, 4, 4, 4)
        self.top_row = QFrame(self.activity_summary_table)
        self.top_row.setObjectName(u"top_row")
        self.top_row.setStyleSheet(u"#top_row {\n"
"	border-bottom: 2px solid #222831;\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.top_row)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.top_row)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_26 = QVBoxLayout(self.widget_15)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 15, 0, 15)
        self.activity_time_label = QLabel(self.widget_15)
        self.activity_time_label.setObjectName(u"activity_time_label")
        font6 = QFont()
        font6.setPointSize(14)
        self.activity_time_label.setFont(font6)

        self.verticalLayout_26.addWidget(self.activity_time_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_10 = QLabel(self.widget_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_26.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_12.addWidget(self.widget_15)

        self.frame_16 = QFrame(self.top_row)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"#frame_16 {\n"
"	border-left: 2px solid #222831;\n"
"	border-right: 2px solid #222831;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.frame_16)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 15, 0, 15)
        self.avg_heart_rate_label = QLabel(self.frame_16)
        self.avg_heart_rate_label.setObjectName(u"avg_heart_rate_label")
        self.avg_heart_rate_label.setFont(font6)

        self.verticalLayout_27.addWidget(self.avg_heart_rate_label, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.frame_16)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_27.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_16)

        self.widget_17 = QWidget(self.top_row)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_28 = QVBoxLayout(self.widget_17)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 15, 0, 15)
        self.distance_label = QLabel(self.widget_17)
        self.distance_label.setObjectName(u"distance_label")
        self.distance_label.setFont(font6)

        self.verticalLayout_28.addWidget(self.distance_label, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.widget_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_28.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.widget_17)


        self.verticalLayout_25.addWidget(self.top_row)

        self.bottom_row = QWidget(self.activity_summary_table)
        self.bottom_row.setObjectName(u"bottom_row")
        self.horizontalLayout_13 = QHBoxLayout(self.bottom_row)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.bottom_row)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_29 = QVBoxLayout(self.widget_18)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 15, 0, 15)
        self.avg_pace_label = QLabel(self.widget_18)
        self.avg_pace_label.setObjectName(u"avg_pace_label")
        self.avg_pace_label.setFont(font6)

        self.verticalLayout_29.addWidget(self.avg_pace_label, 0, Qt.AlignHCenter)

        self.label_16 = QLabel(self.widget_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_29.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.widget_18)

        self.frame_19 = QFrame(self.bottom_row)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"#frame_19 {\n"
"	border-left: 2px solid #222831;\n"
"	border-right: 2px solid #222831;\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.frame_19)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 15, 0, 15)
        self.avg_speed_label = QLabel(self.frame_19)
        self.avg_speed_label.setObjectName(u"avg_speed_label")
        self.avg_speed_label.setFont(font6)

        self.verticalLayout_30.addWidget(self.avg_speed_label, 0, Qt.AlignHCenter)

        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_30.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.frame_19)

        self.widget_20 = QWidget(self.bottom_row)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_31 = QVBoxLayout(self.widget_20)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 15, 0, 15)
        self.max_speed_label = QLabel(self.widget_20)
        self.max_speed_label.setObjectName(u"max_speed_label")
        self.max_speed_label.setFont(font6)

        self.verticalLayout_31.addWidget(self.max_speed_label, 0, Qt.AlignHCenter)

        self.label_20 = QLabel(self.widget_20)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_31.addWidget(self.label_20, 0, Qt.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.widget_20)


        self.verticalLayout_25.addWidget(self.bottom_row)


        self.verticalLayout_24.addWidget(self.activity_summary_table)

        self.heart_rate_container = QFrame(self.scrollAreaWidgetContents)
        self.heart_rate_container.setObjectName(u"heart_rate_container")
        self.heart_rate_container.setMinimumSize(QSize(0, 600))
        self.heart_rate_container.setStyleSheet(u"#heart_rate_container {\n"
"	border: 2px solid transparent;\n"
"	border-radius: 15px;\n"
"}")
        self.verticalLayout_32 = QVBoxLayout(self.heart_rate_container)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.heart_rate_header = QWidget(self.heart_rate_container)
        self.heart_rate_header.setObjectName(u"heart_rate_header")
        self.heart_rate_header.setStyleSheet(u"#heart_rate_header {\n"
"	border-bottom: 2px solid #222831;\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.heart_rate_header)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, -1, -1, 9)
        self.label_21 = QLabel(self.heart_rate_header)
        self.label_21.setObjectName(u"label_21")
        font7 = QFont()
        font7.setPointSize(12)
        self.label_21.setFont(font7)

        self.verticalLayout_33.addWidget(self.label_21)


        self.verticalLayout_32.addWidget(self.heart_rate_header, 0, Qt.AlignTop)

        self.widget_11 = QWidget(self.heart_rate_container)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_34 = QVBoxLayout(self.widget_11)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, 0, 0, 0)
        self.label_22 = QLabel(self.widget_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_34.addWidget(self.label_22)

        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"#widget_13 {\n"
"	border-right: 2px solid #222831;\n"
"}")
        self.verticalLayout_35 = QVBoxLayout(self.widget_13)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.chart_avg_hr_label = QLabel(self.widget_13)
        self.chart_avg_hr_label.setObjectName(u"chart_avg_hr_label")
        self.chart_avg_hr_label.setFont(font7)

        self.verticalLayout_35.addWidget(self.chart_avg_hr_label, 0, Qt.AlignHCenter)

        self.label_23 = QLabel(self.widget_13)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_35.addWidget(self.label_23, 0, Qt.AlignHCenter)


        self.horizontalLayout_14.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_36 = QVBoxLayout(self.widget_14)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.chart_max_hr_label = QLabel(self.widget_14)
        self.chart_max_hr_label.setObjectName(u"chart_max_hr_label")
        self.chart_max_hr_label.setFont(font7)

        self.verticalLayout_36.addWidget(self.chart_max_hr_label, 0, Qt.AlignHCenter)

        self.label_24 = QLabel(self.widget_14)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_36.addWidget(self.label_24, 0, Qt.AlignHCenter)


        self.horizontalLayout_14.addWidget(self.widget_14)


        self.verticalLayout_34.addWidget(self.widget_12)


        self.verticalLayout_32.addWidget(self.widget_11)

        self.heart_rate_chart = QWidget(self.heart_rate_container)
        self.heart_rate_chart.setObjectName(u"heart_rate_chart")
        sizePolicy3.setHeightForWidth(self.heart_rate_chart.sizePolicy().hasHeightForWidth())
        self.heart_rate_chart.setSizePolicy(sizePolicy3)
        self.heart_rate_chart.setStyleSheet(u"")

        self.verticalLayout_32.addWidget(self.heart_rate_chart)


        self.verticalLayout_24.addWidget(self.heart_rate_container)

        self.map = QWidget(self.scrollAreaWidgetContents)
        self.map.setObjectName(u"map")
        self.map.setMinimumSize(QSize(0, 600))
        self.verticalLayout_37 = QVBoxLayout(self.map)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.route_map_header = QWidget(self.map)
        self.route_map_header.setObjectName(u"route_map_header")
        self.route_map_header.setStyleSheet(u"#route_map_header {\n"
"	border-bottom: 2px solid #222831;\n"
"}")
        self.verticalLayout_38 = QVBoxLayout(self.route_map_header)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_27 = QLabel(self.route_map_header)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font7)
        self.label_27.setStyleSheet(u"#route_map_header {\n"
"	border-bottom: 2px solid #222831;\n"
"}")

        self.verticalLayout_38.addWidget(self.label_27)


        self.verticalLayout_37.addWidget(self.route_map_header, 0, Qt.AlignTop)

        self.details_map_container = QWidget(self.map)
        self.details_map_container.setObjectName(u"details_map_container")
        sizePolicy3.setHeightForWidth(self.details_map_container.sizePolicy().hasHeightForWidth())
        self.details_map_container.setSizePolicy(sizePolicy3)
        self.verticalLayout_39 = QVBoxLayout(self.details_map_container)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 3, 0, 0)
        self.details_map = QQuickWidget(self.details_map_container)
        self.details_map.setObjectName(u"details_map")
        self.details_map.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.details_map.setSource(QUrl(u"file:///C:/Users/Konrad PC/Desktop/Studia/Praca/FitWrap/app/MapDisplay.qml"))

        self.verticalLayout_39.addWidget(self.details_map)


        self.verticalLayout_37.addWidget(self.details_map_container)


        self.verticalLayout_24.addWidget(self.map)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_23.addWidget(self.scrollArea)


        self.verticalLayout_22.addWidget(self.widget_9)

        self.activities_sub_pages.addWidget(self.activity_details_page)

        self.verticalLayout_19.addWidget(self.activities_sub_pages)

        self.page.addWidget(self.activities_page)
        self.compare_page = QWidget()
        self.compare_page.setObjectName(u"compare_page")
        self.compare_page.setStyleSheet(u"")
        self.verticalLayout_40 = QVBoxLayout(self.compare_page)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.widget_7 = QWidget(self.compare_page)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_41 = QVBoxLayout(self.widget_7)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.widget_16 = QWidget(self.widget_7)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"	background-color: #222831;\n"
"	border: 3px solid #F0CF90;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	border-radius: 6%; /* Zachowanie kszta\u0142tu k\u00f3\u0142ka */\n"
"	background-color: #EEE;\n"
"}")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_15.setSpacing(30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)

        self.heart_rate_radio_btn = QRadioButton(self.widget_16)
        self.heart_rate_radio_btn.setObjectName(u"heart_rate_radio_btn")
        self.heart_rate_radio_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.heart_rate_radio_btn.setChecked(True)

        self.horizontalLayout_15.addWidget(self.heart_rate_radio_btn)

        self.route_radio_btn = QRadioButton(self.widget_16)
        self.route_radio_btn.setObjectName(u"route_radio_btn")
        self.route_radio_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_15.addWidget(self.route_radio_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.verticalLayout_41.addWidget(self.widget_16, 0, Qt.AlignTop)

        self.widget_19 = QWidget(self.widget_7)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setStyleSheet(u"#widget_19::QComboBox * {\n"
"	background-color: #222831;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 2px solid transparent;\n"
"	border-radius: 5px;\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_16.setSpacing(100)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.activity_1_cbox = QComboBox(self.widget_19)
        self.activity_1_cbox.addItem("")
        self.activity_1_cbox.addItem("")
        self.activity_1_cbox.setObjectName(u"activity_1_cbox")
        self.activity_1_cbox.setMinimumSize(QSize(0, 40))
        self.activity_1_cbox.setMaximumSize(QSize(300, 16777215))
        self.activity_1_cbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.activity_1_cbox.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.activity_1_cbox)

        self.activity_2_cbox = QComboBox(self.widget_19)
        self.activity_2_cbox.addItem("")
        self.activity_2_cbox.addItem("")
        self.activity_2_cbox.setObjectName(u"activity_2_cbox")
        self.activity_2_cbox.setMinimumSize(QSize(0, 40))
        self.activity_2_cbox.setMaximumSize(QSize(300, 16777215))
        self.activity_2_cbox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.activity_2_cbox)


        self.verticalLayout_41.addWidget(self.widget_19)


        self.verticalLayout_40.addWidget(self.widget_7)

        self.widget_10 = QWidget(self.compare_page)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy3.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy3)
        self.verticalLayout_42 = QVBoxLayout(self.widget_10)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.compare_pages = QStackedWidget(self.widget_10)
        self.compare_pages.setObjectName(u"compare_pages")
        self.compare_heart_rate_page = QWidget()
        self.compare_heart_rate_page.setObjectName(u"compare_heart_rate_page")
        self.compare_pages.addWidget(self.compare_heart_rate_page)
        self.compare_route_page = QWidget()
        self.compare_route_page.setObjectName(u"compare_route_page")
        self.verticalLayout_43 = QVBoxLayout(self.compare_route_page)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.compare_route_map = QQuickWidget(self.compare_route_page)
        self.compare_route_map.setObjectName(u"compare_route_map")
        self.compare_route_map.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.compare_route_map.setSource(QUrl(u"file:///C:/Users/Konrad PC/Desktop/Studia/Praca/FitWrap/app/MapDisplay.qml"))

        self.verticalLayout_43.addWidget(self.compare_route_map)

        self.compare_pages.addWidget(self.compare_route_page)

        self.verticalLayout_42.addWidget(self.compare_pages)


        self.verticalLayout_40.addWidget(self.widget_10)

        self.page.addWidget(self.compare_page)
        self.faq_page = QWidget()
        self.faq_page.setObjectName(u"faq_page")
        self.textEdit_8 = QTextEdit(self.faq_page)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(220, 240, 104, 71))
        self.page.addWidget(self.faq_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.textEdit_2 = QTextEdit(self.settings_page)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(160, 140, 271, 211))
        self.page.addWidget(self.settings_page)

        self.verticalLayout_8.addWidget(self.page)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background-color: #2E3642;\n"
"border-bottom-right-radius: 7px;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, 1, 0, 1)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.author = QLabel(self.frame_4)
        self.author.setObjectName(u"author")
        self.author.setStyleSheet(u"color: #858585;")

        self.verticalLayout_3.addWidget(self.author, 0, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.footer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_2.addWidget(self.pushButton_7, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.page.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.activities_sub_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.add_activity_btn.setText(QCoreApplication.translate("MainWindow", u"Add activity", None))
        self.manage_devices_btn.setText(QCoreApplication.translate("MainWindow", u"Manage devices", None))
        self.activities_btn.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.map_btn.setText(QCoreApplication.translate("MainWindow", u"Activity map", None))
        self.compare_btn.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.faq_btn.setText(QCoreApplication.translate("MainWindow", u"FAQ", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.notifications_btn.setText("")
        self.account_btn.setText("")
        self.selected_device_cbox.setItemText(0, QCoreApplication.translate("MainWindow", u"Huawei GT3 Pro", None))
        self.selected_device_cbox.setItemText(1, QCoreApplication.translate("MainWindow", u"Samsung Watch 6", None))
        self.selected_device_cbox.setItemText(2, QCoreApplication.translate("MainWindow", u"Garmin Forerunner", None))

        self.selected_device_cbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select device", None))
        self.show_side_menu_button.setText("")
        self.minimize_window_button.setText("")
        self.maximize_window_button.setText("")
        self.close_window_button.setText("")
        self.log_out_btn.setText(QCoreApplication.translate("MainWindow", u"  Log out   ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Change password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current password:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"New password:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confirm password:", None))
        self.change_password_warning_label.setText(QCoreApplication.translate("MainWindow", u"Password change warning placeholder.", None))
        self.wrong_password_warning_label.setText(QCoreApplication.translate("MainWindow", u"Wrong password.", None))
        self.password_changed_label.setText(QCoreApplication.translate("MainWindow", u"Password changed.", None))
        self.change_password_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
#if QT_CONFIG(whatsthis)
        self.home_page.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Home page", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Add activity", None))
        self.select_activity_file_btn.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.no_device_selected_label.setText(QCoreApplication.translate("MainWindow", u"No device selected", None))
        self.error_while_loading_data_label.setText(QCoreApplication.translate("MainWindow", u"An error occurred while loading data ", None))
        self.activity_added_label.setText(QCoreApplication.translate("MainWindow", u"Activity added", None))
        self.add_device_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.edit_device_table_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.save_edited_table_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.delete_device_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.edit_devices_warning_label.setText(QCoreApplication.translate("MainWindow", u"Editing enabled.", None))
        self.unsaved_changes_label.setText(QCoreApplication.translate("MainWindow", u"Changes made to the table have not been saved.", None))
        self.search_device_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for device", None))
        ___qtablewidgetitem = self.device_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Device icon", None));
        ___qtablewidgetitem1 = self.device_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Brand", None));
        ___qtablewidgetitem2 = self.device_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Model", None));
        ___qtablewidgetitem3 = self.device_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem4 = self.device_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Last update", None));
        ___qtablewidgetitem5 = self.device_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"No. of activities", None));

        __sortingEnabled = self.device_table.isSortingEnabled()
        self.device_table.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.device_table.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"dd", None));
        ___qtablewidgetitem7 = self.device_table.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"wdqd", None));
        ___qtablewidgetitem8 = self.device_table.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"qdqd", None));
        ___qtablewidgetitem9 = self.device_table.item(0, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"qd", None));
        self.device_table.setSortingEnabled(__sortingEnabled)

        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Activity map</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.back_to_activities_list_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.delete_activity_btn.setText(QCoreApplication.translate("MainWindow", u"Delete activity", None))
        self.activity_time_label.setText(QCoreApplication.translate("MainWindow", u"01:40:34", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Activity time", None))
        self.avg_heart_rate_label.setText(QCoreApplication.translate("MainWindow", u"114", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Avg heart rate", None))
        self.distance_label.setText(QCoreApplication.translate("MainWindow", u"20.90 km", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.avg_pace_label.setText(QCoreApplication.translate("MainWindow", u"135", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Avg pace", None))
        self.avg_speed_label.setText(QCoreApplication.translate("MainWindow", u"12.29", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Avg speed", None))
        self.max_speed_label.setText(QCoreApplication.translate("MainWindow", u"31.30", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Max speed", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Heart rate", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"(bpm)", None))
        self.chart_avg_hr_label.setText(QCoreApplication.translate("MainWindow", u"114", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Avg", None))
        self.chart_max_hr_label.setText(QCoreApplication.translate("MainWindow", u"166", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Route map", None))
        self.heart_rate_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Heart rate", None))
        self.route_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Route", None))
        self.activity_1_cbox.setItemText(0, QCoreApplication.translate("MainWindow", u"test", None))
        self.activity_1_cbox.setItemText(1, QCoreApplication.translate("MainWindow", u"test", None))

        self.activity_1_cbox.setCurrentText("")
        self.activity_1_cbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select activity", None))
        self.activity_2_cbox.setItemText(0, QCoreApplication.translate("MainWindow", u"test", None))
        self.activity_2_cbox.setItemText(1, QCoreApplication.translate("MainWindow", u"test", None))

        self.activity_2_cbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select activity", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FAQ</p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Settings page</span></p></body></html>", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"By: Konrad Janiszewski", None))
        self.pushButton_7.setText("")
    # retranslateUi

