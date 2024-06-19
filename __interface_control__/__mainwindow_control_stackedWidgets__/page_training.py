from __interface__.ui_mainwindow import Ui_MainWindow
from database.database import Database
from model import Model

class page_training:
    def __init__(self, mainUI:Ui_MainWindow, db:Database) -> None:
        self.mainUI = mainUI
        self.db = db
        self.model = Model()

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(2)
        self.model.train()