from PySide6.QtGui import QCloseEvent
from __interface__.ui_mainwindow import *
import __interface__.rc_resource
from database.database import Database
from .__mainwindow_control_stackedWidgets__.page_dashboard import page_dashboard
from .__mainwindow_control_stackedWidgets__.page_account import page_account
from .__mainwindow_control_stackedWidgets__.page_extract import page_extract
from .__mainwindow_control_stackedWidgets__.page_training import page_training
from .__mainwindow_control_stackedWidgets__.page_collect import page_collect
from .__mainwindow_control_stackedWidgets__.page_settings import page_settings


class MainWindow(QMainWindow, QWidget):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.mainUI = Ui_MainWindow()
        self.mainUI.setupUi(self)

        self.db = Database()
        self.dashboard = page_dashboard(self.mainUI,self.db)
        self.account = page_account(self.mainUI)
        self.extract = page_extract(self.mainUI,self.db)
        self.training = page_training(self.mainUI,self.db)
        self.collect = page_collect(self.mainUI,self.db)
        self.setting = page_settings(self.mainUI)

        self.buttonClicked()

    def buttonClicked(self):
        self.mainUI.btn_dashboard.clicked.connect(self.dashboard.stackedBtn_clicked)
        self.mainUI.btn_account.clicked.connect(self.account.stackedBtn_clicked)
        self.mainUI.btn_extract.clicked.connect(self.extract.stackedBtn_clicked)
        self.mainUI.btn_training.clicked.connect(self.training.stackedBtn_clicked)
        self.mainUI.btn_collect.clicked.connect(self.collect.stackedBtn_clicked)
        self.mainUI.btn_setting.clicked.connect(self.setting.stackedBtn_clicked)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.dashboard.close(event)
