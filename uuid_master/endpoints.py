from flask import make_response
from flask.views import MethodView
from sqlalchemy.orm.exc import NoResultFound

from uuid_master.models import db, UuidMapping


class UuidMappingEndpoint(MethodView):
    def post(self):
        """
        Create a new UUID mapping

        Example: POST /

        {
            "some_application_name": "some_application_id"
        }

        """
        UuidMapping.from_req
        pass

    def patch(self, uuid):
        """
        Partially update a UUID mapping

        Example: PATCH /06a743ea-4797-4bdc-95f5-6352f2bd10eb

        {
            "some_application_name": "some_application_id"
        }

        """
    pass
