# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activity_item_widgetcxTGmJ.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources.icons_rc

class Ui_ActivityWidget(object):
    def setupUi(self, ActivityWidget):
        if not ActivityWidget.objectName():
            ActivityWidget.setObjectName(u"ActivityWidget")
        ActivityWidget.resize(900, 100)
        ActivityWidget.setMinimumSize(QSize(900, 100))
        ActivityWidget.setCursor(QCursor(Qt.PointingHandCursor))
        ActivityWidget.setStyleSheet(u"#ActivityWidget * {\n"
"	border: none;\n"
"	background-color: #2C343F;\n"
"	color: #EEEEEE;\n"
"}\n"
"\n"
"#ActivityWidget {\n"
"	\n"
"}")
        self.verticalLayout = QVBoxLayout(ActivityWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, -1, 3)
        self.date_container = QWidget(ActivityWidget)
        self.date_container.setObjectName(u"date_container")
        font = QFont()
        font.setPointSize(10)
        self.date_container.setFont(font)
        self.date_container.setStyleSheet(u"#date_container {\n"
"	border-bottom: 2px solid #393E46;\n"
"	border-top: 3px solid transparent;\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.date_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 2, 0)
        self.activity_date_label = QLabel(self.date_container)
        self.activity_date_label.setObjectName(u"activity_date_label")
        font1 = QFont()
        font1.setPointSize(11)
        self.activity_date_label.setFont(font1)

        self.horizontalLayout.addWidget(self.activity_date_label, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.date_container)

        self.widget_2 = QWidget(ActivityWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
"	border-bottom: 3px solid transparent;\n"
"	border-bottom-left-radius: 12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(50, 50))
        self.widget_3.setMaximumSize(QSize(50, 50))
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.activity_icon = QLabel(self.widget_3)
        self.activity_icon.setObjectName(u"activity_icon")
        self.activity_icon.setMinimumSize(QSize(50, 50))
        self.activity_icon.setPixmap(QPixmap(u":/icons/icons/default-activity-icon.png"))
        self.activity_icon.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.activity_icon, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignLeft)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 25))
        self.widget_5.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.activity_name_label = QLabel(self.widget_7)
        self.activity_name_label.setObjectName(u"activity_name_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.activity_name_label.sizePolicy().hasHeightForWidth())
        self.activity_name_label.setSizePolicy(sizePolicy1)
        self.activity_name_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.activity_name_label)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.activity_start_time_label = QLabel(self.widget_8)
        self.activity_start_time_label.setObjectName(u"activity_start_time_label")
        self.activity_start_time_label.setFont(font1)
        self.activity_start_time_label.setStyleSheet(u"color: #BBB;")

        self.verticalLayout_4.addWidget(self.activity_start_time_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.widget_8, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.info_container = QWidget(self.widget_4)
        self.info_container.setObjectName(u"info_container")
        self.info_container.setMinimumSize(QSize(0, 30))
        self.info_container.setMaximumSize(QSize(16777215, 30))
        self.info_container.setStyleSheet(u"color: #BBB;")
        self.horizontalLayout_5 = QHBoxLayout(self.info_container)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.duration = QPushButton(self.info_container)
        self.duration.setObjectName(u"duration")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.duration.sizePolicy().hasHeightForWidth())
        self.duration.setSizePolicy(sizePolicy2)
        self.duration.setMinimumSize(QSize(80, 0))
        icon = QIcon()
        icon.addFile(u":/icons/icons/clock-three-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.duration.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.duration, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.avg_speed = QPushButton(self.info_container)
        self.avg_speed.setObjectName(u"avg_speed")
        self.avg_speed.setMinimumSize(QSize(100, 0))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/clock-lines-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.avg_speed.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.avg_speed, 0, Qt.AlignVCenter)

        self.distance = QPushButton(self.info_container)
        self.distance.setObjectName(u"distance")
        self.distance.setMinimumSize(QSize(100, 0))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/road-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.distance.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.distance, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.info_container)


        self.horizontalLayout_2.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(ActivityWidget)

        QMetaObject.connectSlotsByName(ActivityWidget)
    # setupUi

    def retranslateUi(self, ActivityWidget):
        ActivityWidget.setWindowTitle(QCoreApplication.translate("ActivityWidget", u"Form", None))
        self.activity_date_label.setText(QCoreApplication.translate("ActivityWidget", u"18.01.2021", None))
        self.activity_icon.setText("")
        self.activity_name_label.setText(QCoreApplication.translate("ActivityWidget", u"Bieganie", None))
        self.activity_start_time_label.setText(QCoreApplication.translate("ActivityWidget", u"16:16", None))
        self.duration.setText(QCoreApplication.translate("ActivityWidget", u"00:00:00", None))
        self.avg_speed.setText(QCoreApplication.translate("ActivityWidget", u"100,00", None))
        self.distance.setText(QCoreApplication.translate("ActivityWidget", u"22.22km", None))
    # retranslateUi

