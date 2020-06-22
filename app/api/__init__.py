from flask_restful import Api

from api.routes.v1.utils import Utils
from api.routes.v1.devices import Devices
from api.routes.v1.measurements import Measurements


def create_api(app):
    api = Api(app)
    api.add_resource(Utils, '/utils')
    api.add_resource(Devices, '/devices')
    api.add_resource(Measurements, '/measurements')
