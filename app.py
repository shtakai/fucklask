from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", title = "hell")


@app.route('/about')
def about():
    return render_template("about.html", title = "hellabout")


@app.route('/contact')
def contact():
    return render_template("contact.html", title = "contact ass")


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

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')
