import uuid

from flask_sqlalchemy import SQLAlchemy

from uuid_master.utils import create_api_key, create_uuid


db = SQLAlchemy(session_options={"autoflush": False})
known_applications = None


def update_known_applications(applications):
    global known_applications
    known_applications = {a.application_name: a for a in applications}


class UuidMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), default=create_uuid, nullable=False)
    app_local_id = db.Column(db.String(255), nullable=False)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    application = db.relationship('Application', backref=db.backref('uuid_mappings', lazy=True))

    __table_args__ = (
        db.UniqueConstraint('application_id', 'app_local_id', name='uuid_app_id_unique_constraint'),
    )

    def __repr__(self):
        return f'UuidMapping[uuid={self.uuid}, application={self.application.application_name}, app_local_id={self.app_local_id}]'


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'Application[name={self.application_name}]'


class ApiKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(255), default=create_api_key, nullable=False)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=True)
    application = db.relationship('Application', backref=db.backref('api_key', lazy=True))

