import os

from flask import Flask

from views import main_bp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
