from flask import Flask, g, current_app

from uuid_master.models import db, Application, ApiKey, UuidMapping, update_known_applications
from uuid_master.endpoints import get_uuidmapping_by_uuid, create_uuidmapping, partially_update_uuidmapping_by_uuid
from uuid_master.schemas import create_schema_from_app_list


def load_applications():
    """
    Loads configured application names into the database:
    """
    configured_apps = current_app.config['KNOWN_APPLICATIONS']
    apps_in_db = [app.application_name for app in Application.query.all()]

    for configured_app in configured_apps:
        if configured_app not in apps_in_db:
            # store configured app in db if not yet present
            new_app = Application(application_name=configured_app)
            new_api_key = ApiKey(application=new_app)
            db.session.add(new_app)
            db.session.add(new_api_key)
            apps_in_db.append(new_app)
            print(f"Configured app '{configured_app}' with api key '{new_api_key.api_key}'")

    db.session.commit()

    # reload application list from db and generate schema
    apps_in_db = Application.query.all()
    create_schema_from_app_list(apps_in_db)
    update_known_applications(apps_in_db)


def create_app():
    """
    Creates & configures the Flask app object:
    """
    # create app object from config
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # generate validation schema based on applications known in database
    app.before_first_request(load_applications)

    # register routes & auth
    app.add_url_rule('/uuids/<uuid>', methods=['GET'], view_func=get_uuidmapping_by_uuid)
    app.add_url_rule('/uuids', methods=['POST'], view_func=create_uuidmapping)
    app.add_url_rule('/uuids/<uuid>', methods=['PATCH'], view_func=partially_update_uuidmapping_by_uuid)


    # initialize SQLAlchemy
    db.init_app(app)

    return app


# launch app
app = create_app()
db.create_all(app=app)
