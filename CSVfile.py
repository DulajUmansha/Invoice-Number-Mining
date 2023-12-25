import os.path
import csv


class CSVfile:
    def __init__(self) -> None:
        if os.path.exists("ocrData.csv"):
            self.create()

    def create(self):
        file = open("ocrData.csv", "w")
        file.write("ocr_data,X1,Y1,X2,Y2,X3,Y3,X4,Y4\n")
        file.close()

    def write(self):
        pass

    def append(self, allData: list):
        for data in allData:
            csvfile = open("csv data/" + data[0] + ".csv", "w", newline="")
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(
                ["ocr_data", "X1", "Y1", "X2", "Y2", "X3", "Y3", "X4", "Y4"]
            )
            for row in data[1:]:
                csvwriter.writerow(row)

    def clear(self):
        pass

    def formatData(self, invoNoList: list, invoOCRDataList: list):
        allData = []
        for invoNo, label_list in zip(invoNoList, invoOCRDataList):
            data = []
            data.append(invoNo)
            for label, coord_list in label_list:
                row = [label]
                for coords in coord_list:
                    row.extend(coords)
                data.append(row)
            allData.append(data)
        return allData
