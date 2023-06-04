My approach to this program will be to use a pretrained model called "shape_predictor_68_face_landmarks.dat" as it contains many pretrained Facial Landmark Detection
# Next, I need to read the frame and then convert the frame to grayscale for facial landmark detection
# Then I setup the filters and the red dots for the UpperLips and the Lower Lips
# Then passed a contion that if the length exceeds more than 30 then it should apply the filter 
# At the last I implemented a "Quit" Structure where if the user presses 'c' then both the program and the terminal will close.
