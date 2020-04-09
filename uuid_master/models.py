from flask_sqlalchemy import SQLAlchemy

from utils import create_api_key


db = SQLAlchemy()


class UuidMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=True)
    application = db.relationship('Application', db.backref('uuid_mappings', lazy=True))


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_name = db.Column(db.String(255), nullable=False)


class ApiKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(255), default=create_api_key, nullable=False)

    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=True)
    application = db.relationship('Application')

