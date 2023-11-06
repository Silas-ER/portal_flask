import os
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators 
from wtforms.validators import DataRequired, Length

class FormularioCadastro(FlaskForm):
    nickname = StringField()
    password = StringField()
    departamento = StringField()
    #salvar = 

class FormularioLogin(FlaskForm):
    nickname = StringField('username', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=1, max=100)])
    entrar = SubmitField('Login')