from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage

def sendmails(k):
    msg = EmailMessage()
    msg['From'] = 'rkatoch2017@gmail.com'
    msg['To'] = 'aryasagar123456@gmail.com'
    msg['Subject'] = 'Email with multiple image attachments'

    # Attach the first image
    with open(k, 'rb') as f:
        img_data = f.read()
    img = MIMEImage(img_data, name=k)
    msg.add_attachment(img)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('rkatoch2017@gmail.com', 'qwupmcgvbmvcusif')
    smtp.send_message(msg)
    smtp.quit()

# Initialize the video capture from a webcam
cap = cv2.VideoCapture(1)
cap.set(3, 1000)  # 1280
cap.set(4, 720)   # 720

model = YOLO("yolov8n.pt")

v = 1
output_image_counter = 1

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

zone_x1, zone_y1, zone_x2, zone_y2 = 0, 0, 1280, 720  # Adjust dimensions as needed

detected_ids = set()

prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    people_count = 0

    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

            if "person" == classNames[cls]:
                people_count = people_count + 1

    if people_count == 1 and v == 1:
        ret, frame = cap.read()
        img_name = f"output_{output_image_counter}.png"
        cv2.imwrite(img_name, frame)
        output_image_counter += 1
        v = 0
        sendmails(img_name)

    count_text = f'People Count: {people_count}'
    cv2.putText(img, count_text, (zone_x1, zone_y2 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.rectangle(img, (zone_x1, zone_y1), (zone_x2, zone_y2), (0, 0, 255), 2)
    cv2.putText(img, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()