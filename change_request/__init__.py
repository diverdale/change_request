import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)

basedir = os.path.abspath(os.path.dirname(__file__))
# toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)
mail = Mail(app)
Bootstrap(app)
Migrate(app, db)

from .views import change_request
from .views import api
app.register_blueprint(change_request, url_prefix='')
app.register_blueprint(api, url_prefix='/api/v1')