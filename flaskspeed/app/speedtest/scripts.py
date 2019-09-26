from .views import OrmSpeedTest


def init_commands(manager):
    manager.add_command('orm_speed_test', OrmSpeedTest())
    return manager