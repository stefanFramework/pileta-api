import logging
from flask import Flask
from config import current_config, selected_config
from api import create_api
from log import LogConfigurator


def create_app():
    app = Flask(__name__)
    app.config.from_object(selected_config)

    create_api(app)

    log_configurator = LogConfigurator(current_config)

    file_handler = log_configurator.create_file_handler()
    console_handler = log_configurator.create_console_handler()
    level = log_configurator.get_current_log_level()

    logging.basicConfig(handlers=[file_handler, console_handler],
                        level=level)

    return app
