from flask import Flask, render_template

class User:
    def __init__(self, nome, senha, departamento):
        self.nome = nome
        self.senha = senha
        self.departamento = departamento

listaUsers = []
        
app = Flask(__name__)

@app.route('/login') #definição da rota de aplicação

def login():
    return render_template('login.html')

app.run() #iniciar projeto