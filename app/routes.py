from app import app
from flask import render_template

@app.route('/')  # define a raiz do projeto
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')
