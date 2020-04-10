import json

from marshmallow import Schema, fields


_UUIDMAPPING_SCHEMA = None


def create_schema_from_app_list(applications):
    global _UUIDMAPPING_SCHEMA
    schema_fields = {a.application_name: fields.String() for a in applications}
    schema = Schema.from_dict(schema_fields)
    _UUIDMAPPING_SCHEMA = schema()


def create_resp_from_uuidmappings(uuid_mappings):
    if not isinstance(uuid_mappings, list):
        uuid_mappings = [uuid_mappings]

    resp = {m.application.application_name: m.app_local_id for m in uuid_mappings}

    return _UUIDMAPPING_SCHEMA.dump(resp)
