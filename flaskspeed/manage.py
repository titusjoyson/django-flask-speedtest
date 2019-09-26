from flask_script import Manager
from app.speedtest.scripts import init_commands
from app import app

manager = Manager(app)
manager = init_commands(manager)

if __name__ == "__main__":
    manager.run()
