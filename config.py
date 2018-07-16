import os
import secrets
from os.path import join, dirname
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_urlsafe()
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
