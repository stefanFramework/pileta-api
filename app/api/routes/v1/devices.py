from flask import jsonify
from flask_restful import Resource

from domain.models.devices import Device
from database import get_session
from datetime import datetime


class Devices(Resource):
    def __init__(self):
        self.session = get_session()

    def post(self):
        pass

    def get(self):
        # device = Device()
        # device.name = 'test2'
        # device.ip = '123'
        # device.created_at = datetime.today().strftime('%Y-%m-%d')
        # device.updated_at = datetime.today().strftime('%Y-%m-%d')
        # self.session.add(device)
        # self.session.commit()

        return jsonify({
            'status': 'OK'
        })

    def delete(self, id):
        pass