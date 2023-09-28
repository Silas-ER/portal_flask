from flask import Flask, render_template, url_for, request, redirect

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

@app.route('/criar', methods=['GET', 'POST'])

def criar():     
    return render_template('criar_user.html')

#criação de novo usuário
@app.route('/salvarnovo', methods=['POST'])

def salvarnovo():
    nome = request.form['username']
    senha = request.form['password']
    departamento = request.form['dpt']
    usuario = User(nome, senha, departamento) 
    listaUsers.append(usuario)
    return redirect('/login')
app.run() #iniciar projeto e o debugger para rodar direto