import os
import logging
import logging.handlers

def init_app(app):
    if app.debug:
        app.config.from_object('config.DevelopmentConfig')
        logging.basicConfig(filename=app.config['APPLICATION_LOG'],
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.DEBUG)     
    else:
        app.config.from_object('config.ProductionConfig')
        logging.basicConfig(filename=app.config['APPLICATION_LOG'],
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.DEBUG)   
        