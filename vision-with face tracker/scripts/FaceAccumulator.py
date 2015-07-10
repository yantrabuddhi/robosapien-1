import cv2, os, re
import numpy as np

# Device ID
deviceID = 0

# Nat sort defn
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

# Get Name
name = raw_input("Enter name: ")
outputPath = "faces/" + name

# Create directory if it doesn't exist
if (not os.path.isdir(outputPath)): os.makedirs(outputPath)

# Get index of last added face
lastIndex = -1
listOfFiles = natural_sort(os.listdir(outputPath))
if len(listOfFiles) > 0:
    lastIndex = int(re.search(r'\d+', listOfFiles[-1]).group())

# Init Webcam and face_haarcascade
capture = cv2.VideoCapture(deviceID)
face_cascade = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")
cv2.waitKey(0)
while (True):
    ret, frame = capture.read()
    if ret:
        cv2.imshow("Frame", frame)
        faces = face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 2)
        cmd = cv2.waitKey(10)
        if len(faces) > 0 and cmd == 1048608:  # Save face to file
            x, y, width, height = faces[0]
            lastIndex += 1
            face = frame[y:y + height, x:x + width]
            face = cv2.resize(face, (150, 150))
            cv2.imwrite(outputPath + "/" + str(lastIndex) + ".jpg", face)
            print "File saved - " + str(lastIndex) + ".jpg"
        elif (cmd == 1048603):
            break

capture.release()
cv2.destroyAllWindows()
