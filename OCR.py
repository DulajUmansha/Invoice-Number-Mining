import easyocr
import pandas as pd

class OCR:
  def __init__(self):
    self.reader = easyocr.Reader(['en'], gpu=False,)

  def read(self,image):
    result = self.reader.readtext(image)
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['ocr_data', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'confident_level'])

    # Append each detection to the DataFrame
    for detection in result:
        points = detection[0]
        text = detection[1]
        confident_level = detection[2]

        # Extract x, y coordinates
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        x4, y4 = points[3]

        # Create a temporary DataFrame for the current detection
        temp_df = pd.DataFrame({'ocr_data': [text], 'x1': [x1], 'y1': [y1], 'x2': [x2], 'y2': [y2], 'x3': [x3], 'y3': [y3],
                                'x4': [x4], 'y4': [y4], 'confident_level': [confident_level]})

        # Concatenate the temporary DataFrame with the main DataFrame
        df = pd.concat([df, temp_df], ignore_index=True)
    return df