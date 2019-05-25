from app import app
from flask import render_template, url_for
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
                {
            'author': {'username': 'Dan'},
            'body': 'Dogs!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/About')
def about():
	phone="321-xxx-xxxx"
	return render_template('about.html', title='About Me', phone=phone)
