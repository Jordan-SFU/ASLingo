# Program for training tensorflow model on DATA folder

# Imports
import os
import tensorflow as tf
import FramesToNumpy as ftn
import numpy as np
from sklearn.preprocessing import LabelEncoder
import keras

trainingLen = 20

# Path to dataset
DATADIR = "data"
numLabels = len(os.listdir(DATADIR)) - 2

# Each word part has 10 training numpy arrays (using ftn)
# Assign labels to each numpy array
# Create training data
training_data = []
training_labels = []

# if training_data.npy does not exist, train model
if not os.path.isfile("training_data.npy"):
    # Iterate through each word
    for word in os.listdir(DATADIR):
        # Iterate through each training numpy array
        for i in range(1, trainingLen + 1):
            try:
                # Add training data to list
                # Convert lists to numpy arrays
                training_data_np = np.array(ftn.landmarkArray(ftn.poseToNumpy(word, word + "1-" + str(i) + ".jpg"), ftn.handsToNumpy(word, word + "1-" + str(i) + ".jpg")))
                training_data.append(training_data_np)
                print(training_data_np)
            except:
                pass

# add labels
for word in os.listdir(DATADIR):
    for i in range(1, trainingLen + 1):
        training_labels.append(word)

# save training data and labels to file
np.save('training_data.npy', training_data)

# load training data and labels from file
training_data = np.load('training_data.npy', allow_pickle=True)

print(numLabels, len(training_data), len(training_labels))

# Set up tensorflow model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(numLabels, activation=tf.nn.softmax))

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# Reshape the data
training_data_np = np.array(training_data).reshape((trainingLen * numLabels), -1)

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
training_data_np = np.array(training_data).reshape((trainingLen * numLabels), -1)

# Make predictions
predictions = new_model.predict(training_data_np)

# convert predictions into strings
predictions = le.inverse_transform([np.argmax(i) for i in predictions])

# Print predictions and labels
print(predictions)
print(training_labels)