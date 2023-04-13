from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask import Flask, request, render_template, redirect
from wtforms.validators import DataRequired
from data import db_session

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = 'art_secret_key'
db_session.global_init("db/blogs.db")
app.run()

@app.route('/chest')
def chest():
    return '''         <!doctype html>
                                    <html lang="en">
                                      <head>
                                        <meta charset="utf-8">
                                        <meta name="viewport" content="width=device-width, 
                                        initial-scale=1, shrink-to-fit=no">
                                        <link rel="stylesheet"
                                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                        crossorigin="anonymous">
                                        <link rel="stylesheet" type="text/css" />
                                        <title>reg</title>
                                      </head>
                                      <body>
                                        <h1 align="center">Chest</h1>
                                      </body>
                                    </html>'''


@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/success')
def success():
    return """"<!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                  integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                  crossorigin="anonymous">
            <title>Rat</title>
        </head>
        <body>
                <div align="right">
                    <a href="/login" class="btn btn-primary">профиль</a>
                    <a type="submit" class="btn btn-primary">выйти</a>
                </div>
                <h1 align="center">RAT</h1>
                <h3 style="margin-top: 100px;" align="center">Base</h3>
                <div align="center">
                    <img filename='data/Chest.jpg', width="100", height="111"/>
                </div>
        </body>
    </html>"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
