from .alembic import MigrateCommand
from flask_script import Server, Manager


def create_manager(app):
    manager = Manager(app)
    manager.add_command('db', MigrateCommand())
    manager.add_command('runserver', Server(host='0.0.0.0', port=80))

    return manager
