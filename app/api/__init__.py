from flask import Flask
# from flask_restful import Api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@database/pileta_api'
    return app

#
# def init_api(app):
#     api = Api(app)
#     api.add_resource(TodoSimple, '/<string:todo_id>')