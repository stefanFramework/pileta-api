from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_database(app):
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    return db
