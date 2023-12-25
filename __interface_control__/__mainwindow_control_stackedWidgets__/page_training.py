from __interface__.ui_mainwindow import Ui_MainWindow

class page_training:
    def __init__(self, mainUI:Ui_MainWindow) -> None:
        self.mainUI = mainUI

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(2)