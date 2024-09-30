from app import app
from flask import render_template

@app.route('/')  # define a raiz do projeto
@app.route('/index')
def index():
    nome = "Eder"
    return render_template('index.html')
    