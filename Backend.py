# Imports
import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import base64

# Mediapipe setup
mp_holistic = mp.solutions.holistic # Holistic model
mp_draw = mp.solutions.drawing_utils # Drawing utilities

# Dictionary containing each word, and number of parts to word
words = {"hello": 1, "thank you": 1}

# Set up tensorflow model
model = tf.keras.models.load_model("model.h5")

# --------Helper Functions-------- #

# Convert base64 image to cv2 image
def base64_to_cv2_image(base64_img):
    # Convert base64 image to bytes
    img_bytes = base64.b64decode(base64_img)

    # Convert bytes to numpy array
    img_array = np.frombuffer(img_bytes, dtype=np.uint8)

    # Convert numpy array to cv2 image
    img = cv2.imdecode(img_array, flags=cv2.IMREAD_COLOR)

    # Return cv2 image
    return img

# Get results from frame
def mediapipe_detection(image, model):
    # Convert image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False # To improve performance
    results = model.process(image) # Make detections
    image.flags.writeable = True # To improve performance
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # Convert back to BGR
    return image, results

# Make predictions
def process_image(image):
    model = tf.keras.models.load_model("model.h5")

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        # Get mediapipe detection
        image, results = mediapipe_detection(image, holistic)

        # Convert landmarks to numpy array
        landmarks = np.array([[res.x, res.y, res.z] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*3)
        landmarks = np.concatenate((landmarks, np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)), axis=0)
        landmarks = np.concatenate((landmarks, np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)), axis=0)

        # Make predictions
        predictions = model.predict(np.array([landmarks]))

        # Get the index of the prediction
        prediction = np.argmax(predictions[0])

        # Get the word from the index
        word = list(words.keys())[prediction]

        # Return word
        return word

# Draw landmarks
def draw_landmarks(image, results):
        mp_draw.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Pose connections
        mp_draw.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Left hand connections
        mp_draw.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Right hand connections

# --------Main-------- #

# Function for reading frames
#cap = cv2.VideoCapture(0)
#while(cap):
    # Get webcam feed
#    ret, image = cap.read()

    # Make detections
    #image, results = mediapipe_detection(image, holistic)

    # Draw landmarks
    #draw_landmarks(image, results)

    # Draw predictions
#    try:
#        cv2.putText(image, process_image(image), (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv2.LINE_AA)
    # No predictions
#    except:
#        pass

    # Show to screen
#    cv2.imshow('frame', image)

    # Break loop
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break