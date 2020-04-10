from flask import Flask

from uuid_master.models import db, Application, ApiKey, UuidMapping
from uuid_master.endpoints import get_uuidmapping_by_uuid
from uuid_master.schemas import create_schema_from_app_list


def load_applications():
    applications = Application.query.all()
    create_schema_from_app_list(applications)


def create_app():
    # create app object from config
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # register routes & auth
    app.add_url_rule('/uuids/<uuid>', view_func=get_uuidmapping_by_uuid)

    # initialize SQLAlchemy
    db.init_app(app)

    # generate validation schema based on applications known in database
    app.before_first_request(load_applications)

    return app


app = create_app()

with app.app_context():
    db.create_all(app=app)
    application = Application(application_name='bestapp')
    application2 = Application(application_name='someotherapp')
    api_key = ApiKey(application=application)
    api_key2 = ApiKey(application=application2)
    uuid_mapping = UuidMapping(app_local_id='1234', application=application)
    db.session.add(application)
    db.session.add(api_key)
    db.session.add(uuid_mapping)
    db.session.commit()
    uuid_mapping2 = UuidMapping(uuid=uuid_mapping.uuid, app_local_id='some_app_id', application=application2)
    db.session.add(uuid_mapping2)
    db.session.commit()
    print(uuid_mapping.uuid)