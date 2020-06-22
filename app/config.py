import os
from os.path import abspath, normpath, dirname, join

BASE_DIR = abspath(dirname(__file__))


class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ''

    # The number of connections to keep open inside the connection pool
    SQLALCHEMY_DATABASE_POOL_SIZE = 5

    LOGGER_NAME = 'flask'

    LOG_FILENAME = normpath(join(BASE_DIR, 'logs/pileta-api.log'))
    LOG_LEVEL = 'INFO'
    SQLALCHEMY_LOG_LEVEL = 'WARNING'
    LOG_ROTATION_INTERVAL_UNIT = 'D'
    LOG_ROTATION_INTERVAL = 1
    LOG_BACKUP_COUNT = 7
    LOG_FILE_FORMAT = '%(asctime)s %(levelname)s %(name)s %(message)s %(pathname)s %(lineno)d %(module)s %(funcName)s'
    LOG_CONSOLE_FORMAT = "[%(asctime)s] (%(name)s) %(levelname)s: %(message)s"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@pileta-db/pileta_api'


class ProductionConfig(BaseConfig):
    pass


if 'PILETA_ENV' not in os.environ:
    os.environ['PILETA_ENV'] = 'development'

env = os.environ['PILETA_ENV']
cls_name = "{0}Config".format(env.capitalize())
selected_config = "config.{0}".format(cls_name)
current_config = eval(cls_name)
