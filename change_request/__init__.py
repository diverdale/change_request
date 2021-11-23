from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)
mail = Mail(app)
Bootstrap(app)
Migrate(app, db)

from change_request.views import change_request
app.register_blueprint(change_request, url_prefix='')
