from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    names_of_fuckers = ["Sashimi", "Junta", "Hanneman"]
    random_name = "Kim"
    return render_template(
            'welcome.html',
            names=names_of_fuckers,
            name=random_name)


@app.route('/show-form')
def show_form():
    return render_template('first-form.html')


@app.route('/data')
def print_name():
    first = request.args.get('first')
    last = request.args.get('last')
    return f"You killed {first} {last}"


@app.route('/title')
def title():
    return render_template('title.html')


@app.route('/hi')
def hi():
    return "fucked HI"


@app.route('/bye')
def bye():
    return "bye"


@app.route('/name/<person>')
def say_name(person):
    return f"The name is {person}"


@app.route('/name/<int:num>')
def favorite_number(num):
    output = f"Your fucked up favorite number was {num}, "
    output += f" which was half of {num * 2}"
    return output


@app.route('/')
def home():
    return render_template("home.html", title="hell")


@app.route('/about')
def about():
    return render_template("about.html", title="hellabout")


@app.route('/contact')
def contact():
    return render_template("contact.html", title="contact ass")


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
