import os 
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

class Config(object):
    # Default
    SECRET_KEY = '<YOUR SECRET KEY>'  

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    APPLICATION_LOG = '{}/log/application_production.log'.format(BASE_DIR)

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    APPLICATION_LOG = '{}/log/application_development.log'.format(BASE_DIR)