import datetime
import os
import time

from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'outbound.cisco.com'

# toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)
# mail = Mail(app)
Bootstrap(app)
Migrate(app, db)


from change_request.views import change_request

app.register_blueprint(change_request, url_prefix='')
