from flask import Flask

def create_app(selected_config):
    app = Flask(__name__)
    app.config.from_object(selected_config)
    return app