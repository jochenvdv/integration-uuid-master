from decouple import config


DATABASE_URI = config('DATABASE_URI', default='sqlite:////tmp/uuidmappings.db')