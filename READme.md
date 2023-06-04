<h2> Screenshots and Recording Samples </h2>

### 'Screen Recording Sample'
[label](https://github.com/anubhabguha1999/Mouth-Recognition-Assignment/assets/96384072/aae83dc6-dde4-418b-963c-6ff6935a610e)

### 'Screensort Sample 1'
![Screenshot 1](https://github.com/anubhabguha1999/Mouth-Recognition-Assignment/assets/96384072/37cb9342-a73d-4274-8167-371c380b1c76)

### 'Screensort Sample 1'
![Screenshot 2](https://github.com/anubhabguha1999/Mouth-Recognition-Assignment/assets/96384072/feade7e9-ed9c-4005-8cce-9a0dd5f83a03)

<h2> My Approach </h2>

My approach to this program will be to use a pretrained model called "shape_predictor_68_face_landmarks.dat" as it contains many pretrained Facial Landmark Detection
Next, I need to read the frame and then convert the frame to grayscale for facial landmark detection
Then I setup the filters and the red dots for the UpperLips and the Lower Lips
Then passed a contion that if the length exceeds more than 30 then it should apply the filter 
At the last I implemented a "Quit" Structure where if the user presses 'c' then both the program and the terminal will close.