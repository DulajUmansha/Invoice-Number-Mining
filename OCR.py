import keras_ocr

class OCR:
    def __init__(self) -> None:
        self.pipeline = keras_ocr.pipeline.Pipeline()
    

    def read(self,imageList:list):
        print(imageList)
        images = [
            keras_ocr.tools.read(url)
            for url in imageList
        ]

        prediction_groups = self.pipeline.recognize(images)

        return prediction_groups