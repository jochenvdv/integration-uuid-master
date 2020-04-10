from flask import make_response, request
from flask.views import MethodView
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from uuid_master.utils import create_uuid
from uuid_master.schemas import create_resp_from_uuidmappings
from uuid_master.models import db, UuidMapping
from uuid_master.errors import create_404, create_400


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
        return make_response(create_resp_from_uuidmappings(uuid_mappings), 200)
    except NoResultFound:
        return create_404()


def create_uuidmapping():
    """
    Create a new UUID mapping

    Example: POST /uuids

    {
        "some_application_name": "some_application_id"
    }

    """
    from uuid_master.schemas import uuid_mapping_schema
    from uuid_master.models import known_applications

    try:
        uuid_mappings = uuid_mapping_schema.load(request.json)
    except ValidationError:
        return create_400()

    entities = []
    uuid = create_uuid()

    for app_name in uuid_mappings.keys():
        application = known_applications[app_name]
        entity = UuidMapping(
            uuid=uuid,
            application=application,
            app_local_id=uuid_mappings[app_name]
        )
        entities.append(entity)
        db.session.add(entity)

    db.session.commit()

    return make_response(
        create_resp_from_uuidmappings(entities),
        201,
        {'Location': f'/uuids/{uuid}'}
    )


def partially_update_uuidmapping_by_uuid(uuid):
    """
    Partially update a UUID mapping

    Example: PATCH /uuids/06a743ea-4797-4bdc-95f5-6352f2bd10eb

    {
        "some_application_name": "some_application_id"
    }

    """
    from uuid_master.schemas import uuid_mapping_schema
    from uuid_master.models import known_applications

    try:
        uuid_mappings = uuid_mapping_schema.load(request.json)
    except ValidationError:
        return create_400()

    existing_uuid_mappings = UuidMapping.query.filter(UuidMapping.uuid == uuid).all()

    if not existing_uuid_mappings:
        return create_404()

    entities = {m.application.application_name: m for m in existing_uuid_mappings}

    for app_name in uuid_mappings.keys():
        if app_name in entities:
            # update existing UuidMapping
            entities[app_name].app_local_id = uuid_mappings[app_name]
            db.session.merge(entities[app_name])
        else:
            # create new UuidMapping
            application = known_applications[app_name]
            entity = UuidMapping(
                uuid=uuid,
                application=application,
                app_local_id=uuid_mappings[app_name]
            )
            entities[app_name] = entity
            db.session.add(entity)

    db.session.commit()

    return make_response(create_resp_from_uuidmappings(list(entities.values())), 200)
