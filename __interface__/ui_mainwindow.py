# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)
# import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1203, 716)
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
"	padding: 15px 5px 5px 5px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 5px;\n"
"	font-size:20px;\n"
"	text-align:left;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
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
"QScrollBar::handle:vertical::hover{\n"
"    background: rgba(255,255,255,0.90);\n"
"    border-radius: 4px;\n"
"    width:8px;\n"
"}\n"
"Q"
                        "ScrollBar::handle:vertical::pressed{\n"
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
"    height:8px;\n"
"}\n"
"QScrollBar::handle:horizontal::pressed{\n"
"    background: rgba(255,255,255,0.90);\n"
""
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
"	border-radius: 10px; /* same radius as the QComboBox */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-po"
                        "sition: top right;\n"
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
"QDateTimeEdit::down-button {\n"
"	border: solid;\n"
"}\n"
"QTableView{\n"
"	background-color: rgba(0,0,0,50);\n"
""
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
"QHeaderView::section,QTableCornerButton::section\n"
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
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 1)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 0)
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

        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(24, 30, 54);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(138, 65, 254, 50);\n"
"}\n"
"QProgressBar{\n"
"	background-color: rgb(24, 30, 54);\n"
"}")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_left)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_collect = QPushButton(self.frame_left)
        self.btn_collect.setObjectName(u"btn_collect")
        font = QFont()
        font.setFamilies([u"Inter Variable Text"])
        font.setBold(True)
        self.btn_collect.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icon/resource/icon/data-collection.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_collect.setIcon(icon1)
        self.btn_collect.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.btn_collect)

        self.progressBar_collcet = QProgressBar(self.frame_left)
        self.progressBar_collcet.setObjectName(u"progressBar_collcet")
        font1 = QFont()
        font1.setPointSize(1)
        font1.setBold(False)
        self.progressBar_collcet.setFont(font1)
        self.progressBar_collcet.setAutoFillBackground(False)
        self.progressBar_collcet.setValue(0)
        self.progressBar_collcet.setTextVisible(False)
        self.progressBar_collcet.setOrientation(Qt.Horizontal)
        self.progressBar_collcet.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar_collcet)


        self.gridLayout_3.addLayout(self.verticalLayout, 6, 0, 1, 2)

        self.label_3 = QLabel(self.frame_left)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Inter Variable Text"])
        font2.setPointSize(10)
        self.label_3.setFont(font2)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 2, Qt.AlignHCenter)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_dashboard = QPushButton(self.frame_left)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icon/resource/icon/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dashboard.setIcon(icon2)
        self.btn_dashboard.setIconSize(QSize(30, 30))
        self.btn_dashboard.setAutoDefault(False)
        self.btn_dashboard.setFlat(False)

        self.verticalLayout_4.addWidget(self.btn_dashboard)

        self.progressBar_dashboard = QProgressBar(self.frame_left)
        self.progressBar_dashboard.setObjectName(u"progressBar_dashboard")
        self.progressBar_dashboard.setFont(font1)
        self.progressBar_dashboard.setAutoFillBackground(False)
        self.progressBar_dashboard.setValue(0)
        self.progressBar_dashboard.setTextVisible(False)
        self.progressBar_dashboard.setOrientation(Qt.Horizontal)
        self.progressBar_dashboard.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_4.addWidget(self.progressBar_dashboard)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 3, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_extract = QPushButton(self.frame_left)
        self.btn_extract.setObjectName(u"btn_extract")
        self.btn_extract.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icon/resource/icon/extract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_extract.setIcon(icon3)
        self.btn_extract.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.btn_extract)

        self.progressBar_extract = QProgressBar(self.frame_left)
        self.progressBar_extract.setObjectName(u"progressBar_extract")
        self.progressBar_extract.setFont(font1)
        self.progressBar_extract.setAutoFillBackground(False)
        self.progressBar_extract.setValue(0)
        self.progressBar_extract.setTextVisible(False)
        self.progressBar_extract.setOrientation(Qt.Horizontal)
        self.progressBar_extract.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_3.addWidget(self.progressBar_extract)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 4, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 7, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_training = QPushButton(self.frame_left)
        self.btn_training.setObjectName(u"btn_training")
        self.btn_training.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icon/resource/icon/train.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_training.setIcon(icon4)
        self.btn_training.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.btn_training)

        self.progressBar_train = QProgressBar(self.frame_left)
        self.progressBar_train.setObjectName(u"progressBar_train")
        self.progressBar_train.setFont(font1)
        self.progressBar_train.setAutoFillBackground(False)
        self.progressBar_train.setValue(0)
        self.progressBar_train.setTextVisible(False)
        self.progressBar_train.setOrientation(Qt.Horizontal)
        self.progressBar_train.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_2.addWidget(self.progressBar_train)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 5, 0, 1, 2)

        self.btn_account = QPushButton(self.frame_left)
        self.btn_account.setObjectName(u"btn_account")
        self.btn_account.setMinimumSize(QSize(50, 100))
        self.btn_account.setStyleSheet(u"QPushButton{\n"
"	border-radius:25px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/resource/icon/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_account.setIcon(icon5)
        self.btn_account.setIconSize(QSize(150, 150))

        self.gridLayout_3.addWidget(self.btn_account, 0, 0, 1, 2)

        self.btn_setting = QPushButton(self.frame_left)
        self.btn_setting.setObjectName(u"btn_setting")
        font3 = QFont()
        font3.setFamilies([u"Inter UI"])
        self.btn_setting.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/icon/resource/icon/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon6)
        self.btn_setting.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.btn_setting, 8, 0, 1, 2, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_left, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMinimumSize(QSize(979, 679))
        self.stackedWidget.setFont(font3)
        self.stackedWidget.setStyleSheet(u"#page_ocrLibrary, \n"
"#page_account,\n"
"#page_collect,\n"
"#page_dashboard,\n"
"#page_extract,\n"
"#page_settings,\n"
"#page_training,\n"
"#page_extractHistory{\n"
"	background-color: rgb(87, 84, 111);\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:center;\n"
"	padding:10;\n"
"	background-color: rgba(0, 0, 0, 150);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding:10;\n"
"	text-align:center;\n"
"	background-color: rgba(0, 0, 0, 200);\n"
"}")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.gridLayout_5 = QGridLayout(self.page_dashboard)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.page_dashboard)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Inter Variable Text"])
        font4.setPointSize(28)
        self.label_2.setFont(font4)

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignLeft)

        self.frame = QFrame(self.page_dashboard)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
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
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_5.setFont(font5)

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
        font6 = QFont()
        font6.setPointSize(20)
        self.trained_value.setFont(font6)

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
        self.speed_value.setFont(font6)

        self.gridLayout_13.addWidget(self.speed_value, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_13.addWidget(self.label_10, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)


        self.gridLayout_12.addWidget(self.frame_10, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)

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
        self.label_7.setFont(font5)

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
        self.label_13.setFont(font5)

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
        self.label_12.setFont(font5)

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
        self.label_4.setFont(font5)

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
        font7 = QFont()
        font7.setPointSize(25)
        self.accuracy_value.setFont(font7)

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
        self.greetings.setFont(font6)

        self.gridLayout_8.addWidget(self.greetings, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.frame_12, 0, 0, 2, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_extract = QWidget()
        self.page_extract.setObjectName(u"page_extract")
        self.gridLayout_24 = QGridLayout(self.page_extract)
        self.gridLayout_24.setSpacing(25)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(25, 25, 25, 25)
        self.label_20 = QLabel(self.page_extract)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setFont(font4)

        self.gridLayout_24.addWidget(self.label_20, 0, 0, 1, 2, Qt.AlignLeft)

        self.frame_extractInvoice = QFrame(self.page_extract)
        self.frame_extractInvoice.setObjectName(u"frame_extractInvoice")
        sizePolicy1.setHeightForWidth(self.frame_extractInvoice.sizePolicy().hasHeightForWidth())
        self.frame_extractInvoice.setSizePolicy(sizePolicy1)
        self.frame_extractInvoice.setFrameShape(QFrame.StyledPanel)
        self.frame_extractInvoice.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_extractInvoice)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_18 = QLabel(self.frame_extractInvoice)
        self.label_18.setObjectName(u"label_18")
        font8 = QFont()
        font8.setFamilies([u"Inter Variable Text"])
        font8.setPointSize(15)
        self.label_18.setFont(font8)

        self.gridLayout_25.addWidget(self.label_18, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_24.addWidget(self.frame_extractInvoice, 1, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.startExtractBtn = QPushButton(self.page_extract)
        self.startExtractBtn.setObjectName(u"startExtractBtn")
        font9 = QFont()
        font9.setFamilies([u"Inter Variable Text"])
        self.startExtractBtn.setFont(font9)
        icon7 = QIcon()
        icon7.addFile(u":/icon/resource/icon/search-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startExtractBtn.setIcon(icon7)
        self.startExtractBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_11.addWidget(self.startExtractBtn)

        self.clearInvoiceBtn = QPushButton(self.page_extract)
        self.clearInvoiceBtn.setObjectName(u"clearInvoiceBtn")
        self.clearInvoiceBtn.setFont(font9)
        icon8 = QIcon()
        icon8.addFile(u":/icon/resource/icon/document-circle-wrong.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearInvoiceBtn.setIcon(icon8)
        self.clearInvoiceBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_11.addWidget(self.clearInvoiceBtn)


        self.gridLayout_24.addLayout(self.verticalLayout_11, 1, 1, 1, 1)

        self.frame_13 = QFrame(self.page_extract)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_13)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.label_22 = QLabel(self.frame_13)
        self.label_22.setObjectName(u"label_22")
        font10 = QFont()
        font10.setFamilies([u"Inter Variable Text"])
        font10.setPointSize(12)
        self.label_22.setFont(font10)

        self.verticalLayout_12.addWidget(self.label_22)

        self.lineEdit_invoiceNo = QLineEdit(self.frame_13)
        self.lineEdit_invoiceNo.setObjectName(u"lineEdit_invoiceNo")
        self.lineEdit_invoiceNo.setMinimumSize(QSize(0, 35))
        self.lineEdit_invoiceNo.setFont(font10)

        self.verticalLayout_12.addWidget(self.lineEdit_invoiceNo)


        self.gridLayout_26.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.confirmInvoDataBtn = QPushButton(self.frame_13)
        self.confirmInvoDataBtn.setObjectName(u"confirmInvoDataBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icon/resource/icon/assept-document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.confirmInvoDataBtn.setIcon(icon9)

        self.gridLayout_26.addWidget(self.confirmInvoDataBtn, 2, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_24.addWidget(self.frame_13, 1, 2, 1, 1)

        self.extractHistoryBtn = QPushButton(self.page_extract)
        self.extractHistoryBtn.setObjectName(u"extractHistoryBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icon/resource/icon/time-past.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extractHistoryBtn.setIcon(icon10)

        self.gridLayout_24.addWidget(self.extractHistoryBtn, 0, 2, 1, 1, Qt.AlignRight)

        self.stackedWidget.addWidget(self.page_extract)
        self.page_training = QWidget()
        self.page_training.setObjectName(u"page_training")
        self.page_training.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.gridLayout_23 = QGridLayout(self.page_training)
        self.gridLayout_23.setSpacing(25)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(25, 25, 25, 25)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer, 6, 1, 1, 1)

        self.frame_Load = QFrame(self.page_training)
        self.frame_Load.setObjectName(u"frame_Load")
        sizePolicy1.setHeightForWidth(self.frame_Load.sizePolicy().hasHeightForWidth())
        self.frame_Load.setSizePolicy(sizePolicy1)
        self.frame_Load.setFrameShape(QFrame.StyledPanel)
        self.frame_Load.setFrameShadow(QFrame.Raised)

        self.gridLayout_23.addWidget(self.frame_Load, 4, 0, 1, 5, Qt.AlignHCenter)

        self.label_16 = QLabel(self.page_training)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        font11 = QFont()
        font11.setFamilies([u"Inter Variable Text"])
        font11.setPointSize(28)
        font11.setBold(False)
        self.label_16.setFont(font11)

        self.gridLayout_23.addWidget(self.label_16, 0, 0, 1, 5, Qt.AlignLeft)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_19 = QLabel(self.page_training)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font10)

        self.verticalLayout_8.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.label_afterTrainAcc = QLabel(self.page_training)
        self.label_afterTrainAcc.setObjectName(u"label_afterTrainAcc")
        self.label_afterTrainAcc.setFont(font10)
        self.label_afterTrainAcc.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_8.addWidget(self.label_afterTrainAcc, 0, Qt.AlignHCenter)


        self.gridLayout_23.addLayout(self.verticalLayout_8, 6, 0, 1, 1)

        self.line = QFrame(self.page_training)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_23.addWidget(self.line, 2, 0, 1, 5)

        self.startTrainBtn = QPushButton(self.page_training)
        self.startTrainBtn.setObjectName(u"startTrainBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        sizePolicy4.setHeightForWidth(self.startTrainBtn.sizePolicy().hasHeightForWidth())
        self.startTrainBtn.setSizePolicy(sizePolicy4)
        self.startTrainBtn.setMinimumSize(QSize(200, 0))
        self.startTrainBtn.setFont(font9)

        self.gridLayout_23.addWidget(self.startTrainBtn, 3, 0, 1, 5, Qt.AlignHCenter)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_21 = QLabel(self.page_training)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font10)

        self.verticalLayout_9.addWidget(self.label_21, 0, Qt.AlignHCenter)

        self.label_afterTrainLoss = QLabel(self.page_training)
        self.label_afterTrainLoss.setObjectName(u"label_afterTrainLoss")
        self.label_afterTrainLoss.setFont(font10)
        self.label_afterTrainLoss.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_9.addWidget(self.label_afterTrainLoss, 0, Qt.AlignHCenter)


        self.gridLayout_23.addLayout(self.verticalLayout_9, 6, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_23 = QLabel(self.page_training)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font10)

        self.verticalLayout_10.addWidget(self.label_23, 0, Qt.AlignHCenter)

        self.label_trainTime = QLabel(self.page_training)
        self.label_trainTime.setObjectName(u"label_trainTime")
        self.label_trainTime.setFont(font10)
        self.label_trainTime.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_10.addWidget(self.label_trainTime, 0, Qt.AlignHCenter)


        self.gridLayout_23.addLayout(self.verticalLayout_10, 6, 4, 1, 1)

        self.line_2 = QFrame(self.page_training)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_23.addWidget(self.line_2, 5, 0, 1, 5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_17 = QLabel(self.page_training)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font10)

        self.verticalLayout_6.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.label_NoofInvoicestoTrain = QLabel(self.page_training)
        self.label_NoofInvoicestoTrain.setObjectName(u"label_NoofInvoicestoTrain")
        font12 = QFont()
        font12.setFamilies([u"Inter Variable Text"])
        font12.setPointSize(20)
        self.label_NoofInvoicestoTrain.setFont(font12)
        self.label_NoofInvoicestoTrain.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_6.addWidget(self.label_NoofInvoicestoTrain, 0, Qt.AlignHCenter)


        self.gridLayout_23.addLayout(self.verticalLayout_6, 1, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_2, 6, 3, 1, 1)

        self.stackedWidget.addWidget(self.page_training)
        self.page_collect = QWidget()
        self.page_collect.setObjectName(u"page_collect")
        self.page_collect.setEnabled(True)
        self.page_collect.setStyleSheet(u"")
        self.gridLayout_15 = QGridLayout(self.page_collect)
        self.gridLayout_15.setSpacing(25)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(25, 25, 25, 25)
        self.label_8 = QLabel(self.page_collect)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.gridLayout_15.addWidget(self.label_8, 0, 0, 1, 1)

        self.frame_image_preview = QFrame(self.page_collect)
        self.frame_image_preview.setObjectName(u"frame_image_preview")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_image_preview.sizePolicy().hasHeightForWidth())
        self.frame_image_preview.setSizePolicy(sizePolicy5)
        self.frame_image_preview.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.frame_image_preview.setFrameShape(QFrame.StyledPanel)
        self.frame_image_preview.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_image_preview)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_14 = QLabel(self.frame_image_preview)
        self.label_14.setObjectName(u"label_14")
        font13 = QFont()
        font13.setPointSize(15)
        self.label_14.setFont(font13)

        self.gridLayout_20.addWidget(self.label_14, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_15.addWidget(self.frame_image_preview, 1, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ocrBtn = QPushButton(self.page_collect)
        self.ocrBtn.setObjectName(u"ocrBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icon/resource/icon/right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ocrBtn.setIcon(icon11)
        self.ocrBtn.setIconSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.ocrBtn)

        self.image_preview_clearBtn = QPushButton(self.page_collect)
        self.image_preview_clearBtn.setObjectName(u"image_preview_clearBtn")
        font14 = QFont()
        self.image_preview_clearBtn.setFont(font14)
        icon12 = QIcon()
        icon12.addFile(u":/icon/resource/icon/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.image_preview_clearBtn.setIcon(icon12)
        self.image_preview_clearBtn.setIconSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.image_preview_clearBtn)


        self.gridLayout_15.addLayout(self.verticalLayout_5, 1, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableView__image_data = QTableView(self.page_collect)
        self.tableView__image_data.setObjectName(u"tableView__image_data")
        sizePolicy5.setHeightForWidth(self.tableView__image_data.sizePolicy().hasHeightForWidth())
        self.tableView__image_data.setSizePolicy(sizePolicy5)
        self.tableView__image_data.setFont(font14)
        self.tableView__image_data.setAutoFillBackground(False)
        self.tableView__image_data.setStyleSheet(u"")
        self.tableView__image_data.setLineWidth(1)
        self.tableView__image_data.setMidLineWidth(10)
        self.tableView__image_data.setDragDropMode(QAbstractItemView.DragDrop)
        self.tableView__image_data.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView__image_data.setIconSize(QSize(100, 100))

        self.verticalLayout_7.addWidget(self.tableView__image_data)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_preview_list_clearAllBtn = QPushButton(self.page_collect)
        self.image_preview_list_clearAllBtn.setObjectName(u"image_preview_list_clearAllBtn")
        self.image_preview_list_clearAllBtn.setLayoutDirection(Qt.RightToLeft)
        icon13 = QIcon()
        icon13.addFile(u":/icon/resource/icon/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.image_preview_list_clearAllBtn.setIcon(icon13)
        self.image_preview_list_clearAllBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.image_preview_list_clearAllBtn)

        self.invoDataSubmitBtn = QPushButton(self.page_collect)
        self.invoDataSubmitBtn.setObjectName(u"invoDataSubmitBtn")
        self.invoDataSubmitBtn.setLayoutDirection(Qt.RightToLeft)
        icon14 = QIcon()
        icon14.addFile(u":/icon/resource/icon/submit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.invoDataSubmitBtn.setIcon(icon14)
        self.invoDataSubmitBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.invoDataSubmitBtn)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.gridLayout_15.addLayout(self.verticalLayout_7, 1, 2, 2, 1)

        self.lineEdit_invoNumber = QLineEdit(self.page_collect)
        self.lineEdit_invoNumber.setObjectName(u"lineEdit_invoNumber")
        self.lineEdit_invoNumber.setMinimumSize(QSize(300, 40))
        font15 = QFont()
        font15.setPointSize(12)
        self.lineEdit_invoNumber.setFont(font15)
        self.lineEdit_invoNumber.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_invoNumber.setAlignment(Qt.AlignCenter)
        self.lineEdit_invoNumber.setClearButtonEnabled(True)

        self.gridLayout_15.addWidget(self.lineEdit_invoNumber, 2, 0, 1, 1)

        self.ocr_library_btn = QPushButton(self.page_collect)
        self.ocr_library_btn.setObjectName(u"ocr_library_btn")
        self.ocr_library_btn.setFont(font14)
        self.ocr_library_btn.setLayoutDirection(Qt.RightToLeft)
        self.ocr_library_btn.setStyleSheet(u"QPushButton{\n"
"	padding:10px 10px 10px 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 255, 255, 200);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icon/resource/icon/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ocr_library_btn.setIcon(icon15)
        self.ocr_library_btn.setIconSize(QSize(30, 30))
        self.ocr_library_btn.setAutoDefault(False)

        self.gridLayout_15.addWidget(self.ocr_library_btn, 3, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_collect)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.stackedWidget.addWidget(self.page_settings)
        self.page_account = QWidget()
        self.page_account.setObjectName(u"page_account")
        self.stackedWidget.addWidget(self.page_account)
        self.page_ocrLibrary = QWidget()
        self.page_ocrLibrary.setObjectName(u"page_ocrLibrary")
        self.gridLayout_21 = QGridLayout(self.page_ocrLibrary)
        self.gridLayout_21.setSpacing(25)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(25, 25, 25, 25)
        self.frame_2 = QFrame(self.page_ocrLibrary)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(10)
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_2)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        font16 = QFont()
        font16.setPointSize(18)
        font16.setBold(True)
        self.label_11.setFont(font16)
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_21.addWidget(self.frame_2, 2, 0, 1, 1)

        self.progressBar_drawAnnotation = QProgressBar(self.page_ocrLibrary)
        self.progressBar_drawAnnotation.setObjectName(u"progressBar_drawAnnotation")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.progressBar_drawAnnotation.sizePolicy().hasHeightForWidth())
        self.progressBar_drawAnnotation.setSizePolicy(sizePolicy7)
        self.progressBar_drawAnnotation.setStyleSheet(u"background-color: rgb(87, 84, 111);\n"
"")
        self.progressBar_drawAnnotation.setValue(0)
        self.progressBar_drawAnnotation.setTextVisible(False)

        self.gridLayout_21.addWidget(self.progressBar_drawAnnotation, 3, 0, 1, 1)

        self.label_15 = QLabel(self.page_ocrLibrary)
        self.label_15.setObjectName(u"label_15")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy8)
        self.label_15.setFont(font4)

        self.gridLayout_21.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignLeft)

        self.library_listWidget = QListWidget(self.page_ocrLibrary)
        self.library_listWidget.setObjectName(u"library_listWidget")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(3)
        sizePolicy9.setHeightForWidth(self.library_listWidget.sizePolicy().hasHeightForWidth())
        self.library_listWidget.setSizePolicy(sizePolicy9)
        self.library_listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.library_listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.library_listWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.library_listWidget.setIconSize(QSize(100, 100))
        self.library_listWidget.setMovement(QListView.Snap)
        self.library_listWidget.setFlow(QListView.LeftToRight)
        self.library_listWidget.setResizeMode(QListView.Adjust)
        self.library_listWidget.setViewMode(QListView.IconMode)
        self.library_listWidget.setItemAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.library_listWidget, 4, 0, 1, 1)

        self.ocrLibraryBackBtn = QPushButton(self.page_ocrLibrary)
        self.ocrLibraryBackBtn.setObjectName(u"ocrLibraryBackBtn")
        icon16 = QIcon()
        icon16.addFile(u":/icon/resource/icon/angle-small-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ocrLibraryBackBtn.setIcon(icon16)

        self.gridLayout_21.addWidget(self.ocrLibraryBackBtn, 1, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_ocrLibrary)
        self.page_extractHistory = QWidget()
        self.page_extractHistory.setObjectName(u"page_extractHistory")
        self.gridLayout_27 = QGridLayout(self.page_extractHistory)
        self.gridLayout_27.setSpacing(25)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(25, 25, 25, 25)
        self.label_24 = QLabel(self.page_extractHistory)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)

        self.gridLayout_27.addWidget(self.label_24, 0, 0, 1, 1, Qt.AlignLeft)

        self.tableView = QTableView(self.page_extractHistory)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_27.addWidget(self.tableView, 2, 0, 1, 1)

        self.extractHistoryBackBtn = QPushButton(self.page_extractHistory)
        self.extractHistoryBackBtn.setObjectName(u"extractHistoryBackBtn")
        self.extractHistoryBackBtn.setIcon(icon16)

        self.gridLayout_27.addWidget(self.extractHistoryBackBtn, 1, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.page_extractHistory)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.lineEdit_invoNumber.returnPressed.connect(self.ocrBtn.click)
        self.image_preview_clearBtn.clicked.connect(self.lineEdit_invoNumber.clear)
        self.image_preview_list_clearAllBtn.clicked["bool"].connect(self.image_preview_clearBtn.click)
        self.image_preview_list_clearAllBtn.clicked.connect(self.ocrBtn.click)
        self.invoDataSubmitBtn.clicked["bool"].connect(self.tableView__image_data.reset)
        self.image_preview_list_clearAllBtn.clicked["bool"].connect(self.tableView__image_data.reset)
        self.clearInvoiceBtn.clicked["bool"].connect(self.lineEdit_invoiceNo.clear)
        self.startExtractBtn.clicked["bool"].connect(self.lineEdit_invoiceNo.clear)

        self.btn_dashboard.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.ocr_library_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Invoice Number Extractor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" This Research Project can make mistakes. Consider checking important information.", None))
        self.btn_collect.setText(QCoreApplication.translate("MainWindow", u"  Collect", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dulaj Umansha", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.btn_extract.setText(QCoreApplication.translate("MainWindow", u"  Extract", None))
        self.btn_training.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.btn_account.setText("")
        self.btn_setting.setText("")
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
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop", None))
        self.startExtractBtn.setText("")
        self.clearInvoiceBtn.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Invoice Number", None))
        self.confirmInvoDataBtn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.extractHistoryBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.label_afterTrainAcc.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.startTrainBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Loss", None))
        self.label_afterTrainLoss.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_trainTime.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Number of Invoices:", None))
        self.label_NoofInvoicestoTrain.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Collect Invoices", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop", None))
        self.ocrBtn.setText("")
        self.image_preview_clearBtn.setText("")
        self.image_preview_list_clearAllBtn.setText(QCoreApplication.translate("MainWindow", u"  Clear All  ", None))
        self.invoDataSubmitBtn.setText(QCoreApplication.translate("MainWindow", u"  Submit  ", None))
        self.lineEdit_invoNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Invoice Number", None))
        self.ocr_library_btn.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"There are no Previous \n"
"Recodes", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.ocrLibraryBackBtn.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.extractHistoryBackBtn.setText("")
    # retranslateUi

