import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'supersecretkey'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True

MAIL_SERVER = 'outbound.cisco.com'
