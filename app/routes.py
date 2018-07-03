from flask import render_template
from app import app


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
