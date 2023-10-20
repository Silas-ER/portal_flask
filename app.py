from flask import Flask, render_template, url_for, request, redirect, session, flash

class User:
    def __init__(self, nome, senha, departamento):
        self.nome = nome
        self.senha = senha
        self.departamento = departamento

listaUsers = []
        
first_user = User("silas", "12345", "TI")
listaUsers.append(first_user)

app = Flask(__name__)
app.secret_key = 'produmar' #criptografar

#pagina inicial de login
@app.route('/login') #definição da rota de aplicação
def login():
    return render_template('login.html')

#rota para login de usuario
@app.route('/logar', methods=['GET','POST'])
def logar():
    username = request.form['username']
    password = request.form['password']

    for user in listaUsers:
        if user.nome == username and user.senha == password:
            session['usuario_logado'] = username #manter logado
            return redirect('/home')
        else:
            flash('Usuário ou senha incorretas!') #inputar mensagens
            return redirect('/login')

#rota para deslogar
@app.route('/deslogar')
def deslogar():
    session['usuario_logado'] = None
    flash('Saiu com sucesso!')
    return redirect('/login')

#rota criar usuario
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

@app.route('/home', methods=['GET',])
def home():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('home.html')

@app.route('/relatorios', methods=['GET', 'POST'])
def relatorios():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('relatorios.html')

@app.route('/solicitacoes')
def solicitacoes():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('solicitacoes.html')

@app.route('/suporte')
def suporte():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('suporte.html')

app.run(debug=True) #iniciar projeto 