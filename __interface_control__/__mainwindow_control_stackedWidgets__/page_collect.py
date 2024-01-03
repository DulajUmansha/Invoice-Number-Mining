from __interface__.ui_mainwindow import Ui_MainWindow
from __interface_control__.__mainwindow_control_stackedWidgets__.page_ocrLibrary import (
    page_ocrLibrary,
)
from __interface_control__.dragAndDropListWidget import *
from PySide6.QtWidgets import QAbstractItemView
import os, time
from OCR import OCR
from CSVfile import CSVfile
from PySide6.QtCore import QThread, Signal
from database.database import Database
from database.tbl_ocr_data import tbl_ocr_data
import shutil


class OCRThread(QThread):
    ocr_completed = Signal(object)
    progress_updated = Signal(int)

    def __init__(self, imageData_list):
        super().__init__()
        self.imageData_list = imageData_list
        self.ocr = OCR()
        self.csvFile = CSVfile()

    def run(self):
        try:
            self.copyImageTolocalDir()
            self.invoiceUrlList = [url[0] for url in self.imageData_list]
            self.invoiceNumber = [no[1] for no in self.imageData_list]
            self.update_progress(20)

            fileNames = [
                self.csvFile.generateFileName()
                for url in self.imageData_list
                if time.sleep(0.2) is None
            ]

            data = self.ocr.read(self.invoiceUrlList)
            self.update_progress(70)

            formatedData = self.csvFile.formatData(
                self.invoiceNumber, data, self.invoiceUrlList, fileNames
            )
            self.csvFile.write(formatedData)

            self.update_database(formatedData)
            self.update_progress(100)
            self.ocr_completed.emit(formatedData)
        except Exception as e:
            print(f"Error in OCRThread: {str(e)}")

    def copyImageTolocalDir(self):
        newUrl = []
        for image, invoNo in self.imageData_list:
            shutil.copy(image, "invoices\\")
            newUrl.append(["invoices/" + image.split("/")[-1], invoNo])
        self.imageData_list = newUrl

    def update_progress(self, value):
        self.progress_updated.emit(value)

    def update_database(self, formatedData):
        db = Database()
        try:
            db.connect()
            tblOCRData = tbl_ocr_data()

            for datum in formatedData:
                tblOCRData.set_invo_no(datum[0])
                tblOCRData.set_file_path(datum[-2])
                tblOCRData.set_csv_file_name(datum[-1])
                tblOCRData.insertData()

        except Exception as e:
            print(f"Error updating database: {str(e)}")
        finally:
            db.close()


class page_collect:
    def __init__(self, mainUI: Ui_MainWindow) -> None:
        self.mainUI = mainUI
        self.ocrLibrary = page_ocrLibrary(self.mainUI)

        self.ListWidget = dragAndDropListWidget()
        self.ListWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.mainUI.gridLayout_15.addWidget(self.ListWidget, 1, 0, 1, 1)

        self.ListWidget.fileDropped.connect(self.pictureDropped)
        self.mainUI.invoDataCollectBtn.clicked.connect(self.invoDataCollectBtn_clicked)
        self.mainUI.invoDataSubmitBtn.clicked.connect(self.invoDataSubmitBtn_clicked)
        self.mainUI.image_preview_clearBtn.clicked.connect(
            self.image_preview_clearBtn_clicked
        )
        self.mainUI.image_preview_list_clearAllBtn.clicked.connect(
            self.image_preview_list_clearAllBtn_clicked
        )
        self.mainUI.ocr_library_btn.clicked.connect(self.ocrLibrary.stackedBtn_clicked)

        self.collectedInvoiceList = []

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(3)

    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                icon = QtGui.QIcon(url)
                item = QtWidgets.QListWidgetItem(url, self.ListWidget)
                item.setIcon(icon)
                item.setStatusTip(url)

    def invoDataCollectBtn_clicked(self):
        invoNo = self.mainUI.lineEdit_invoNumber.text()
        url = self.ListWidget.getItem()
        if invoNo and url:
            item = QtWidgets.QListWidgetItem(
                invoNo, self.mainUI.listWidget__image_preview
            )
            item.setIcon(QtGui.QIcon(url))
            self.collectedInvoiceList.append([url, invoNo])
            self.ListWidget.clearList()
            self.mainUI.lineEdit_invoNumber.clear()

    def invoDataSubmitBtn_clicked(self):
        self.mainUI.page_collect.setDisabled(True)
        self.ocr_thread = OCRThread(self.collectedInvoiceList)
        # self.ocr_thread.ocr_completed.connect(self.ocr_completed)
        self.ocr_thread.progress_updated.connect(self.update_progress_bar)
        self.ocr_thread.start()

    def update_progress_bar(self, value):
        self.mainUI.progressBar_collcet.setValue(value)
        if value == 100:
            time.sleep(1)
            self.mainUI.progressBar_collcet.setValue(0)
            self.mainUI.page_collect.setEnabled(True)

    def task_completed(self):
        self.mainUI.progressBar_collcet.setValue(100)

    def image_preview_clearBtn_clicked(self):
        self.ListWidget.clearList()

    def image_preview_list_clearAllBtn_clicked(self):
        self.collectedInvoiceList.clear()
