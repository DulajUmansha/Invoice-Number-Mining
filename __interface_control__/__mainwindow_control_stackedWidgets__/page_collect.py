from __interface__.ui_mainwindow import Ui_MainWindow
from __interface__.dragAndDropListWidget import *
import os
from OCR import OCR
from CSVfile import CSVfile
from PySide6.QtCore import QThread, Signal

class OCRThread(QThread):
    ocr_completed = Signal(list)

    def __init__(self, imageData_list):
        super().__init__()
        self.imageData_list = imageData_list
        self.ocr = OCR()
        self.csvFile = CSVfile()

    def run(self):
        self.invoiceUrlList = [url[0] for url in self.imageData_list]
        self.invoiceNumber = [no[1] for no in self.imageData_list]
        data = self.ocr.read(self.invoiceUrlList)
        formattedData = self.csvFile.formatData(self.invoiceNumber, data)
        self.csvFile.append(formattedData)
        self.ocr_completed.emit(data)

class page_collect(QThread):
    def __init__(self, mainUI: Ui_MainWindow) -> None:
        self.mainUI = mainUI
        self.ListWidget = dragAndDropListWidget()
        self.mainUI.gridLayout_15.addWidget(self.ListWidget, 1, 0, 1, 1)
        self.ListWidget.fileDropped.connect(self.pictureDropped)
        self.mainUI.invoDataCollectBtn.clicked.connect(self.invoDataCollectBtn_clicked)
        self.mainUI.invoDataSubmitBtn.clicked.connect(self.invoDataSubmitBtn_clicked)
        self.mainUI.image_preview_list_clearAllBtn.clicked.connect(
            self.image_preview_list_clearAllBtn_clicked
        )
        self.collectedInvoiceList = []

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(3)

    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                icon = QtGui.QIcon(url)
                item = QtWidgets.QListWidgetItem(
                    url, self.ListWidget
                )  # item = QtWidgets.QListWidgetItem(invoice_number,self.ListWidget)
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
        self.ocr_thread = OCRThread(self.collectedInvoiceList)
        # self.ocr_thread.ocr_completed.connect(self.ocr_completed)
        self.ocr_thread.start()

    def image_preview_list_clearAllBtn_clicked(self):
        self.collectedInvoiceList.clear()
