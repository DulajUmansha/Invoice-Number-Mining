from PIL import Image
import pytesseract

# Path to the Tesseract executable (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your image file
image_path = r"C:\Users\dulaj\Downloads\invoices\IMG-20231016-WA0006.jpg"

# Perform OCR on the image
def ocr_image(image_path):
    try:
        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_path)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)

        # Print the extracted text
        print("Extracted Text:")
        print(text)

    except Exception as e:
        print(f"Error: {e}")

# Perform OCR on the specified image
ocr_image(image_path)
