from personal_site import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!!!'

@app.route('/test')
def render():
    return render_template('index.html')