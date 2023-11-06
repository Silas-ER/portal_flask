from flask import render_template, url_for, request, redirect, session, flash
from app import app, db
from werkzeug.security import check_password_hash
from models import Usuarios 
from helpers import FormularioLogin
from flask_bcrypt import check_password_hash

#pagina inicial de login
@app.route('/') #definição da rota de aplicação
def login():
    form = FormularioLogin()
    return render_template('login.html', form=form)

@app.route('/logar', methods=['GET', 'POST'])
def logar():
    form = FormularioLogin()

    if form.validate_on_submit():
        username = form.nickname.data
        password = form.password.data

        usuario = Usuarios.query.filter_by(nickname=username).first()
        if usuario and check_password_hash(usuario.senha, password):
            flash('Logado com sucesso!')
            session['usuario_logado'] = username  # Defina a sessão do usuário
            return redirect(url_for('home'))  # Redirecione para a rota 'home'

        flash('Usuário ou senha incorretos!')

    return render_template('login.html', form=form)  # Redirecione para a página de login ('login.html')

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
