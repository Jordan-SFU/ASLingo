from flask import Flask, render_template, request
from PIL import Image
import Backend as bk

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

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    img = Image.open(file.stream)

    prediction = bk.process_image(img)
    return {'prediction': prediction}