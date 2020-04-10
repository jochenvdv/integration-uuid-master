from decouple import config


SQLALCHEMY_DATABASE_URI = config('DATABASE_URI', default='sqlite:////tmp/uuidmappings.db')
SQLALCHEMY_ECHO=True