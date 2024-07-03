from database.table import Table

class tbl_extraced_invoice(Table):
	def __init__(self) -> None:
		super(tbl_extraced_invoice,self).__init__()
		self.tableName = 'tbl_extracedinvoice' #self.__class__.__name__
		self.extracedInvoiceID = None
		self.invo_no = None
		self.ocr_csv_file_name = None
		self.image_name = None
		self.date_time = None
		self.status = None
		
	def get_extracedInvoiceID(self):
		return self.extracedInvoiceID

	def set_extracedInvoiceID(self,value):
		self.extracedInvoiceID = value

	def get_invo_no(self):
		return self.invo_no

	def set_invo_no(self,value):
		self.invo_no = value

	def get_ocr_csv_file_name(self):
		return self.ocr_csv_file_name

	def set_ocr_csv_file_name(self,value):
		self.ocr_csv_file_name = value

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
			if 'extracedInvoiceID' in result:
				self.extracedInvoiceID = result['extracedInvoiceID']
			if 'invo_no' in result:
				self.invo_no = result['invo_no']
			if 'ocr_csv_file_name' in result:
				self.ocr_csv_file_name = result['ocr_csv_file_name']
			if 'image_name' in result:
				self.image_name = result['image_name']
			if 'date_time' in result:
				self.date_time = result['date_time']
			if 'status' in result:
				self.status = result['status']
		elif type(result) == list:
			extracedInvoiceIDList = []
			invo_noList = []
			ocr_csv_file_nameList = []
			image_nameList = []
			date_timeList = []
			statusList = []
			for i in result:
				if 'extracedInvoiceID' in i:
					extracedInvoiceIDList.append(i['extracedInvoiceID'])
				if 'invo_no' in i:
					invo_noList.append(i['invo_no'])
				if 'ocr_csv_file_name' in i:
					ocr_csv_file_nameList.append(i['ocr_csv_file_name'])
				if 'image_name' in i:
					image_nameList.append(i['image_name'])
				if 'date_time' in i:
					date_timeList.append(i['date_time'])
				if 'status' in i:
					statusList.append(i['status'])
			self.extracedInvoiceID = extracedInvoiceIDList
			self.invo_no = invo_noList
			self.ocr_csv_file_name = ocr_csv_file_nameList
			self.image_name = image_nameList
			self.date_time = date_timeList
			self.status = statusList
		return result

	def insertData(self, table=None, *args, **data) -> bool:
		self.set_tableName(self.tableName)
		data = {'extracedInvoiceID':self.extracedInvoiceID,'invo_no':self.invo_no,'ocr_csv_file_name':self.ocr_csv_file_name,'image_name':self.image_name,'date_time':self.date_time,'status':self.status}|data
		data = {k: v for k, v in data.items() if v is not None}
		return super().insertData(table, *args, **data)

	def updateData(self, table=None, where=None, *args, **data) -> bool:
		self.set_tableName(self.tableName)
		data = {'extracedInvoiceID':self.extracedInvoiceID,'invo_no':self.invo_no,'ocr_csv_file_name':self.ocr_csv_file_name,'image_name':self.image_name,'date_time':self.date_time,'status':self.status}|data
		data = {k: v for k, v in data.items() if v is not None}
		return super().updateData(table, where, *args, **data)
