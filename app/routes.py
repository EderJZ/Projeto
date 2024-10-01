from app import app
from flask import render_template

@app.route('/')  # define a raiz do projeto
@app.route('/index')
def index():
    nome = "Eder"
    dados = {"profissao": "Professor", "canal": "eu123"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
