# Program for training tensorflow model on DATA folder

# Imports
import os
import tensorflow as tf
import FramesToNumpy as ftn
import numpy as np
from sklearn.preprocessing import LabelEncoder
import keras

trainingLen = 10

# Path to dataset
DATADIR = "data"

# Each word part has 10 training numpy arrays (using ftn)
# Assign labels to each numpy array
# Create training data
training_data = []
training_labels = []

# Iterate through each word
for word in os.listdir(DATADIR):
    # Iterate through each training numpy array
    for i in range(1, trainingLen + 1):
        try:
            # Add training data to list
            # Convert lists to numpy arrays
            training_data_np = np.array(ftn.landmarkArray(ftn.poseToNumpy(word, word + "-" + str(i) + ".jpg"), ftn.handsToNumpy(word, word + "-" + str(i) + ".jpg")))
            training_data.append(training_data_np)
            print(training_data_np)
            # Add training labels
            print(word)
            training_labels.append(word)
        except:
            pass

# Set up tensorflow model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(len(os.listdir(DATADIR)), activation=tf.nn.softmax))

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])



training_data_np = np.array(training_data).reshape((trainingLen * len(os.listdir(DATADIR)), -1))

# Create a label (category) encoder object
le = LabelEncoder()

# Fit the encoder to the pandas column
le.fit(training_labels)

# Apply the fitted encoder to the pandas column
training_labels_np = le.transform(training_labels) 

# Train model
model.fit(training_data_np, training_labels_np, epochs=100)

# Save model
model.save('model.h5')

# Load the model
new_model = keras.models.load_model('model.h5')

# Reshape the data
training_data_np = np.array(training_data).reshape((trainingLen * len(os.listdir(DATADIR)), -1))

# Make predictions
predictions = new_model.predict(training_data_np)

# convert predictions into strings
predictions = le.inverse_transform([np.argmax(i) for i in predictions])

# Print predictions and labels
print(predictions)
print(training_labels)