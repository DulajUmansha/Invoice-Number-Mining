
from database.table import Table

class tbl_ocr_data(Table):
	def __init__(self) -> None:
		super(tbl_ocr_data,self).__init__()
		self.tableName = 'tbl_ocr_data' #self.__class__.__name__
		self.id = None
		self.invo_no = None
		self.csv_file_name = None
		self.file_path = None
		self.date_time = None
		self.status = None
		
	def get_id(self):
		return self.id

	def set_id(self,value):
		self.id = value

	def get_invo_no(self):
		return self.invo_no

	def set_invo_no(self,value):
		self.invo_no = value

	def get_csv_file_name(self):
		return self.csv_file_name

	def set_csv_file_name(self,value):
		self.csv_file_name = value

	def get_file_path(self):
		return self.file_path

	def set_file_path(self,value):
		self.file_path = value

	def get_date_time(self):
		return self.date_time

	def set_date_time(self,value):
		self.date_time = value

	def get_status(self):
		return self.status

	def set_status(self,value):
		self.status = value

	def retriveData(self):
		self.set_tableName(self.tableName)
		return super().retriveData()

	def insertData(self, table=None,db = None, *args, **data) -> bool:
		self.set_tableName(self.tableName)
		data = {'id':self.id,'invo_no':self.invo_no,'csv_file_name':self.csv_file_name,'file_path':self.file_path,'date_time':self.date_time,'status':self.status}
		data = {k: v for k, v in data.items() if v is not None}
		return super().insertData(table, db=db, *args, **data)

	def updateData(self, table=None, where=None, *args, **data) -> bool:
		self.set_tableName(self.tableName)
		return super().updateData(table, where, *args, **data)
