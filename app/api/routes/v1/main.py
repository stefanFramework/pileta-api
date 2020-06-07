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

# TODO:
# Una vez definidas las rutas, pasar a resources --> class MeasurmentsCollection(Resource): ...
# Crear las Entities con SQLAlchemy
#
# app = Flask(__name__)
#
# # dialect://username:password@host:port/database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@database/pileta_api'
# db = SQLAlchemy(app)
#
#
# class Device(db.Model):
#     __tablename__ = 'devices'
#
#     id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column('name', db.String, nullable=False)
#     ip = db.Column('ip', db.String, nullable=False)
#     notes = db.Column('notes', db.String, nullable=False)
#
#
# @app.route('/version', methods=['GET'])
# def version():
#     current_date = datetime.datetime.now()
#     response = {
#         'name': 'pileta-api',
#         'version': '1.0.0',
#         'date': current_date.strftime("%Y-%m-%d %H:%M")
#     }
#     return jsonify(response)

#
# @app.route('/device', methods=['GET'])
# def get_devices():
#     device = Device()
#     device.ip = '10.0.0.0'
#     device.name = 'orm created'
#     device.notes = 'asasasd'
#     db.session.add(device)
#     db.session.commit()
#     ld = Device.query.first()
#
#     response = {
#         'id': ld.id,
#         'ip': ld.ip,
#         'name': ld.name,
#         'notes': ld.notes
#     }
#
#     return jsonify(response)
#
# # Registers a new measurements
# @app.route('/register', methods=['POST'])
# def register():
#     if request.method != 'POST':
#         return ''
#
#     return 'register'
#
#
# # For variable status pooling
# @app.route('/status', methods=['GET'])
# def status():
#     return 'status'