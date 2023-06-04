# My approach to this program will be to use a pretrained model called "shape_predictor_68_face_landmarks.dat" as it contains many pretrained Facial Landmark Detection
# Next, I need to read the frame and then convert the frame to grayscale for facial landmark detection
# Then I setup the filters and the red dots for the UpperLips and the Lower Lips
# Then passed a contion that if the length exceeds more than 30 then it should apply the filter 
# At the last I implemented a "Quit" Structure where if the user presses 'c' then both the program and the terminal will close.

# INSTALL THE DEPENDENCIES

# pip install opencv-python
# pip install dlib
# pip install numpy


import cv2
import dlib
import numpy as np

# loading the pretrained Facial Landmark Detection
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


faceCapture = cv2.VideoCapture(0)
#applying the filter
filter = np.zeros((480, 640, 3), np.uint8)

filter[:, :] = (0, 0, 255)

while True:
    ret, frame = faceCapture.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = dlib.get_frontal_face_detector()(gray)

    for face in faces:
        gMark = predictor(gray, face)

        # Coordinates of the Lips
        upperlipMarker = (gMark.part(51).x, gMark.part(51).y)
        lowerlipMarker = (gMark.part(57).x, gMark.part(57).y)

        distanceOfLips = np.linalg.norm(np.array(upperlipMarker) - np.array(lowerlipMarker))
        # if distance is greater than 30 then apply the filter 
        if distanceOfLips > 30: 
            frame = cv2.addWeighted(frame, 0.7, filter, 0.3, 0)


        # Red Dots on the Upper and the Lower Lips
        cv2.circle (frame, upperlipMarker, 5, (0, 0, 255), -1)
        cv2.circle (frame, lowerlipMarker, 5, (0, 0, 255), -1)


    #Camera Module
    cv2.imshow('CAMERA MODULE for Mouth Recognition', frame)




    # press 'c' to quit command
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break



#finishing commands
faceCapture.release()
cv2.destroyAllWindows()
