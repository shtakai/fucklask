from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hell fuck lask'


@app.route('/hell/<name>')
def hell_there(name):
    from datetime import datetime
    now = datetime.now()

    return render_template(
            "hell_there.html",
            title="hell no",
            message="Hell there, " + name + "!",
            date=now.strftime("%A, %d %B, %Y at %X")
            )
