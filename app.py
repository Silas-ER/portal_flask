from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app) #ponte para banco de dados real
crsf= CSRFProtect(app)

bcrypt = Bcrypt(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True) #iniciar projeto 