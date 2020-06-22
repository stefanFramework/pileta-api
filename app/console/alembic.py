import os
from os.path import normpath, join, abspath, dirname
from flask_script import Command, Option
from alembic import command as AlembicCommand
from alembic.config import Config as AlembicConfig

alembic_path = normpath(join(abspath(dirname(__file__)), '../migrations'))

config = AlembicConfig(join(alembic_path, 'alembic.ini'))


class MigrateCommand(Command):

    MIGRATE = 'migrate'
    DOWNGRADE = 'downgrade'
    GEN_MIGRATION = 'revision'

    option_list = [
        Option('--operation', '-o', dest='operation'),
        Option('--arg', '-a', dest='arg')
    ]

    def run(self, operation, arg):
        if operation == self.GEN_MIGRATION:
            self._gen_migration(arg)
            return

        if operation == self.MIGRATE:
            self._migrate()
            return

        if operation == self.DOWNGRADE:
            self._downgrade()
            return

        print('Invalid Operation: ' + operation)

    def _gen_migration(self, message):
        AlembicCommand.revision(config, message)

    def _migrate(self):
        AlembicCommand.upgrade(config, 'head')

    def _downgrade(self):
        AlembicCommand.downgrade(config, '-1')
