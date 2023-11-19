import cv2
import os
import time

# Program that prompts the user with an ASL word, and saves a frame every 0.5 seconds 
# to a new directory for each word

# each word has multiple parts

# dictionary containing each word, and number of parts
words = {"hello": 2, "goodbye": 2, "please": 1, "thank you": 2, "yes": 2, "no": 2}

# create a new directory for each word in "data" folder
# if the word has multiple parts, create a new directory for each part
try:
    for word in words:
        if words[word] > 1:
            for i in range(1, words[word]):
                os.mkdir("data/" + word + str(i))
        else:
            os.mkdir("data/" + word)
except OSError:
    pass

# Get results from frame
def mediapipe_detection(image, model):
    # Convert image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False # To improve performance
    results = model.process(image) # Make detections
    image.flags.writeable = True # To improve performance
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # Convert back to BGR
    return image, results

# Function for reading frames
cap = cv2.VideoCapture(0)

# iterate through each word and word part
for word in words:
    for i in range(1, words[word] + 1):
        time.sleep(5)
        print("Please sign " + word + " " + str(i))
        # iterate through each frame
        for j in range(1, 21):
            time.sleep(1)
            # Get webcam feed
            ret, frame = cap.read()

            # Show to screen
            cv2.imshow('frame', frame)

            # Save frame every second
            cv2.imwrite("data/" + word + str(i) + "/" + word + str(i) + "-" + str(j) + ".jpg", frame)

            # Break loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break