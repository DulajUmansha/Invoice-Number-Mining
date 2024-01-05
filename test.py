import sys
from PySide6.QtCore import QThread, Qt
from PySide6.QtWidgets import QApplication
from database.database import Database

class MyThread(QThread):
    def __init__(self, db:Database):
        super().__init__()
        self.db = db

    def run(self):
        self.db.connect()
        # Perform operations in the thread using the database
        # ...
        self.db.close()

def main():
    app = QApplication(sys.argv)

    # Create a database object in the main thread
    main_thread_db = Database("main_thread_connection")
    main_thread_db.connect()
    # Perform operations in the main thread using the database
    # ...
    main_thread_db.close()
    main_thread_db.removeDatabase("main_thread_connection")

    # Create a QThread and move the other database object to the thread
    thread_db = Database("qthread_connection")
    thread_db.connect()

    my_thread = MyThread(thread_db)
    my_thread.start()
    my_thread.wait()

    thread_db.close()
    thread_db.removeDatabase("qthread_connection")

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
