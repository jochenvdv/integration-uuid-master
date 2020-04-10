from pytest import fixture

from uuid_master.app import create_app
from uuid_master.models import db, Application, ApiKey, UuidMapping


@fixture(scope='session')
def app():
    app = create_app()
    app.config['SQLALCHEMY_ECHO'] = False
    return app


@fixture(scope='session')
def _db(app):
    db.init_app(app)
    db.create_all(app=app)

    return db
