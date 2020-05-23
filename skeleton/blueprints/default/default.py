from flask import render_template
from flask import current_app

def index():
    current_app.logger.info('Logging message from blueprint default')
    return render_template('index.html')