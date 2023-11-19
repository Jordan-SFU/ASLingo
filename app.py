from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import Backend as bk


app = Flask(__name__)
# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = 'thisissecret'

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False)
#     password = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/learning')
def learning():
    return render_template('learning.html')

@app.route('/translator')
def translator():
    return render_template('translator.html')

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@app.route('/lesson2')
def lesson2():
    return render_template('lesson2.html')

@app.route('/lesson3')
def lesson3():
    return render_template('lesson3.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    data = request.json
    frame_data_url = data.get('frame', '')

    # Extract the base64-encoded image data from the data URL
    _, encoded = frame_data_url.split(',', 1)
    image_data = encoded.encode('ascii')  # Python 3

    # Save the image to a file or process it using Pillow
    with open('captured_frame.png', 'wb') as f:
        f.write(image_data)
    prediction = bk.process_image('captured_frame.png')
    print(prediction)
    return 'Frame received and processed!'

if __name__ == '__main__':
    app.run(debug=True)
