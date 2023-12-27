
from PySide6.QtSql import QSqlDatabase

class Database:
    def __init__(self) -> None:
        self.db_host_name = 'localhost'     
        self.db_name = 'invoice_number_mining'     
        self.db_user_name = 'root'     
        self.db_password = ''     
        self.db = QSqlDatabase.addDatabase("QMYSQL")   

    def get_db_host_name(self) -> str:
        return self.db_host_name

    def set_db_host_name(self, value) -> None:
        self.db_host_name = value

    def get_db_name(self) -> str:
        return self.db_name

    def set_db_name(self, value) -> None:
        self.db_name = value

    def get_db_user_name(self) -> str:
        return self.db_user_name

    def set_db_user_name(self, value) -> None:
        self.db_user_name = value

    def get_db_password(self) -> str:
        return self.db_password

    def set_db_password(self, value) -> None:
        self.db_password = value

    def connect(self) -> None:
        self.db.setHostName(self.db_host_name)
        self.db.setDatabaseName(self.db_name)
        self.db.setUserName(self.db_user_name)
        self.db.setPassword(self.db_password)
        self.db.open()

    def close(self):
        self.db.close()
        