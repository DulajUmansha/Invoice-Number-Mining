import os
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtCore import QThread, Signal
import numpy as np
import tensorflow as tf
from OCR import OCR
from __interface__.ui_mainwindow import Ui_MainWindow
from __interface_control__.__mainwindow_control_stackedWidgets__.page_extractHistory import page_extractHistory
from __interface_control__.dragAndDropListWidget import *
from database.database import Database
from format import FormatData

class ExtractThread(QThread):
    progress_updated = Signal(int)
    finished = Signal(str)

    def __init__(self, url, parent = None) -> None:
        super().__init__(parent)
        self.model = tf.keras.models.load_model("metaData/model.h5")
        self.ocr = OCR()
        self.format_data = FormatData()
        self.x_data=[]
        self.invoUrl = url

    def run(self) -> None:
        try:
            self.update_progress(10)
            ocrData = self.ocr.read(self.invoUrl)
            self.update_progress(50)
            formated_ocrData = self.format_data.formatInvoice(ocrData)
            self.update_progress(70)
            
            formated_ocrData1 = formated_ocrData.drop(columns=['ocr_data','confident_level'])
            max_value = formated_ocrData1.max().max()
        
            formated_ocrData1[['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4']] = formated_ocrData1[['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4']].div(max_value).round(6)


            self.x_data.append(np.array(formated_ocrData1.values.tolist()))
            self.x_data = tf.keras.preprocessing.sequence.pad_sequences(self.x_data, padding="post", maxlen=277, dtype="float32")
            

            (_,DATA_HEIGHT, DATA_WIDTH) = self.x_data.shape
            DATA_CHANNELS = 1
            x_data_with_chanels = self.x_data.reshape(self.x_data.shape[0],DATA_HEIGHT,DATA_WIDTH,DATA_CHANNELS)
            predictions = self.model.predict(x_data_with_chanels)
            predicted_invoNo = formated_ocrData.at[int(predictions[0][0]),'ocr_data']
            self.update_progress(100)
            self.finished.emit(predicted_invoNo)

        except Exception as e:
            print(f"Error in OCRThread: {str(e)}")

    def update_progress(self, value):
        self.progress_updated.emit(value)

class page_extract:
    def __init__(self, mainUI:Ui_MainWindow,  db: Database) -> None:
        self.mainUI = mainUI
        self.db = db
        self.invoUrl = None
        self.extract_history = page_extractHistory(self.mainUI,self.db)
        
        self.ListWidget = dragAndDropListWidget()
        self.ListWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.mainUI.gridLayout_24.addWidget(self.ListWidget, 1, 0, 1, 1)

        self.ListWidget.fileDropped.connect(self.pictureDropped)
        self.mainUI.clearInvoiceBtn.clicked.connect(self.ListWidget.clearList)
        self.mainUI.startExtractBtn.clicked.connect(self.startExtractBtn_clicked)

        self.mainUI.extractHistoryBtn.clicked.connect(self.extract_history.stackedBtn_clicked)

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(1)
    
    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                icon = QtGui.QIcon(url)
                icon = icon.pixmap(self.mainUI.frame_extractInvoice.size())
                icon = icon.scaled(self.mainUI.frame_extractInvoice.size())
                item = QtWidgets.QListWidgetItem(self.ListWidget)
                item.setIcon(icon)
                item.setStatusTip(url)
                self.invoUrl = url

    def startExtractBtn_clicked(self):
        self.worker_thread = ExtractThread(self.invoUrl)
        self.worker_thread.progress_updated.connect(self.update_progress_bar)
        self.worker_thread.finished.connect(self.extract_finished)
        self.worker_thread.start()
        self.mainUI.startExtractBtn.setDisabled(True)

    def extract_finished(self,predicted_invoNo):
        self.mainUI.lineEdit_invoiceNo.setText(str(predicted_invoNo))
        self.mainUI.startExtractBtn.setEnabled(True)
        self.mainUI.progressBar_extract.setValue(0)

    def update_progress_bar(self, value):
        self.mainUI.progressBar_extract.setValue(value)
    
