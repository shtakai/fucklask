import os
from os.path import join, dirname
from dotenv import load_dotenv


class Config(object):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    SECRET_KEY = os.environ.get('SECRET_KEY')
