import os
from dotenv import load_dotenv

def init_app(app):
    load_dotenv()
    app.config.from_object(os.environ['FLASK_CONFIG_FILE'])