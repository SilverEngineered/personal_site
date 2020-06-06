from app import app
from flask import render_template, url_for, jsonify, request
import fractal_gen

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
@app.route('/Fractal')
def fractal():
	fractal_gen.makeImage()
	return render_template('fractal.html', title='FRACTAL!')
@app.route('/json', methods = ['POST'])
def json():
	if not request.json or not 'title' in request.json:
		abort(400)
	task = {
		'id': 1,
		'title': request.json['title'],
		'description': request.json.get('description', ""),
		'done': False
	}
	return jsonify({'task': task}), 201