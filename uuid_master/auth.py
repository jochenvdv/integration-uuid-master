from flask import g, request, make_response
from sqlalchemy.orm.exc import NoResultFound

from uuid_master.models import ApiKey
from uuid_master.errors import create_401

_API_KEY_HEADER = 'x-apikey'


def verify_auth():
    if not _API_KEY_HEADER in request.headers:
        return make_response('Unauthorized', 401)

    api_key = request.headers[_API_KEY_HEADER]

    try:
        api_key = ApiKey.query.filter(ApiKey.api_key == api_key).one()
        g.auth_application = api_key.application
    except NoResultFound:
        return create_401()
