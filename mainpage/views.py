from datetime import datetime
from email import message
from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template(
        'index.html',
        title='Flask',
        year=datetime.now().year,
        message='Under development...'
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Pending...'
    )

@app.route('/discordbot')
def discordbot():
    return render_template(
        'discordbot.html',
        title='Bot',
        year=datetime.now().year,
        message='Pending...'
    )