import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath =  sys.argv[2] # "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=4,    
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

eyes = []
img = image
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

print("Found {0} faces!".format(len(faces)))
print("Found {0} eyes!".format(len(eyes)))


# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# cv2.imshow("Faces found", image)
cv2.imwrite(imagePath + "_processed.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
