import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "2Do"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'myApp.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False