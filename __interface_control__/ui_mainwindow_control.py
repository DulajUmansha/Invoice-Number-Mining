from __interface__.ui_mainwindow import *
import __interface__.rc_resource
from __interface_control__.cpu_memory_digram import *
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

        self.dashboard = page_dashboard(self.mainUI)
        self.account = page_account(self.mainUI)
        self.extract = page_extract(self.mainUI)
        self.training = page_training(self.mainUI)
        self.collect = page_collect(self.mainUI)
        self.setting = page_settings(self.mainUI)

        self.buttonClicked()
        self.cpu_memory_canvas()

    def cpu_memory_canvas(self):
        # Create CPU usage canvas
        self.cpu_sc = MplCanvas(self.mainUI.frame_CPU, width=5, height=2, dpi=100)
        self.mainUI.gridLayout_16.addWidget(self.cpu_sc)

        # Create Memory usage canvas
        self.memory_sc = MplCanvas(self.mainUI.frame_Memory,  width=5, height=2, dpi=100)
        self.mainUI.gridLayout_18.addWidget(self.memory_sc)

        # Create a worker thread
        self.worker_thread = WorkerThread()
        self.worker_thread.update_signal.connect(self.update_plots)
        self.worker_thread.start()

    def update_plots(self, cpu_data, memory_data):
        update_plot(cpu_data, memory_data, self.cpu_sc, self.memory_sc)

    def closeEvent(self, event):
        # Terminate the worker thread forcefully
        self.worker_thread.terminate()
        self.worker_thread.wait()
        event.accept()

    def buttonClicked(self):
        self.mainUI.btn_dashboard.clicked.connect(self.dashboard.stackedBtn_clicked)
        self.mainUI.btn_account.clicked.connect(self.account.stackedBtn_clicked)
        self.mainUI.btn_extract.clicked.connect(self.extract.stackedBtn_clicked)
        self.mainUI.btn_training.clicked.connect(self.training.stackedBtn_clicked)
        self.mainUI.btn_collect.clicked.connect(self.collect.stackedBtn_clicked)
        self.mainUI.btn_setting.clicked.connect(self.setting.stackedBtn_clicked)
