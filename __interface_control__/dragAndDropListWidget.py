from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import QListWidgetItem


class dragAndDropListWidget(QtWidgets.QListWidget):
    fileDropped = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(dragAndDropListWidget, self).__init__(parent)
    
        self.setAcceptDrops(True)
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.setIconSize(QtCore.QSize(self.size()))
        self.setResizeMode(QtWidgets.QListView.Adjust)
        self.setStyleSheet("QListWidget { background-color: rgba(66, 66, 66, 0); color: white; }")

    def enableDragAndDrop(self, enable=True):
        self.setAcceptDrops(enable)

    def getItem(self):
        return self.item(0).text()
    
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = [url.toLocalFile() for url in event.mimeData().urls()]
            self.fileDropped.emit(links)
            if self.count():
                self.enableDragAndDrop(False)
        else:
            event.ignore()

    def clearList(self):
        self.clear()
        self.enableDragAndDrop(True)
