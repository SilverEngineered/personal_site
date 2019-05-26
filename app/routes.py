from app import app
from flask import render_template, url_for
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dan'}
    posts = [
        {
            'title': 'Hi There!',
            'body': 'If you are here I can only hope to believe you are atleast a little bit '\
            'interested in my work and qualifications.  This website serves as' \
            ' a portfolio for that very purpose!'
        },
        {
            'title': 'Who am I',
            'body': 'My name is Dan Silver and I am currently pursuing'\
            ' a dual Bachelor\'s and Master\'s degree in Computer Engineering,' \
            ' concentrating in Machine Learning, Computer Vision, and Algorithms. ' \
            ' I am in my 4th year of study at Northeastern University. My graduate GPA is a 4.0' \
            ' and my Major GPA is  3.66. While my degree' \
            ' is more hardware based, my work experience and personal projects are ' \
            'more based on a mix of machine learning, computer vision, and software!'
        },
                {
            'title': 'My skills',
            'body': 'My technical toolbelt includes experience in the following: '\
            ' Deep Learning, Tensorflow, Apache Spark, Generative Adversarial Networks, Natural Language Processing, Git, Triplet Embedding Networks'\
            ', Computer Vision, Object Tracking, Linux, Game design for research/data acquisition, Parallel Processing, & Embedded design'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/Projects')
def projects():
	return render_template('projects.html')

@app.route('/Contact')
def contact():
	phone="321-xxx-xxxx"
	return render_template('contact.html', title='About Me', phone=phone)
