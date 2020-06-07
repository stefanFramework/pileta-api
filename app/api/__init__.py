from flask import Flask
from flask_restful import Api

from api.routes.v1.utils import Utils

def create_app():
    app = Flask(__name__)
     # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@database/pileta_api'

    api = Api(app)
    api.add_resource(Utils, '/utils')

   
    return app