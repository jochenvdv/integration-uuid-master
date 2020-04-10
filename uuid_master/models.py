import uuid

from flask_sqlalchemy import SQLAlchemy

from uuid_master.utils import create_api_key, create_uuid


db = SQLAlchemy()
known_applications = None


def update_known_applications(applications):
    global known_applications
    known_applications = {a.application_name: a for a in applications}
    print(known_applications)


class UuidMapping(db.Model):
    # TODO: add composite unique constraint on 'uuid' & 'application.name'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), default=create_uuid, nullable=False)
    app_local_id = db.Column(db.String(255), nullable=False)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=True)
    application = db.relationship('Application', backref=db.backref('uuid_mappings', lazy=True))


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_name = db.Column(db.String(255), nullable=False)


class ApiKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(255), default=create_api_key, nullable=False)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=True)
    application = db.relationship('Application', backref=db.backref('api_key', lazy=True))

