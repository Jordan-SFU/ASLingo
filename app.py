from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'thisissecret'

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

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@app.route('/lesson2')
def lesson2():
    return render_template('lesson2.html')

@app.route('/lesson3')
def lesson3():
    return render_template('lesson3.html')