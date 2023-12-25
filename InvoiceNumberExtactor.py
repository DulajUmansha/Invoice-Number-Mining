# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from __interface_control__.ui_mainwindow_control import MainWindow


if __name__ == "__main__":
    app = QApplication()
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
