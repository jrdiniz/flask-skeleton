from flask import Blueprint

from .default import index

bp = Blueprint('default', __name__, template_folder="templates")

index.methods = ['GET']
bp.add_url_rule('/', view_func=index)

def init_app(app):
    app.register_blueprint(bp, url_prefix='/')