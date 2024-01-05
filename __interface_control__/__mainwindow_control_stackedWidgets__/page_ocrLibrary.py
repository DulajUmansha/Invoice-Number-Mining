import csv
from matplotlib import pyplot as plt
import numpy as np
from __interface__.ui_mainwindow import Ui_MainWindow
from database.database import Database
from database.tbl_ocr_data import tbl_ocr_data
from PySide6 import QtWidgets, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from keras_ocr import tools


class page_ocrLibrary:
    def __init__(self, mainUI: Ui_MainWindow, db:Database) -> None:
        self.mainUI = mainUI
        self.db = db
        self.ocrDataList = []
        self.mainUI.library_listWidget.currentItemChanged.connect(self.library_listWidget_currentItemChanged)

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(6)
        self.addimages()
        self.library_listWidget_currentItemChanged()

    def addimages(self):
        self.mainUI.library_listWidget.clear()
        # self.db = Database("qt_sql_library_connection")
        data = self.getOCRImageData()
        file_paths = [item['file_path'] for item in data]
        invo_numbers = [item['invo_no'] for item in data]
        csv_file_names = [item['csv_file_name'] for item in data]
        for file_path, invo_no, csv_file_name in zip(file_paths,invo_numbers, csv_file_names):
            icon = QtGui.QIcon(file_path)
            item = QtWidgets.QListWidgetItem(invo_no, self.mainUI.library_listWidget) 
            item.setIcon(icon)
            self.ocrDataList.append([invo_no,file_path,csv_file_name])

    def getOCRImageData(self):
        self.db.connect()
        tblOCRData = tbl_ocr_data()
        data = tblOCRData.retriveData()
        self.db.close()
        return data
    
    def library_listWidget_currentItemChanged(self):
        if len(self.ocrDataList) != 0:
            itemIndex=self.mainUI.library_listWidget.currentIndex().row()
            data = self.getDataFromCSVFile(self.ocrDataList[itemIndex][2])
            canvas = self.drawAnnotations(self.ocrDataList[itemIndex][1],data)
            self.mainUI.progressBar_drawAnnotation.setValue(100)
            self.mainUI.gridLayout_21.addWidget(canvas, 1, 0, 1, 1)
            self.mainUI.progressBar_drawAnnotation.setValue(0)

    def getDataFromCSVFile(self,csv_file_name:str):
        csvfile =  open("csv data\\"+csv_file_name, "r")
        csvreader = csv.DictReader(csvfile)

        result_list = []
        for row in csvreader:
            ocr_data = row["ocr_data"]
            x_values = [float(row[f"X{i}"]) for i in range(1, 5)]
            y_values = [float(row[f"Y{i}"]) for i in range(1, 5)]

            coordinates = np.array(list(zip(x_values, y_values)), dtype=np.float32)

            result_list.append((ocr_data, coordinates))
        return result_list

    def drawAnnotations(self, file_path: str, csvData: list):
        self.mainUI.progressBar_drawAnnotation.setValue(25)
        images = [tools.read(file_path)]

        if hasattr(self, 'fig') and self.fig:
            plt.close(self.fig)

        self.fig, self.ax = plt.subplots()
        # Clear the previous annotations
        self.ax.clear()

        try:
            for image, predictions in zip(images, [csvData]):
                tools.drawAnnotations(
                    image=image, predictions=predictions, ax=self.ax
                )
                self.mainUI.progressBar_drawAnnotation.setValue(50)
        except Exception as e:
            print(f"Error: {e}")
        
        self.mainUI.progressBar_drawAnnotation.setValue(75)
        canvas = FigureCanvas(self.fig)
        canvas.figure.set_facecolor('#FFFFFF96')

        return canvas
