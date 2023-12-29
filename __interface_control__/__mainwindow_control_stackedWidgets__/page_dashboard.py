from __interface__.ui_mainwindow import Ui_MainWindow
from __interface_control__.cpu_memory_digram import *

class page_dashboard:
    def __init__(self, mainUI:Ui_MainWindow) -> None:
        self.mainUI = mainUI
        self.cpu_memory_canvas()

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(0)

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

    def close(self, event):
        # Terminate the worker thread forcefully
        self.worker_thread.terminate()
        self.worker_thread.wait()
        event.accept()