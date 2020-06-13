# TODO: Crear una Clase Config por ambiente y meter todos los
# parametros de configuracion
import os

class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ''

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@pileta-db/pileta_api'


if 'PILETA_ENV' not in os.environ:
    os.environ['PILETA_ENV'] = 'development'

env = os.environ['PILETA_ENV']
cls_name = "{0}Config".format(env.capitalize())
selected_config = "config.{0}".format(cls_name)