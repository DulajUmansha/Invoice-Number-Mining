# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QWidget)
# import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1186, 716)
        icon = QIcon()
        icon.addFile(u":/icon/resource/icon/receipt.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: rgb(66, 66, 66);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 10px 5px 5px 5px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 5px;\n"
"	font-size:20px;\n"
"	text-align:left;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"	border-radius: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar:vertical{\n"
"    width:8px; \n"
"    border-style:flat;\n"
"    border-radius: 4px;\n"
"    border:0px;\n"
"     background: #19191A;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"    background: rgba(255,255,255,0.50);\n"
"    border-radius: 4px;\n"
"    width:8px;\n"
"    min-height:91px;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::handle:vertical"
                        "::hover{\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius: 4px;\n"
"    width:8px;\n"
"}\n"
"QScrollBar::handle:vertical::pressed{\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius:4px;\n"
"    width:8px;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
"    background: #19191A;\n"
"border-style:flat;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
"   background: #19191A;\n"
"border-style:flat;\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"   background: #19191A;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   background: #19191A;\n"
"}\n"
"QScrollBar:horizontal{\n"
"    height:8px; \n"
"    border-style:flat;\n"
"    border-radius: 4px;\n"
"    border:0px;\n"
"background: #19191A;\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"    background: rgba(255,255,255,0.50);\n"
"    border-radius: 4px;\n"
"    height:8px;\n"
"    min-width:91px;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::handle:horizontal::hover{\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius: 4px;\n"
""
                        "    height:8px;\n"
"}\n"
"QScrollBar::handle:horizontal::pressed{\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius:4px;\n"
"    height:8px;\n"
"}\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: #19191A;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::add-page:horizontal {\n"
"   background: #19191A;\n"
"    border-style:flat;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   background: #19191A;\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"   background: #19191A;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 10px;\n"
"	background-color: rgba(255, 255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox:editable:on {\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
""
                        "	border-radius: 10px; /* same radius as the QComboBox */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    border-left-style: solid; /* just a single line */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/resource/icon/chevron-down.svg);\n"
"	right: 10px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on{\n"
"	top: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"	background-color: rgba(255, 255, 255, 200);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QDoubleSpinBox::up-arrow{\n"
"	image: url(:/icons/resource/icon/chevron-up.svg);\n"
"}\n"
"QDoubleSpinBox::down-arrow{\n"
"	image: url(:/icons/resource/icon/chevron-down.svg);\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"	border: solid;\n"
"}\n"
"QDoubleSpinBox::down-button {\n"
"	border: solid;\n"
"}\n"
"\n"
"QDateTimeEdit::up-arrow{\n"
"	image: url(:/icons/resource/icon/chevron-up.svg);\n"
"}\n"
"QDateTimeEdit::down-arrow{\n"
"	image: url(:/icons/resource/icon/chevron-down.svg);\n"
"}\n"
"QDateTimeEdit::up-button {\n"
"	border: solid;\n"
"}\n"
""
                        "QDateTimeEdit::down-button {\n"
"	border: solid;\n"
"}\n"
"QTableView{\n"
"	background-color: rgba(0,0,0,50);\n"
"	color: rgb(255, 255, 255);\n"
"	font-size:22px;\n"
"}\n"
"QTableView::item\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgba(0,0,0,150);\n"
"    text-align:center;\n"
"}\n"
"QTableView::item:hover\n"
"{\n"
"    color:#FFFFFF;\n"
"    background: #4B4B4D;\n"
"}\n"
"QTableView::item:selected\n"
"{\n"
"    color:#FFFFFF;\n"
"    background: #4B4B4D;\n"
"}\n"
"\n"
"QHeaderView{\n"
"	background-color: rgba(0,0,0,70);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section,QTableCornerButton:section\n"
"{\n"
"	font-size:18px;\n"
"    text-align:center;\n"
"    padding:3px;\n"
"    margin:0px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(2,2,50,200);\n"
"    border:1px solid #242424;\n"
"	border-radius: 8px;\n"
"}\n"
"QHeaderView::section:selected\n"
"{\n"
"    color:#FFFFFF;\n"
"    border:1px solid #242424;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 0)
        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setStyleSheet(u"background-color: rgb(24, 30, 54);")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_left)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(20)
        self.btn_training = QPushButton(self.frame_left)
        self.btn_training.setObjectName(u"btn_training")
        font = QFont()
        font.setFamilies([u"Inter UI"])
        font.setBold(True)
        self.btn_training.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icon/resource/icon/train.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_training.setIcon(icon1)
        self.btn_training.setIconSize(QSize(60, 60))

        self.gridLayout_3.addWidget(self.btn_training, 5, 0, 1, 1)

        self.btn_account = QPushButton(self.frame_left)
        self.btn_account.setObjectName(u"btn_account")
        self.btn_account.setMinimumSize(QSize(50, 100))
        self.btn_account.setStyleSheet(u"QPushButton{\n"
"	border-radius:25px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/resource/icon/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_account.setIcon(icon2)
        self.btn_account.setIconSize(QSize(150, 150))

        self.gridLayout_3.addWidget(self.btn_account, 0, 0, 1, 1, Qt.AlignTop)

        self.label_3 = QLabel(self.frame_left)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1, Qt.AlignHCenter)

        self.btn_extract = QPushButton(self.frame_left)
        self.btn_extract.setObjectName(u"btn_extract")
        self.btn_extract.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icon/resource/icon/extract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_extract.setIcon(icon3)
        self.btn_extract.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btn_extract, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.btn_collect = QPushButton(self.frame_left)
        self.btn_collect.setObjectName(u"btn_collect")
        self.btn_collect.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icon/resource/icon/data-collection.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_collect.setIcon(icon4)
        self.btn_collect.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.btn_collect, 6, 0, 1, 1)

        self.btn_dashboard = QPushButton(self.frame_left)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icon/resource/icon/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dashboard.setIcon(icon5)
        self.btn_dashboard.setIconSize(QSize(30, 30))
        self.btn_dashboard.setAutoDefault(False)
        self.btn_dashboard.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_dashboard, 3, 0, 1, 1)

        self.btn_setting = QPushButton(self.frame_left)
        self.btn_setting.setObjectName(u"btn_setting")
        font2 = QFont()
        font2.setFamilies([u"Inter UI"])
        self.btn_setting.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/icon/resource/icon/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon6)
        self.btn_setting.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.btn_setting, 8, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_left, 0, 0, 1, 1)

        self.frame_bottom = QFrame(self.frame_main)
        self.frame_bottom.setObjectName(u"frame_bottom")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_bottom.sizePolicy().hasHeightForWidth())
        self.frame_bottom.setSizePolicy(sizePolicy)
        self.frame_bottom.setMaximumSize(QSize(16777215, 16777215))
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_bottom)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_bottom)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_bottom, 1, 0, 1, 2)

        self.stackedWidget = QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMinimumSize(QSize(979, 679))
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(87, 84, 111);")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.gridLayout_5 = QGridLayout(self.page_dashboard)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.page_dashboard)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(28)
        self.label_2.setFont(font3)

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame = QFrame(self.page_dashboard)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(66, 66, 66);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.label_5.setFont(font4)

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.trained_value = QLabel(self.frame_9)
        self.trained_value.setObjectName(u"trained_value")
        font5 = QFont()
        font5.setPointSize(20)
        self.trained_value.setFont(font5)

        self.gridLayout_10.addWidget(self.trained_value, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_10.addWidget(self.label_9, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)


        self.gridLayout_11.addWidget(self.frame_9, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_4, 0, 1, 2, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(66, 66, 66);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_10)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.speed_value = QLabel(self.frame_10)
        self.speed_value.setObjectName(u"speed_value")
        self.speed_value.setFont(font5)

        self.gridLayout_13.addWidget(self.speed_value, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_13.addWidget(self.label_10, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)


        self.gridLayout_12.addWidget(self.frame_10, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.frame_5, 2, 1, 1, 1)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(66, 66, 66);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_11, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_6, 3, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(66, 66, 66);\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_14)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.gridLayout_18.addWidget(self.label_13, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_Memory = QFrame(self.frame_14)
        self.frame_Memory.setObjectName(u"frame_Memory")
        sizePolicy1.setHeightForWidth(self.frame_Memory.sizePolicy().hasHeightForWidth())
        self.frame_Memory.setSizePolicy(sizePolicy1)
        self.frame_Memory.setFrameShape(QFrame.StyledPanel)
        self.frame_Memory.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_Memory)
        self.gridLayout_19.setObjectName(u"gridLayout_19")

        self.gridLayout_18.addWidget(self.frame_Memory, 1, 0, 1, 1)


        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.frame_14)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(66, 66, 66);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.gridLayout_16.addWidget(self.label_12, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_CPU = QFrame(self.frame_7)
        self.frame_CPU.setObjectName(u"frame_CPU")
        sizePolicy1.setHeightForWidth(self.frame_CPU.sizePolicy().hasHeightForWidth())
        self.frame_CPU.setSizePolicy(sizePolicy1)
        self.frame_CPU.setFrameShape(QFrame.StyledPanel)
        self.frame_CPU.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_CPU)
        self.gridLayout_17.setObjectName(u"gridLayout_17")

        self.gridLayout_16.addWidget(self.frame_CPU, 1, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.frame_7)


        self.gridLayout_6.addLayout(self.formLayout, 0, 2, 4, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(66, 66, 66);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_8)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.accuracy_value = QLabel(self.frame_8)
        self.accuracy_value.setObjectName(u"accuracy_value")
        font6 = QFont()
        font6.setPointSize(25)
        self.accuracy_value.setFont(font6)

        self.gridLayout_14.addWidget(self.accuracy_value, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_9.addWidget(self.frame_8, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_3, 2, 0, 2, 1)

        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(66, 66, 66);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.greetings = QLabel(self.frame_12)
        self.greetings.setObjectName(u"greetings")
        self.greetings.setFont(font5)

        self.gridLayout_8.addWidget(self.greetings, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.frame_12, 0, 0, 2, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_extract = QWidget()
        self.page_extract.setObjectName(u"page_extract")
        self.stackedWidget.addWidget(self.page_extract)
        self.page_training = QWidget()
        self.page_training.setObjectName(u"page_training")
        self.stackedWidget.addWidget(self.page_training)
        self.page_collect = QWidget()
        self.page_collect.setObjectName(u"page_collect")
        self.gridLayout_15 = QGridLayout(self.page_collect)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.lineEdit_invoNumber = QLineEdit(self.page_collect)
        self.lineEdit_invoNumber.setObjectName(u"lineEdit_invoNumber")
        self.lineEdit_invoNumber.setMinimumSize(QSize(300, 40))
        font7 = QFont()
        font7.setPointSize(12)
        self.lineEdit_invoNumber.setFont(font7)
        self.lineEdit_invoNumber.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_invoNumber.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.lineEdit_invoNumber, 5, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.invoDataCollectBtn = QPushButton(self.page_collect)
        self.invoDataCollectBtn.setObjectName(u"invoDataCollectBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icon/resource/icon/right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.invoDataCollectBtn.setIcon(icon7)
        self.invoDataCollectBtn.setIconSize(QSize(50, 50))

        self.gridLayout_15.addWidget(self.invoDataCollectBtn, 1, 1, 1, 1)

        self.label_8 = QLabel(self.page_collect)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout_15.addWidget(self.label_8, 0, 0, 1, 1)

        self.frame_image_preview = QFrame(self.page_collect)
        self.frame_image_preview.setObjectName(u"frame_image_preview")
        sizePolicy1.setHeightForWidth(self.frame_image_preview.sizePolicy().hasHeightForWidth())
        self.frame_image_preview.setSizePolicy(sizePolicy1)
        self.frame_image_preview.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.frame_image_preview.setFrameShape(QFrame.StyledPanel)
        self.frame_image_preview.setFrameShadow(QFrame.Raised)

        self.gridLayout_15.addWidget(self.frame_image_preview, 1, 0, 1, 1)

        self.image_preview_clearBtn = QPushButton(self.page_collect)
        self.image_preview_clearBtn.setObjectName(u"image_preview_clearBtn")
        self.image_preview_clearBtn.setStyleSheet(u"background-color: rgb(255, 82, 82);")

        self.gridLayout_15.addWidget(self.image_preview_clearBtn, 8, 0, 1, 2, Qt.AlignLeft)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_preview_list_clearAllBtn = QPushButton(self.page_collect)
        self.image_preview_list_clearAllBtn.setObjectName(u"image_preview_list_clearAllBtn")
        self.image_preview_list_clearAllBtn.setStyleSheet(u"background-color: rgb(255, 82, 82);")

        self.horizontalLayout.addWidget(self.image_preview_list_clearAllBtn, 0, Qt.AlignHCenter)

        self.invoDataSubmitBtn = QPushButton(self.page_collect)
        self.invoDataSubmitBtn.setObjectName(u"invoDataSubmitBtn")
        self.invoDataSubmitBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icon/resource/icon/submit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.invoDataSubmitBtn.setIcon(icon8)
        self.invoDataSubmitBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.invoDataSubmitBtn, 0, Qt.AlignHCenter)


        self.gridLayout_15.addLayout(self.horizontalLayout, 8, 2, 1, 1)

        self.listWidget__image_preview = QListWidget(self.page_collect)
        self.listWidget__image_preview.setObjectName(u"listWidget__image_preview")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget__image_preview.sizePolicy().hasHeightForWidth())
        self.listWidget__image_preview.setSizePolicy(sizePolicy2)
        self.listWidget__image_preview.setFont(font7)
        self.listWidget__image_preview.setAutoFillBackground(False)
        self.listWidget__image_preview.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.listWidget__image_preview.setLineWidth(1)
        self.listWidget__image_preview.setMidLineWidth(10)
        self.listWidget__image_preview.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget__image_preview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listWidget__image_preview.setIconSize(QSize(100, 100))
        self.listWidget__image_preview.setResizeMode(QListView.Adjust)
        self.listWidget__image_preview.setSpacing(20)
        self.listWidget__image_preview.setViewMode(QListView.IconMode)
        self.listWidget__image_preview.setItemAlignment(Qt.AlignAbsolute|Qt.AlignCenter|Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.listWidget__image_preview, 0, 2, 8, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.label_11 = QLabel(self.page_collect)
        self.label_11.setObjectName(u"label_11")
        font8 = QFont()
        font8.setPointSize(14)
        self.label_11.setFont(font8)

        self.gridLayout_15.addWidget(self.label_11, 3, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_collect)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.stackedWidget.addWidget(self.page_settings)
        self.page_account = QWidget()
        self.page_account.setObjectName(u"page_account")
        self.stackedWidget.addWidget(self.page_account)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.image_preview_list_clearAllBtn.clicked["bool"].connect(self.listWidget__image_preview.clear)
        self.image_preview_clearBtn.clicked["bool"].connect(self.lineEdit_invoNumber.clear)
        self.lineEdit_invoNumber.returnPressed.connect(self.invoDataCollectBtn.click)

        self.btn_dashboard.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Invoice Number Extractor", None))
        self.btn_training.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.btn_account.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dulaj Umansha", None))
        self.btn_extract.setText(QCoreApplication.translate("MainWindow", u"  Extract", None))
        self.btn_collect.setText(QCoreApplication.translate("MainWindow", u"  Collect", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.btn_setting.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u" This is a Research project and  can make mistakes. Consider checking important information.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Trained", None))
        self.trained_value.setText(QCoreApplication.translate("MainWindow", u"2000", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Invoices", None))
        self.speed_value.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"minute per Invoice", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Avg Speed", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MEMORY", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.accuracy_value.setText(QCoreApplication.translate("MainWindow", u"78%", None))
        self.greetings.setText(QCoreApplication.translate("MainWindow", u"Good Morning", None))
        self.invoDataCollectBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Collect Invoices", None))
        self.image_preview_clearBtn.setText(QCoreApplication.translate("MainWindow", u"  Clear  ", None))
        self.image_preview_list_clearAllBtn.setText(QCoreApplication.translate("MainWindow", u"  Clear All  ", None))
        self.invoDataSubmitBtn.setText(QCoreApplication.translate("MainWindow", u"  Submit  ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Invoice Number", None))
    # retranslateUi

