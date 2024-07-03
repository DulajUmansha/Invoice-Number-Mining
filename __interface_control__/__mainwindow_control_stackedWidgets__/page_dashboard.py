import json
from __interface__.ui_mainwindow import Ui_MainWindow
from __interface_control__.__mainwindow_control_stackedWidgets__.page_extractHistory import page_extractHistory
from __interface_control__.cpu_memory_digram import *
from database.database import Database
from database.tbl_extracedinvoice import tbl_extraced_invoice

class page_dashboard:
    def __init__(self, mainUI:Ui_MainWindow, db: Database) -> None:
        self.mainUI = mainUI
        self.db = db
        self.extract_history = page_extractHistory(self.mainUI,self.db)
        self.cpu_memory_canvas()
        self.updateStats()
        self.mainUI.historyCountBtn.clicked.connect(self.extract_history.stackedBtn_clicked)

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

    def updateStats(self):
        self.db.connect()
        tbl_extracedInvoice = tbl_extraced_invoice()
        tbl_extracedInvoice.set_columnFilter(["invo_no"])
        tbl_extracedInvoice.retriveData()
        self.db.close()
        count = len(tbl_extracedInvoice.get_invo_no())
        self.mainUI.historyCountBtn.setText(str(count))

        # File path where the JSON is saved
        file_path = 'metaData/stats.json'

        # Read the dictionary from the JSON file
        with open(file_path, 'r') as json_file:
            loaded_dict = json.load(json_file)
        
        self.mainUI.accuracy_value.setText(str(loaded_dict['accuracy'])+"%")
        self.mainUI.trained_value.setText(str(loaded_dict['trained_invoices']))