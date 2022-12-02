from flask import Flask, redirect, render_template, request, url_for
#from crypt import methods
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, 
                     SubmitField, EmailField,
                     IntegerField, RadioField,
                     SelectField, TextAreaField)
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

############## Rutas public##############
@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about/')
def about():
    return render_template('public/about.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

# @app.route('/portfolio')
# def portfolio():
#    return render_template('public/portfolio.html')

@app.route('/portfolio')
def portfolio():
    projects = [
        {
            'name':'Primer proyecto',
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/home-bg.jpg',
            'url': 'http://google.com'
        },
        {
            'name':'Segundo proyecto',
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'http://xataka.com'
        }, 
        {
            'name':'Primer proyecto',
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/home-bg.jpg',
            'url': 'http://google.com'
        },
        {
            'name':'Segundo proyecto',
            'description': 'As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm....',
            'image': 'img/about-bg.jpg',
            'url': 'http://xataka.com'
        }
    ]
    return render_template('public/portfolio.html', projects=projects)

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


############## Rutas Login ######################

@app.route('/auth/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        return render_template('admin/index.html', email= email )

    return render_template('auth/login.html', form = form)

@app.route('/auth/register')
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form = form)

# @app.route('/welcome', methods = ['GET', 'POST'])
# def welcome(form):
#   form = LoginForm()
#    if form.validate_on_submit():
#        email = form.email.data
#        password = form.password.data
#        #email = request.form['mail']
#        #password = request.form['password']
#        #access = {'email': email }
#        return render_template('admin/index.html', email= email )
#    return redirect(url_for('login'))

@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('error/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)