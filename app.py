from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hell fuck lask'


@app.route('/hell/<name>')
def hell_there(name):
    from datetime import datetime
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    html_content = "<html><head><title>Hell, fucklask</title></head><body>"
    html_content += "<strong>Hell there, " + name + "!</strong>. It's "
    html_content += formatted_now
    html_content += "</body></html>"

    return html_content
