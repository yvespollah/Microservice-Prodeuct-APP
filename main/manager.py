from main import app, db
from flask_migrate import Migrate
from flask_script import Manager

migrate = Migrate(app, db)
manager = Manager(app)

# Ajout manuel des commandes de migration
@manager.command
def db_init():
    """Initialise la base de données"""
    from flask_migrate import init
    init()

@manager.command
def db_migrate():
    """Crée une nouvelle migration"""
    from flask_migrate import migrate
    migrate()

@manager.command
def db_upgrade():
    """Applique les migrations"""
    from flask_migrate import upgrade
    upgrade()

@manager.command
def db_downgrade():
    """Annule la dernière migration"""
    from flask_migrate import downgrade
    downgrade()

if __name__ == '__main__':
    manager.run()
