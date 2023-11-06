from flask import render_template, url_for, request, redirect, session, flash
from app import app, db
from models import Usuarios 
from helpers import FormularioLogin
from flask_bcrypt import check_password_hash

#pagina inicial de login
@app.route('/') #definição da rota de aplicação
def login():
    form = FormularioLogin()
    return render_template('login.html', form=form)

#rota para login de usuario
@app.route('/logar', methods=['GET', 'POST'])
def logar():
    form = FormularioLogin(request.form)
    senha = check_password_hash(usuario.senha, form.password.data)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        usuario = Usuarios.query.filter_by(nickname=username).first()
        if usuario:
            if senha:
                flash('Logado com sucesso!')
                return render_template('home.html')  
        
        flash('Usuário ou senha incorretos!')  
    return redirect(url_for('login'))

#rota para deslogar
@app.route('/deslogar')
def deslogar():
    session['usuario_logado'] = None
    flash('Saiu com sucesso!')
    return redirect(url_for('login'))

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
    
    user = Usuarios.query.filter_by(nome=nome).first()
    
    if user:
        flash('usuario já cadastrado')
        return redirect(url_for('criar'))
    
    usuario = Usuarios(nome, senha, departamento) 
    db.session.add(usuario)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/home', methods=['GET',])
def home():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')
    return render_template('home.html')

@app.route('/relatorios', methods=['GET', 'POST'])
def relatorios():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')
    return render_template('relatorios.html')

@app.route('/solicitacoes')
def solicitacoes():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')
    return render_template('solicitacoes.html')

@app.route('/suporte')
def suporte():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/')
    return render_template('suporte.html')
