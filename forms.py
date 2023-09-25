from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField

from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    cep = StringField('Cep', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class ItemForm(FlaskForm):
    produto_id = HiddenField(validators=[DataRequired()])
    quantity = HiddenField(validators=[DataRequired()])
