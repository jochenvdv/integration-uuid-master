from flask import make_response
from flask.views import MethodView
from sqlalchemy.orm.exc import NoResultFound

from uuid_master.mapping import uuidmapping_to_json
from uuid_master.models import db, UuidMapping
from uuid_master.errors import return_404


def get_uuidmapping_by_uuid(uuid):
    """
    Retrieve a UUID mapping

    Example: GET /uuids/06a743ea-4797-4bdc-95f5-6352f2bd10eb

    {
        "some_application_name": "some_application_id"
    }

    """
    try:
        uuid_mappings = UuidMapping.query.filter(UuidMapping.uuid == uuid).all()
        return make_response(uuidmapping_to_json(uuid_mappings), 200)
    except NoResultFound:
        return_404()


def create_uuidmapping():
    """
    Create a new UUID mapping

    Example: POST /uuids

    {
        "some_application_name": "some_application_id"
    }

    """
pass


def partially_update_uuidmapping_by_uuid(uuid):
    """
    Partially update a UUID mapping

    Example: PATCH /uuids/06a743ea-4797-4bdc-95f5-6352f2bd10eb

    {
        "some_application_name": "some_application_id"
    }

    """
pass
