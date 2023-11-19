from flask import Flask, render_template, request
from PIL import Image
import Backend as bk
import base64
import io
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/learning')
def learning():
    return render_template('learning.html')

@app.route('/login')
def login():
    return render_template('homePage.html')

@app.route('/translator')
def translator():
    return render_template('translator.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    # Get the image data from the POST request
    data = request.data

    # Convert the base64 data to a PIL image
    image = Image.open(io.BytesIO(base64.b64decode(data)))

    # Convert the PIL image to a numpy array
    image = np.array(image)

    # Convert the image to BGR format for cv2
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Pass the image to your process_image function
    prediction = bk.process_image(image)

    # Return the prediction
    return prediction

if __name__ == '__main__':
    app.run(debug=True)