from __interface__.ui_mainwindow import Ui_MainWindow
from database.database import Database
from PySide6.QtWidgets import QStyledItemDelegate, QHeaderView
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

from database.tbl_extracedinvoice import tbl_extraced_invoice

class ImageDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == 0:
            image_path = index.data(Qt.DisplayRole)
            pixmap = QPixmap(image_path)

            if pixmap.isNull():
                # If the pixmap failed to load, display an empty placeholder
                pixmap = QPixmap(100, 100)
                pixmap.fill(Qt.lightGray)
            else:
                pixmap = pixmap.scaled(100,100, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Calculate the rect to center the image within the cell
            rect = option.rect
            pixmap_rect = pixmap.rect()
            pixmap_rect.moveCenter(rect.center())

            # Draw the pixmap
            painter.drawPixmap(pixmap_rect.topLeft(), pixmap)
        else:
            super().paint(painter, option, index)

class TableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return 2  # We have two columns: image and image name

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = self._data[index.row()]
            if index.column() == 0:
                return ("Extracted/Invoices/"+row['image_name'])
            elif index.column() == 1:
                return row['invo_no']
            
        elif role == Qt.TextAlignmentRole:
            column = index.column()
            if column in [0,1]:
                return Qt.AlignHCenter | Qt.AlignVCenter
            else:  # Default alignment for other columns
                return Qt.AlignLeft | Qt.AlignVCenter
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return ["Invoice", "Invoice Number"][section]
            else:
                return f"Row {section + 1}"
        return None
    
class page_extractHistory:
    def __init__(self, mainUI: Ui_MainWindow, db: Database) -> None:
        self.mainUI = mainUI
        self.db = db
        self.imageNames = []

        self.mainUI.extractHistoryBackBtn.clicked.connect(self.extractHistoryBackBtn_clicked)

    def stackedBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(7)
        self.getDataFromDB()

    def extractHistoryBackBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(1)

    def getDataFromDB(self):
        self.db.connect()
        tbl_extracedInvoice = tbl_extraced_invoice()
        tbl_extracedInvoice.set_columnFilter(["invo_no","image_name"])
        data = tbl_extracedInvoice.retriveData()
        self.mainUI.tableView_extractedHistory.clearMask()
        self.model = TableModel(data)
        self.mainUI.tableView_extractedHistory.setModel(self.model)

        self.delegate = ImageDelegate()
        self.mainUI.tableView_extractedHistory.setItemDelegate(self.delegate)
        self.mainUI.tableView_extractedHistory.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainUI.tableView_extractedHistory.verticalHeader().setDefaultSectionSize(100)
        self.db.close()