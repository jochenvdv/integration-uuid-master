import json


def uuidmapping_to_json(uuid_mappings):
    if not isinstance(uuid_mappings, list):
        uuid_mappings = [uuid_mappings]

    resp = { m.application.application_name: m.app_local_id for m in uuid_mappings }
    return json.dumps(resp)