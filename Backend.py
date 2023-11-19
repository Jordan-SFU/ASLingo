# Imports
import cv2
import mediapipe as mp
import numpy as np
import time

# Mediapipe setup
mp_holistic = mp.solutions.holistic # Holistic model
mp_draw = mp.solutions.drawing_utils # Drawing utilities

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
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while(cap):
        ret, frame = cap.read()
        

        # Make detections
        image, results = mediapipe_detection(frame, holistic)

        # Draw landmarks
        #mp_draw.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS) # Face connections
        mp_draw.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Pose connections
        mp_draw.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Left hand connections
        mp_draw.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Right hand connections

        cv2.imshow('frame', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break