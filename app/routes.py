from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user
from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'shigel'}
    posts = [
                {
                    'author': {'username': 'Kim'},
                    'body': 'Beautiful Land'
                },
                {
                    'author': {'username': 'Abe'},
                    'body': 'Beautiful Fucked'
                },
            ]
    return render_template(
            'index.html',
            title='Home',
            user=user,
            posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)
