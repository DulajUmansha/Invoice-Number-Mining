import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt

# Specify the paths to the YOLO files
weights_path = "C:/Users/dulaj/Downloads/archive (1)/lapi.weights"
config_path = "C:/Users/dulaj/Downloads/archive (1)/darknet-yolov3.cfg"
coco_names_path = "C:/Users/dulaj//Downloads/archive (1)/classes.names"

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# Load YOLO
net = cv2.dnn.readNet(weights_path, config_path)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load the labels
with open(coco_names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load image
img = cv2.imread(
    "C:/Users/dulaj/Downloads/WhatsApp Image 2024-07-04 at 10.53.28_685c20ad.jpg"
)
height, width, channels = img.shape

# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# Showing information on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Draw bounding box
font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = (0, 255, 0)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y - 5), font, 1, color, 1)

        # Crop the detected number plate
        number_plate = img[y : y + h, x : x + w]

        # Perform OCR on the number plate
        number_plate_text = pytesseract.image_to_string(number_plate, config="--psm 8")
        print("Detected Number Plate Text:", number_plate_text)

        print(data)

# Display the output using Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
