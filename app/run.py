import config
from api import create_app
from api.routes import register_routes
from console import create_manager
from database import create_database

app = create_app(config.selected_config)
register_routes(app)
db = create_database(app)
manager = create_manager(app)

if __name__ == '__main__':
    manager.run()
