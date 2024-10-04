from app import app
from flask import render_template

@app.route('/')  # define a raiz do projeto
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')