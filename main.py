from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField
from flask import Flask, render_template, redirect, url_for
from wtforms.validators import DataRequired
from data import db_session
from forms.user import RegisterForm
from data.users import User
from data.invents import Invent
from flask_login import LoginManager, login_user, login_required, logout_user
from random import randint

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = 'art_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/chest')
def chest():
    a = randint(1, 3)
    if a == 1:
        return f""""<!doctype html>
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
                    <div>
                        <img src="{url_for('static', filename='img/tap.png')}", width="1000", height="555"/>
                    </div>
                    <p>
                        <a class="btn btn-primary ">продать</a>
                        <a class="btn btn-primary ">получить</a>
                    </p>
                </body>
            </html>"""
    elif a == 2:
        return f""""<!doctype html>
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
                            <div>
                                <img src="{url_for('static', filename='img/tap.png')}", width="1000", height="555"/>
                            </div>
                            <p>
                                <a class="btn btn-primary ">продать</a>
                                <a class="btn btn-primary ">получить</a>
                            </p>
                        </body>
                    </html>"""
    else:
        return f""""<!doctype html>
                            <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1,
                                     shrink-to-fit=no">
                                    <link rel="stylesheet"
                                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                          crossorigin="anonymous">
                                    <title>Rat</title>
                                </head>
                                <body>   
                                    <div>
                                        <img src="{url_for('static', filename='img/tap.png')}", width="1000",
                                         height="555"/>
                                    </div>
                                    <p>
                                        <a class="btn btn-primary ">продать</a>
                                        <a class="btn btn-primary ">получить</a>
                                    </p>
                                </body>
                            </html>"""


@app.route('/')
@app.route('/main')
def main():
    db_sess = db_session.create_session()
    inv = db_sess.query(Invent)
    return render_template('main.html', inv=inv)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        inv = Invent(money=0, user=user)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.add(inv)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/invent')
def invent():
    return render_template('invent.html', form='css/style.css')


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
