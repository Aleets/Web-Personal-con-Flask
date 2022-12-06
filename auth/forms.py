from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, 
                     SubmitField, EmailField,
                     IntegerField, RadioField,
                     SelectField, TextAreaField)
from wtforms.validators import DataRequired, Email

########## Formularios de WTForms ###############

class LoginForm(FlaskForm):
    email = EmailField('Username', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    name = StringField('Nombre')
    last_name = StringField('Apellidos')
    email = EmailField('Correo')
    password = PasswordField('Contraseña')
    phone = IntegerField('Telefono')
    is_married = RadioField('Estado Civil', choices = [( 'True', 'Casado' ), ('False', 'Soltero')])
    gender = SelectField('Genero', choices = [( 'male','Masculino' ), ( 'famele', 'Femenino' ), ('other', 'Otro' )])
    submit = SubmitField('Registar')