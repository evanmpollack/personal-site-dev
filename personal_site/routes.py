from personal_site import app
from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index')


@app.route('/about')
def about():
    return render_template('about')


@app.route('/experience')
def experience():
    return render_template('experience')


@app.route('/education')
def education():
    return render_template('education')


@app.route('/projects')
def projects():
    return render_template('projects')
