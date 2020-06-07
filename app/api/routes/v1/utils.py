import datetime
from flask import jsonify
from flask_restful import Resource

class Utils(Resource):
    def get(self):
        current_date = datetime.datetime.now()
        response = {
            'name': 'pileta-api',
            'version': '1.0.0',
            'date': current_date.strftime("%Y-%m-%d %H:%M")
        }
        return jsonify(response)