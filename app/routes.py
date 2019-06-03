from app import app
from flask import render_template, url_for
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/Projects')
def projects():
	return render_template('projects.html')

@app.route('/Contact')
def contact():
	phone="321-xxx-xxxx"
	return render_template('contact.html', title='About Me')
