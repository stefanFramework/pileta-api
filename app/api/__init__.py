from flask import Flask
from flask_restful import Api

from api.routes.v1.utils import Utils
from api.routes.v1.devices import Devices
from api.routes.v1.measurements import Measurements

def create_app():
    app = Flask(__name__)
     # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@database/pileta_api'

    api = Api(app)
    api.add_resource(Utils, '/utils')
    api.add_resource(Devices, '/devices')
    api.add_resource(Measurements, '/measurements')

    return app