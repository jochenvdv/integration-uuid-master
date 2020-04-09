from flask import Flask

from uuid_master.models import db
from uuid_master.endpoints import UuidMappingEndpoint


app = Flask(__name__)
app.config.from_pyfile('config.py')

app.add_url_rule('/uuids', view_func=UuidMappingEndpoint.as_view('uuid_mappings'))

db.init_app(app)