"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""


from datetime import datetime
from flask import render_template, Flask
app = Flask(__name__)
from mainpage.views import app

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
if __name__ == '__main__':
    # app.run(port=80)
    app.run()
