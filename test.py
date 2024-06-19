import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QTableView,
)
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PySide6.QtGui import QStandardItemModel, QStandardItem
import tensorflow as tf
from io import StringIO


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CMD Output")
        self.setGeometry(100, 100, 600, 400)
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        # Load the model
        self.model = tf.keras.applications.MobileNetV2()

        # Display the model summary
        self.show_model_summary()

    def show_model_summary(self):
        # Capture the summary text
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        self.model.summary(print_fn=lambda x: sys.stdout.write(x))
        summary_text = sys.stdout.getvalue()
        sys.stdout = original_stdout
        print(summary_text)
        self.text_edit.setPlainText(summary_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
