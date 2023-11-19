
from flask import Flask, render_template, request, redirect, url_for
import json
import Backend as bk

app = Flask(__name__)

jsonReader = open('data/database.json', 'r')
jsonWriter = open('data/database.json', 'w')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/learning')
def learning():
    return render_template('learning.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = json.load(jsonReader)
        username = request.form['username']
        password = request.form['password']
        for user in data['users']:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('learning'))
        return render_template('login.html', error='Invalid username or password')
    return render_template('homePage.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = json.load(jsonReader)
        username = request.form['username']
        password = request.form['password']
        for user in data['users']:
            if user['username'] == username:
                return render_template('register.html', error='Username already exists')
        data['users'].append({
            'username': username,
            'password': password
        })
        jsonWriter.write(json.dumps(data))
        return redirect(url_for('learning'))
    return render_template('register.html')


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

    # convert to cv2 image
    image = bk.base64_to_cv2_image(image_data)
    return bk.process_image(image)

if __name__ == '__main__':
    app.run(debug=True)
