import cv2


# img = cv2.imread("1.png",1)
img = cv2.imread("bill.png",1)
print(img)
print(cv2.imshow("bill",img))
cv2.waitKey(0)
# cv2.destroyAllWindows()

# bg_img = cv2.imread("1.png",0)
bg_img = cv2.imread("bill.png",0)
print(bg_img)
print(cv2.imshow("bill",bg_img))
cv2.waitKey(0)
cv2.destroyAllWindows()


face_cascade = cv2.CascadeClassifier('cascade_frontface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray_img)

# faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.2,minNeighbors=5)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()