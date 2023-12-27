 
from PySide6.QtSql import  QSqlQueryModel

class View:
    def __init__(self):
        self.query = None

    def model(self):
        self.queryModel = QSqlQueryModel()
        self.queryModel.setQuery(self.query)
        return self.queryModel
    
    def get_query(self):
        return self.query

    def set_query(self, value):
        self.query = value
        