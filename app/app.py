from flask import Flask
from config import selected_config
from api import create_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(selected_config)

    create_api(app)

    return app