import os
from __interface__.ui_mainwindow import Ui_MainWindow
from __interface_control__.circle_progress_bar import CPBar
from database.database import Database
from sklearn.model_selection import train_test_split
from PySide6.QtCore import Qt, QThread, Signal, QObject
from model import *
import numpy as np
import pandas as pd

class TrainThread(QThread):
    progress = Signal(int)
    finished = Signal(float,float)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.x_train = []
        self.y_train = []
        self.x_test = []
        self.y_test = []
        self.metaData = pd.read_csv('metaData/metaData.csv')
        self.model = Model()
        
    def run(self) -> None:
        try:
            self.beginTrain()
        except Exception as e:
            print(f"Error in OCRThread: {str(e)}")

    def beginTrain(self):
        self.x_train, self.y_train, self.x_test, self.y_test = [], [], [], []
        epochCount = self.model.get_epochs()
        
        class TrainingCallback(tf.keras.callbacks.Callback):
            def on_epoch_end(self, epoch, logs=None):
                self.progress.emit((epoch + 1)*epochCount)

        callback = TrainingCallback()
        callback.progress = self.progress
        
        self.scaleData()
        self.splitTrainTest()
        self.reshapeData()
        model = self.model(self.x_train[0].shape)
        model.compile(optimizer='adam', loss='mean_squared_logarithmic_error', metrics=['accuracy'])
        self.model.train(self.x_train,self.y_train,callback)
        model.save("metaData/model.h5")
        acc,loss =self.testModel(model)
        self.finished.emit(acc,loss)

    def scaleData(self):
        a=[]
        for csv_file_name, index in zip(self.metaData['csv_file_name'],self.metaData['index_no']):
            ocrData = pd.read_csv('csv data/'+csv_file_name)
            try:
                ocrData = ocrData.drop(columns=['ocr_data','confident_level'])
            except:
                ocrData = ocrData.drop(columns=['ocr_data'])
            a.append(np.array(ocrData.values.tolist()))
        max_time_steps = max(len(sequence) for sequence in a)
        a = tf.keras.preprocessing.sequence.pad_sequences(
                a, padding="post", maxlen=max_time_steps, dtype="float32"
                )
        max_a = np.max(a)

        for csv_file_name, index in zip(self.metaData['csv_file_name'],self.metaData['index_no']):
            ocrData = pd.read_csv('csv data/'+csv_file_name)
            try:
                ocrData = ocrData.drop(columns=['ocr_data','confident_level'])
            except:
                ocrData = ocrData.drop(columns=['ocr_data'])
            # ocrData = round(ocrData /ocrData.max(),6)

            ocrData['x1'] = round(ocrData['x1']/max_a,6)
            ocrData['y1'] = round(ocrData['y1']/max_a,6)
            ocrData['x2'] = round(ocrData['x2']/max_a,6)
            ocrData['y2'] = round(ocrData['y2']/max_a,6)
            ocrData['x3'] = round(ocrData['x3']/max_a,6)
            ocrData['y3'] = round(ocrData['y3']/max_a,6)
            ocrData['x4'] = round(ocrData['x4']/max_a,6)
            ocrData['y4'] = round(ocrData['y4']/max_a,6)

            self.x_train.append(np.array(ocrData.values.tolist()))
            self.y_train.append(index)

        self.y_train = np.array(self.y_train)
        max_time_steps = max(len(sequence) for sequence in self.x_train)

        self.x_train = tf.keras.preprocessing.sequence.pad_sequences(self.x_train, padding="post", maxlen=max_time_steps, dtype="float32")
        self.progress.emit(5)

    def splitTrainTest(self):
        test_size = 0.2 
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x_train, self.y_train, test_size=test_size, random_state=42) 

    def reshapeData(self):
        (_, DATA_HEIGHT, DATA_WIDTH) = self.x_train.shape
        DATA_CHANNELS = 1

        self.x_train = self.x_train.reshape(self.x_train.shape[0],DATA_HEIGHT,DATA_WIDTH,DATA_CHANNELS)

    def testModel(self,tfModel):
        test_loss, test_acc = tfModel.evaluate(self.x_test,self.y_test)
        return(test_acc, test_loss)
    

class page_training(QObject):
    def __init__(self, mainUI:Ui_MainWindow, db:Database) -> None:
        self.mainUI = mainUI
        self.db = db
        self.prograssCircle = CPBar(self.mainUI.frame_Load)
        self.mainUI.gridLayout_23.addWidget(self.prograssCircle, 4, 0, 1, 5, Qt.AlignHCenter)
        self.qthread = QThread()
        self.train = TrainThread()

        self.train.moveToThread(self.qthread)
        self.qthread.started.connect(self.train.run)
        self.train.progress.connect(self.update_progress)
        self.train.finished.connect(self.train_finished)

        self.loadScreenStats()
        self.mainUI.startTrainBtn.clicked.connect(self.startTrainBtn_clicked)


    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(2)

    def startTrainBtn_clicked(self):
        if not self.qthread.isRunning():
            self.qthread.start()
            self.mainUI.startTrainBtn.setDisabled(True)

    def update_progress(self,epoch):
        print(f'Status: Epoch {epoch}')
        self.prograssCircle.upd(epoch/100)
    
    def train_finished(self,acc,loss):
        self.qthread.quit()
        self.mainUI.startTrainBtn.setEnabled(True)
        acc = round(acc,2)*100
        loss = round(loss,2)*100
        self.mainUI.label_afterTrainAcc.setText(str(acc)+"%")
        self.mainUI.label_afterTrainLoss.setText(str(loss)+"%")
        
    def loadScreenStats(self):
        files = os.listdir("csv data")
        self.mainUI.label_NoofInvoicestoTrain.setText(str(len(files)))
        
    
    