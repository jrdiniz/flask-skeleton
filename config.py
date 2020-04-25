class Config(object):
    # Default
    SECRET_KEY = 'C3}Z%~H:qvjdhm}e)=Cjen4[t.7fNEP*3dd9--RB&jgVAm?hYzDD'

class ProductionConfig(Config):
    # Debug
    DEBUG = False

class DevelopmentConfig(Config):
    # Debug
    DEBUG = True