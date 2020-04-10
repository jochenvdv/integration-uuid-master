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

    application1 = Application(application_name='bestapp')
    application2 = Application(application_name='someotherapp')
    api_key1 = ApiKey(application=application1)
    api_key2 = ApiKey(application=application2)
    db.session.add(application1)
    db.session.add(application2)
    db.session.add(api_key1)
    db.session.add(api_key2)

    db.session.commit()
    return db
