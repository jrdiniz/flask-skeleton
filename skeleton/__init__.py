from flask import Flask

# Extensions
from skeleton.extensions import configuration

# Blueprints
from skeleton.blueprints import default

def create_app():
	app = Flask(__name__)

	# Load Extensions
	configuration.init_app(app)

	# Load Blueprints
	default.init_app(app)

	return app