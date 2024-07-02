from database.table import Table

class tbl_ocr_data(Table):
	def __init__(self) -> None:
		super(tbl_ocr_data,self).__init__()
		self.tableName = 'tbl_ocr_data' #self.__class__.__name__
		self.id = None
		self.index_no = None
		self.invo_no = None
		self.csv_file_name = None
		self.image_name = None
		self.date_time = None
		self.status = None
		
	def get_id(self):
		return self.id

	def set_id(self,value):
		self.id = value

	def get_index_no(self):
		return self.index_no

	def set_index_no(self,value):
		self.index_no = value

	def get_invo_no(self):
		return self.invo_no

	def set_invo_no(self,value):
		self.invo_no = value

	def get_csv_file_name(self):
		return self.csv_file_name

	def set_csv_file_name(self,value):
		self.csv_file_name = value

	def get_image_name(self):
		return self.image_name

	def set_image_name(self,value):
		self.image_name = value

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
		result = super().retriveData()
		if result == {}: return result
		if type(result) == dict:
			if 'id' in result:
				self.id = result['id']
			if 'index_no' in result:
				self.index_no = result['index_no']
			if 'invo_no' in result:
				self.invo_no = result['invo_no']
			if 'csv_file_name' in result:
				self.csv_file_name = result['csv_file_name']
			if 'image_name' in result:
				self.image_name = result['image_name']
			if 'date_time' in result:
				self.date_time = result['date_time']
			if 'status' in result:
				self.status = result['status']
		elif type(result) == list:
			idList = []
			index_noList = []
			invo_noList = []
			csv_file_nameList = []
			image_nameList = []
			date_timeList = []
			statusList = []
			for i in result:
				if 'id' in i:
					idList.append(i['id'])
				if 'index_no' in i:
					index_noList.append(i['index_no'])
				if 'invo_no' in i:
					invo_noList.append(i['invo_no'])
				if 'csv_file_name' in i:
					csv_file_nameList.append(i['csv_file_name'])
				if 'image_name' in i:
					image_nameList.append(i['image_name'])
				if 'date_time' in i:
					date_timeList.append(i['date_time'])
				if 'status' in i:
					statusList.append(i['status'])
			self.id = idList
			self.index_no = index_noList
			self.invo_no = invo_noList
			self.csv_file_name = csv_file_nameList
			self.image_name = image_nameList
			self.date_time = date_timeList
			self.status = statusList
		return result

	def insertData(self, table=None, *args, **data) -> bool:
		self.set_tableName(self.tableName)
		data = {'id':self.id,'index_no':self.index_no,'invo_no':self.invo_no,'csv_file_name':self.csv_file_name,'image_name':self.image_name,'date_time':self.date_time,'status':self.status}|data
		data = {k: v for k, v in data.items() if v is not None}
		return super().insertData(table, *args, **data)

	def updateData(self, table=None, where=None, *args, **data) -> bool:
		self.set_tableName(self.tableName)
		data = {'id':self.id,'index_no':self.index_no,'invo_no':self.invo_no,'csv_file_name':self.csv_file_name,'image_name':self.image_name,'date_time':self.date_time,'status':self.status}|data
		data = {k: v for k, v in data.items() if v is not None}
		return super().updateData(table, where, *args, **data)
