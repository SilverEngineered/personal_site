from app import app
from flask import render_template, url_for
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
@app.route('/Projects')
def projects():
	return render_template('projects.html', title='Projects')

@app.route('/Contact')
def contact():
	return render_template('contact.html', title='Contact')

@app.route('/Upcoming')
def upcoming():
	return render_template('upcoming.html', title='upcoming')
