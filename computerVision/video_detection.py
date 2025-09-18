import time

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


video = cv2.VideoCapture('peopleClapping.mp4')
# video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    frame = cv2.resize(frame,(960,540))

    cv2.imshow("Face Detection",frame)
    print("Frame shape:", frame.shape)
    print("Faces detected:", len(faces))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


# check, frame = video.read()
# time.sleep(3)
#
# if check:
#     cv2.imshow('capturing',frame)
#
#
#     cv2.waitKey(0)
# else:
#     print("Not able to Extract Frame!")
#
# print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(video.get(cv2.CAP_PROP_FRAME_COUNT))
#
# video.release()
# cv2.destroyAllWindows()

