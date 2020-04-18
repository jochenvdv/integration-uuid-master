import os

from pytest import fixture

from uuid_master.app import create_app
from uuid_master.models import db


if os.path.exists('/tmp/uuidmappings_test.db'):
    os.unlink('/tmp/uuidmappings_test.db')


@fixture(scope='function')
def app():
    app = create_app()
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/uuidmappings_test.db'

    with app.app_context():
        db.create_all()

    return app
