from __interface__.ui_mainwindow import Ui_MainWindow
from database.database import Database


class page_extractHistory:
    def __init__(self, mainUI: Ui_MainWindow, db: Database) -> None:
        self.mainUI = mainUI
        self.db = db

        self.mainUI.extractHistoryBackBtn.clicked.connect(self.extractHistoryBackBtn_clicked)

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(7)

    def extractHistoryBackBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(1)