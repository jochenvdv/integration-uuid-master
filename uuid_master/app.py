from flask import Flask

from uuid_master.models import db, Application, ApiKey, UuidMapping
from uuid_master.endpoints import get_uuidmapping_by_uuid

# create app object from config
app = Flask(__name__)
app.config.from_pyfile('config.py')

# register routes & auth
app.add_url_rule('/uuids/<uuid>', view_func=get_uuidmapping_by_uuid)

db.init_app(app)

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