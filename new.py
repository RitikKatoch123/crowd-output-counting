# from ultralytics import YOLO
# import cv2
# import cvzone
# import math
# import time
#
# from email.message import EmailMessage
# import ssl
# import smtplib
#
# #
# # def sendmails():
# #
# #     email_sender = 'ng.niesh123@gmail.com'
# #     email_password = "kkne ubdb tjjf fgqh"
# #     email_receiver = "rkatoch2017@gmail.com"
# #
# #     subject = ' crowd is overlimit'
# #     body = """
# # Dear [Recipient's Name],
# #
# # I hope this message finds you well. We would like to inform you that our crowd
# #  monitoring system has detected an excess of people at phagwara junction at 10:23pm.
# # This situation requires immediate attention and monitoring.
# #
# #
# # Sincerely,
# # [team xyz]
# #
# #
# #
# #
# #     """
# #
# #     em = EmailMessage()
# #     em['From'] = email_sender
# #     em['To'] = email_receiver
# #     em['Subject'] = subject
# #     em.set_content(body)
# #
# #     context = ssl.create_default_context()
# #     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
# #         smtp.login(email_sender, email_password)
# #         smtp.sendmail(email_sender, email_receiver, em.as_string())
# #
# #
#
# def sendmails():
#     email_sender = 'ng.niesh123@gmail.com'
#     email_password = "kkne ubdb tjjf fgqh"
#     email_receivers = ["rkatoch2017@gmail.com",  "aryasagar123456@gmail.com"]
#
#     subject = 'Crowd is overlimit'
#     body = """
#     Dear [Recipient's Name],
#
#     I hope this message finds you well. We would like to inform you that our crowd
#     monitoring system has detected an excess of people at Phagwara Junction at 10:23 PM.
#     This situation requires immediate attention and monitoring.
#
#     Sincerely,
#     [Team XYZ]
#     """
#
#     for email_receiver in email_receivers:
#         em = EmailMessage()
#         em['From'] = email_sender
#         em['To'] = email_receiver
#         em['Subject'] = subject
#         em.set_content(body)
#
#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#             smtp.login(email_sender, email_password)
#             smtp.sendmail(email_sender, email_receiver, em.as_string())
#
#
#
#
#
#
#
#
#
#
#
#
# # Initialize the video capture from a file or webcam
# cap =cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
#
# # cap = cv2.VideoCapture("people1.mp4")
# # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# # # Create an OpenCV window with the same size as the video
# # cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
# # cv2.resizeWindow("Image", width, height)
#
# # Load the YOLO model
# model = YOLO("crowds.pt")
#
# v=int(1)
#
# # Define class names
# classNames = ['people']
#
# # Define the counting zone coordinates to cover the entire interface
# zone_x1, zone_y1, zone_x2, zone_y2 = 0, 0, 1920, 1080  # Adjust dimensions as needed
#
# # Initialize the people count
#
# detected_ids = set()
#
# # Initialize time variables for FPS calculation
# prev_frame_time = 0
# new_frame_time = 0
#
# while True:
#     new_frame_time = time.time()
#     success, img = cap.read()
#     people_count = 0
#
#     # Perform object detection with YOLO
#     results = model(img, stream=True)
#
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             # Bounding Box
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#
#             # Check if the detected object is a person and within the counting zone
#
#             # Draw bounding box and label
#             w, h = x2 - x1, y2 - y1
#             cvzone.cornerRect(img, (x1, y1, w, h))
#             conf = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
#
#
#             people_count = people_count + 1
#
#
#     # Display people count in the counting zone
#     if (people_count==20 and v==1):
#         v=0
#         sendmails()
#
#
#
#
#     count_text = f'People Count: {people_count}'
#     cv2.putText(img, count_text, (zone_x1, zone_y2 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#
#     # Draw the counting zone rectangle
#     cv2.rectangle(img, (zone_x1, zone_y1), (zone_x2, zone_y2), (0, 0, 255), 2)
#
#     # Display the people count in the frame
#     cv2.putText(img, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#
#
#
#
#
#     cv2.imshow("Image", img)
#
#     # Exit the loop if 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the video capture and close OpenCV windows
# cap.release()
# cv2.destroyAllWindows()






from ultralytics import YOLO
import cv2
import cvzone
import math
import time

from email.message import EmailMessage
import ssl
import smtplib

#
# def sendmails():
#
#     email_sender = 'ng.niesh123@gmail.com'
#     email_password = "kkne ubdb tjjf fgqh"
#     email_receiver = "rkatoch2017@gmail.com"
#
#     subject = ' crowd is overlimit'
#     body = """
# Dear [Recipient's Name],
#
# I hope this message finds you well. We would like to inform you that our crowd
#  monitoring system has detected an excess of people at phagwara junction at 10:23pm.
# This situation requires immediate attention and monitoring.
#
#
# Sincerely,
# [team xyz]
#
#
#
#
#     """
#
#     em = EmailMessage()
#     em['From'] = email_sender
#     em['To'] = email_receiver
#     em['Subject'] = subject
#     em.set_content(body)
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(email_sender, email_password)
#         smtp.sendmail(email_sender, email_receiver, em.as_string())
#
#

#def sendmails():
 #   email_sender = 'ng.niesh123@gmail.com'
 #   email_password = "kkne ubdb tjjf fgqh"
  #  email_receivers = ["rkatoch2017@gmail.com",  "aryasagar123456@gmail.com"]

   # subject = 'Crowd is overlimit'
   # body = """
   # Dear [Recipient's Name],

    #I hope this message finds you well. We would like to inform you that our crowd
    #monitoring system has detected an excess of people at Phagwara Junction at 10:23 PM.
    #This situation requires immediate attention and monitoring.

    #Sincerely,
    #[Team XYZ]
   # """

   # for email_receiver in email_receivers:
    #    em = EmailMessage()
     #   em['From'] = email_sender
     #   em['To'] = email_receiver
      #  em['Subject'] = subject
      #  em.set_content(body)

       # context = ssl.create_default_context()
       # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
          #  smtp.login(email_sender, email_password)
          #  smtp.sendmail(email_sender, email_receiver, em.as_string())












# Initialize the video capture from a file or webcam
cap =cv2.VideoCapture(0)
cap.set(3, 1800)
cap.set(4, 720)

# cap = cv2.VideoCapture("people.mp4")
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Create an OpenCV window with the same size as the video
# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Image", width, height)

# Load the YOLO model
model = YOLO("yolov8n.pt")

v=int(1)

# Define class names
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

# Define the counting zone coordinates to cover the entire interface
zone_x1, zone_y1, zone_x2, zone_y2 = 0, 0, 1920, 1080  # Adjust dimensions as needed

# Initialize the people count

detected_ids = set()

# Initialize time variables for FPS calculation
prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    people_count = 0

    # Perform object detection with YOLO
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Check if the detected object is a person and within the counting zone

            # Draw bounding box and label
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

            if "person" == classNames[cls]:
                people_count = people_count + 1


    # Display people count in the counting zone
    #if (people_count==4 and v==1):
     #   v=0
      #  sendmails()




   # count_text = f'People Count: {people_count}'
   # cv2.putText(img, count_text, (zone_x1, zone_y2 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Draw the counting zone rectangle
    cv2.rectangle(img, (zone_x1, zone_y1), (zone_x2, zone_y2), (0, 0, 255), 2)

    # Display the people count in the frame
  #  cv2.putText(img, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)





    cv2.imshow("Image", img)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()