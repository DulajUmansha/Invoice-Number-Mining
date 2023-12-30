import keras_ocr

class OCR:
    def __init__(self) -> None:
        try:
            self.pipeline = keras_ocr.pipeline.Pipeline()
        except Exception as e:
            print(f"Error initializing OCR pipeline: {e}")
    

    def read(self,imageList:list):
        try:
            images = [
                keras_ocr.tools.read(url)
                for url in imageList
            ]

            prediction_groups = self.pipeline.recognize(images)

            return prediction_groups
        
        except Exception as e:
            print(f"Error during OCR processing: {e}")
            return None