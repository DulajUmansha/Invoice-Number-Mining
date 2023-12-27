import csv
from PySide6.QtCore import QDateTime, Qt

class CSVfile:
    def __init__(self) -> None:
        pass

    def write(self, allData: list):
        for data in allData:
            print(data[-1])
            csvfile = open("csv data/" + data[-1], "w", newline="")
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(
                ["ocr_data", "X1", "Y1", "X2", "Y2", "X3", "Y3", "X4", "Y4"]
            )
            for row in data[1:-2]:
                csvwriter.writerow(row)

    def formatData(self, invoNoList: list, invoOCRDataList: list, invoURLList: list, fileNames:list):
        allData = []
        for invoNo, ocr_data, url, fileName in zip(invoNoList, invoOCRDataList, invoURLList, fileNames):
            data = []
            data.append(invoNo)
            for label, coord_list in ocr_data:
                row = [label]
                for coords in coord_list:
                    row.extend(coords)
                data.append(row)
            data.append(url)
            data.append(fileName)
            allData.append(data)
        return allData
    
    def generateFileName(self):
        currentDateTime = QDateTime.currentDateTime()
        currentTime = currentDateTime.time()
        milliseconds = currentTime.msec()
        milliseconds_str = f"{milliseconds:03d}"
        time_str = currentTime.toString("hhmmss")
        file_name = f"ocr_{currentDateTime.date().toString(Qt.ISODate)}_{time_str}_{milliseconds_str}.csv"
        file_name = file_name.replace("-", "").replace(":", "")

        return file_name
