from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField('Email cím', validators=[DataRequired(), Email()])
    password = PasswordField('Jelszó', validators=[DataRequired()])
    submit = SubmitField('Bejelentkezés')

class RegistrationForm(FlaskForm):
    username = StringField('Felhasználónév', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email cím', validators=[DataRequired(), Email()])
    password = PasswordField('Jelszó', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Jelszó megerősítése', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Regisztráció')