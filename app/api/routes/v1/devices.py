import logging

from flask import jsonify, request, abort
from flask_restful import Resource

from domain.models.devices import Device
from domain.repositories.devices import DeviceRepository
from database import get_session
from datetime import datetime

logger = logging.getLogger(__name__)


class Devices(Resource):
    def __init__(self):
        self.session = get_session()
        self.repo = DeviceRepository(self.session)

    def post(self):
        data = request.get_json()

        logger.info('Receive', extra={'data': str(data)})

        device = Device()
        device.name = data.get('name', None)
        device.ip = data.get('ip', None)
        device.notes = data.get('notes', None)

        self.repo.create(device)

        return {
            'status': 'OK'
        }, 201

    def get(self):
        devices = self.repo.find_all()

        if devices is None:
            return []

        return [device.serialize() for device in devices]

    def delete(self, id):
        pass
