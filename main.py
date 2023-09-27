from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio') #definição da rota de aplicação

def ola():
    return render_template('lista.html')

app.run() #iniciar projeto