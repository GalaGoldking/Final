from flask import Flask, render_template, url_for
from flaskapp import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

@app.route('/medicine')
def medicine():
    return render_template('medicine.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')