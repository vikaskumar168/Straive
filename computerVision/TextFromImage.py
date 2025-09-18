import cv2
from PIL import  Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# print(pytesseract.image_to_string(Image.open('textimg.jpg')))

# video = cv2.VideoCapture("textVid.mp4")
#
# while True:
#     ret, frame = video.read()
#     if not ret:
#         print("Failed to grab frame")
#         break
#
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#
#     _,thresholded = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#
#     text = pytesseract.image_to_string(Image.fromarray(thresholded),config='--psm 11').strip()
#     if text:
#         print("Detected Text: ",text)
#
#         cv2.imshow('OCR',frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# video.release()
# cv2.destroyAllWindows()

image_path = "test-image-for-recognition.png"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
else:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    pil_image = Image.fromarray(gray)
    text = pytesseract.image_to_string(pil_image)
    print("Text extracted from Image: \n",text)

    cv2.imshow("Image ",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


