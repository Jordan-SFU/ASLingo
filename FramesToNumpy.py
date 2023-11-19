# Program for converting images into landmark numpy arrays

# Imports
import os
import numpy as np
import cv2
import mediapipe as mp

# Path to dataset
DATADIR = "data"

# Mediapipe setup
mp_holistic = mp.solutions.holistic # Holistic model

# run mediapipe to convert images to landmark numpy arrays

# Pose Landmarks: 33
def poseToNumpy(word, image):
    img = cv2.imread(DATADIR + "/" + word + "/" + image)

    # Convert image to RGB
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        pass

    # Convert image to landmark numpy array
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        results = holistic.process(img)

        # Convert landmarks to numpy array
        landmarks = np.array([[res.x, res.y, res.z] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*3)

        # Return landmarks
        return landmarks
    
# Hand Landmarks: 21
def handsToNumpy(word, image):
    img = cv2.imread(DATADIR + "/" + word + "/" + image)

    # Convert image to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert image to landmark numpy array
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        results = holistic.process(img)

        # Convert landmarks to numpy array
        landmarks = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        landmarks = np.concatenate((landmarks, np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)), axis=0)

        # Return landmarks
        return landmarks
    
def landmarkArray(pose, hands):
    return np.concatenate((pose, hands), axis=0)