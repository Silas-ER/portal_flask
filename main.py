from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        
app = Flask(__name__)

@app.route('/inicio') #definição da rota de aplicação

def ola():
    jogo1 = Jogo('bom de guerra', 'ação', 'ps5')
    jogo2 = Jogo('mentiras de pi', 'ação', 'xbox')
    lista = [jogo1, jogo2]
    return render_template('lista.html', jogos = lista)

app.run() #iniciar projeto