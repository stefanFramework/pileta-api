from flask import jsonify
from flask_restful import Resource

class Measurements(Resource):
    def post(self):
        # Registers a new measurement
        pass

    def get(self):
        # Get the last measurement from each metric
        pass