import os

class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ''

    # The number of connections to keep open inside the connection pool
    SQLALCHEMY_DATABASE_POOL_SIZE = 5

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