import sys
import json
import logging

from datetime import datetime
from config import current_config

from logging.handlers import TimedRotatingFileHandler
from pythonjsonlogger.jsonlogger import JsonFormatter


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


class LogConfigurator():
    def __init__(self, current_config):
        self.config = current_config

    def create_file_handler(self):
        handler = TimedRotatingFileHandler(filename=self.config.LOG_FILENAME,
                                           when=self.config.LOG_ROTATION_INTERVAL_UNIT,
                                           backupCount=self.config.LOG_BACKUP_COUNT,
                                           interval=self.config.LOG_ROTATION_INTERVAL)

        formatter = JsonFormatter(fmt=self.config.LOG_FILE_FORMAT,
                                  json_encoder=CustomJsonEncoder)

        handler.setFormatter(formatter)
        return handler

    def create_console_handler(self):
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(fmt=self.config.LOG_CONSOLE_FORMAT)
        handler.setFormatter(formatter)
        return handler

    def get_current_log_level(self):
        return self.config.LOG_LEVEL
