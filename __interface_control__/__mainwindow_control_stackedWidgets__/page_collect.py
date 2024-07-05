from __interface__.ui_mainwindow import Ui_MainWindow
from __interface_control__.__mainwindow_control_stackedWidgets__.page_ocrLibrary import (
    page_ocrLibrary,
)
from __interface_control__.dragAndDropListWidget import *
from PySide6.QtWidgets import QAbstractItemView
import os
from OCR import OCR
from PySide6.QtCore import QThread, Signal, QObject
from __interface_control__.tableModel import TableModel
from database.database import Database
from database.tbl_ocr_data import tbl_ocr_data
import shutil
from format import FormatData


class OCRThread(QThread):
    progress_updated = Signal(int)
    finished = Signal(list)

    def __init__(self,imageData_list):
        super().__init__()
        self.imageData_list = imageData_list
        self.ocr = OCR()
        self.formatData = FormatData()

    def run(self):
        try:
            self.filePaths = [url[0] for url in self.imageData_list]
            self.invoiceNumber = [no[1] for no in self.imageData_list]
            self.update_progress(20)

            data = self.ocr.read(self.filePaths[0])
            self.update_progress(70)
            formated_ocrData:list = self.formatData.format(data, self.invoiceNumber[0])
            formated_ocrData = formated_ocrData+(self.filePaths[0],)
            self.finished.emit(formated_ocrData)

        except Exception as e:
            print(f"Error in OCRThread: {str(e)}")

    def update_progress(self, value):
        self.progress_updated.emit(value)


class page_collect:
    def __init__(self, mainUI: Ui_MainWindow, db: Database) -> None:
        self.mainUI = mainUI
        self.db = db
        self.ocrLibrary = page_ocrLibrary(self.mainUI, db)
        self.tblOCRData = tbl_ocr_data()

        self.ListWidget = dragAndDropListWidget()
        self.ListWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.mainUI.gridLayout_15.addWidget(self.ListWidget, 1, 0, 1, 1)

        self.ListWidget.fileDropped.connect(self.pictureDropped)
        self.mainUI.ocr_library_btn.clicked.connect(self.ocrLibrary.stackedBtn_clicked)
        self.mainUI.ocrBtn.clicked.connect(self.ocrBtn_clicked_connect)
        self.mainUI.image_preview_clearBtn.clicked.connect(self.ListWidget.clearList)
        self.mainUI.image_preview_list_clearAllBtn.clicked.connect(self.image_preview_list_clearAllBtn_clicked)

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(3)

    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                icon = QtGui.QIcon(url)
                item = QtWidgets.QListWidgetItem(url, self.ListWidget)
                item.setIcon(icon)
                item.setStatusTip(url)

    def ocrBtn_clicked_connect(self):
        url = self.ListWidget.getItem()
        invoNo = self.mainUI.lineEdit_invoNumber.text()

        self.worker_thread = OCRThread([[url,invoNo]])
        self.worker_thread.progress_updated.connect(self.update_progress_bar)
        self.worker_thread.finished.connect(self.finishedOCR)
        self.worker_thread.start()

    def update_progress_bar(self, value):
        self.mainUI.progressBar_collcet.setValue(value)
    
    def finishedOCR(self,formated_data):
        self.mainUI.progressBar_collcet.setValue(0)
        self.mainUI.page_collect.setEnabled(True)

        self.model = TableModel(formated_data[0])
        self.mainUI.tableView__image_data.setModel(self.model)
        self.mainUI.invoDataSubmitBtn.clicked.connect(lambda:self.invoDataSubmitBtn_clicked_connect(formated_data))

    def invoDataSubmitBtn_clicked_connect(self,formated_data):
        invoNo = self.mainUI.lineEdit_invoNumber.text()
        img_fileName = formated_data[2].split("/")[-1]
        csvFileName = img_fileName.split(".")[0]
        if "ocr_similarityInvoNoValue" in formated_data[0].columns:
            formated_data[0].to_csv("csv data/" + str(csvFileName)+".csv", index=False)
            self.copyImageTolocalDir(formated_data[2])
            dbData = [formated_data[1],invoNo,img_fileName,csvFileName+".csv"]
            self.update_database(dbData)
        else:
            print(img_fileName, "could not find invoice number amoung ocr Data")
        self.mainUI.image_preview_list_clearAllBtn.click()
        
    def copyImageTolocalDir(self,img_filePath):
            shutil.copy(img_filePath, "invoices\\")

    def update_database(self, formatedData):
        try:
            self.db.connect()

            self.tblOCRData.set_index_no(formatedData[0])
            self.tblOCRData.set_invo_no(formatedData[1])
            self.tblOCRData.set_image_name(formatedData[-2])
            self.tblOCRData.set_csv_file_name(formatedData[-1])
            self.tblOCRData.insertData(db=self.db.get_db())

        except Exception as e:
            print(f"Error updating database: {str(e)}")
        finally:
            self.db.close()

    def image_preview_list_clearAllBtn_clicked(self):
        self.model.clear()
