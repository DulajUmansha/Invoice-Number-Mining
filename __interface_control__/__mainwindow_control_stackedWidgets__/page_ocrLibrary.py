from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from __interface__.ui_mainwindow import Ui_MainWindow
from database.database import Database
from database.tbl_ocr_data import tbl_ocr_data
from PySide6 import QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from keras_ocr import tools
import mplcursors
from matplotlib.patches import Rectangle

from format import FormatData

class Annotator:
    def __init__(self, ax, image, predictions):
        self.ax = ax
        self.image = image
        self.predictions = predictions
        self.rect = None

    def on_click(self, event):
        if self.rect:
            self.rect.remove()
        
        x, y = event.target
        width, height = 50, 50  # You can customize the rectangle size
        self.rect = Rectangle((x - width / 2, y - height / 2), width, height, linewidth=1, edgecolor='b', facecolor='none')
        self.ax.add_patch(self.rect)

        # Perform actions based on the selected region, e.g., print coordinates
        print(f"Selected region: x={x}, y={y}, width={width}, height={height}")

class page_ocrLibrary:
    def __init__(self, mainUI: Ui_MainWindow, db: Database) -> None:
        self.mainUI = mainUI
        self.db = db
        self.ocrDataList = []
        self.formatData = FormatData()
        self.tblOCRData = tbl_ocr_data()
        self.mainUI.library_listWidget.currentItemChanged.connect(self.library_listWidget_currentItemChanged)
        self.mainUI.ocrLibraryBackBtn.clicked.connect(self.ocrLibraryBackBtn_clicked)

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(6)
        self.addimages()
        self.library_listWidget_currentItemChanged()

    def ocrLibraryBackBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(3)

    def addimages(self):
        self.mainUI.library_listWidget.clear()
        data = self.getOCRImageData()
        ids = [item["id"] for item in data]
        file_paths = [item["image_name"] for item in data]
        invo_numbers = [item["invo_no"] for item in data]
        csv_file_names = [item["csv_file_name"] for item in data]
        for file_path, invo_no, csv_file_name, id in zip(
            file_paths, invo_numbers, csv_file_names, ids
        ):
            if self.validateOCR(invo_no, csv_file_name, id):
                icon = QtGui.QIcon("invoices/" +file_path)
                item = QtWidgets.QListWidgetItem(
                    invo_no, self.mainUI.library_listWidget
                )
                item.setIcon(icon)
                self.ocrDataList.append([invo_no, file_path, csv_file_name])

    def getOCRImageData(self):
        self.db.connect()
        data = self.tblOCRData.retriveData()
        self.db.close()
        return data

    def library_listWidget_currentItemChanged(self):
        if len(self.ocrDataList) != 0:
            itemIndex = self.mainUI.library_listWidget.currentIndex().row()
            data = self.getDataFromCSVFile(self.ocrDataList[itemIndex][2])
            canvas = self.drawAnnotations(self.ocrDataList[itemIndex][1], data)
            self.mainUI.progressBar_drawAnnotation.setValue(100)
            self.mainUI.gridLayout_21.addWidget(canvas, 1, 0, 1, 1)
            self.mainUI.progressBar_drawAnnotation.setValue(0)

    def getDataFromCSVFile(self, csv_file_name: str):
        csvreader = pd.read_csv("csv data/" +csv_file_name)

        result_list = []
        for row in csvreader.iterrows():
            ocr_data = row[1]["ocr_data"]
            x_values = [float(row[1][f"x{i}"]) for i in range(1, 5)]
            y_values = [float(row[1][f"y{i}"]) for i in range(1, 5)]

            coordinates = np.array(list(zip(x_values, y_values)), dtype=np.float32)

            result_list.append((ocr_data, coordinates))
        return result_list 

    def drawAnnotations(self, file_path: str, csvData: list):
        self.mainUI.progressBar_drawAnnotation.setValue(25)
        images = [tools.read("invoices/" +file_path)]

        if hasattr(self, "fig") and self.fig:
            plt.close(self.fig)

        self.fig, self.ax = plt.subplots()
        # Clear the previous annotations
        self.ax.clear()
        annotators = []
        try:
            for image, predictions in zip(images, [csvData]):
                tools.drawAnnotations(image=image, predictions=predictions, ax=self.ax)
                annotator = Annotator(self.ax, image, predictions)
                annotators.append(annotator)
                mplcursors.cursor(hover=False).connect("add", annotator.on_click)
                self.mainUI.progressBar_drawAnnotation.setValue(50)
        except Exception as e:
            print(f"Error: {e}")

        self.mainUI.progressBar_drawAnnotation.setValue(75)
        canvas = FigureCanvas(self.fig)
        canvas.figure.set_facecolor("#FFFFFF96")

        return canvas

    def validateOCR(self, invo_no, csv_file_name, updateID):
        csvreader = pd.read_csv("csv data/" +csv_file_name)

        if self.formatData.isOCRIdentifyInvoiceNo(csvreader,invo_no):
            return True
        
        self.db.connect()
        self.tblOCRData.set_id(updateID)
        self.tblOCRData.set_status("deactive")
        self.tblOCRData.set_conditionData("id", updateID)
        self.tblOCRData.updateData(**dict(self.tblOCRData))
        self.db.close()
        return False
