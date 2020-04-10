from marshmallow import Schema, fields


uuid_mapping_schema = None


def create_schema_from_app_list(applications):
    global uuid_mapping_schema
    schema_fields = {a.application_name: fields.String() for a in applications}
    schema = Schema.from_dict(schema_fields)
    uuid_mapping_schema = schema()


def create_resp_from_uuidmappings(uuid_mappings):
    if not isinstance(uuid_mappings, list):
        uuid_mappings = [uuid_mappings]

    resp = {m.application.application_name: m.app_local_id for m in uuid_mappings}

    return uuid_mapping_schema.dump(resp)
