from app import create_app
from database import register_session
from console import create_manager

app = create_app()
register_session(app)
manager = create_manager(app)

if __name__ == '__main__':
    manager.run()
