from flask import Flask, render_template, url_for, request, redirect

class User:
    def __init__(self, nome, senha, departamento):
        self.nome = nome
        self.senha = senha
        self.departamento = departamento

listaUsers = []
        
first_user = User("silas", "12345", "TI")
listaUsers.append(first_user)

app = Flask(__name__)

#pagina inicial de login
@app.route('/login') #definição da rota de aplicação
def login():
    return render_template('login.html')

#rota para login de usuario
@app.route('/logar', methods=['GET', 'POST'])
def logar():
    username = request.form['username']
    password = request.form['password']

    for user in listaUsers:
        if user.nome == username and user.senha == password:
            return redirect('/home')
    
    return render_template('login.html', error_message="Usuário não encontrado!")

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

#página de relatórios
@app.route('/relatorios', methods=['GET', 'POST'])
def relatorios():
    return render_template('relatorios.html')

@app.route('/home', methods=['GET',])
def home():
    return render_template('home.html')

app.run() #iniciar projeto 