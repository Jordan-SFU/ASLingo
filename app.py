from flask import Flask, render_template

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