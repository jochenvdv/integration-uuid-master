#!/usr/bin/env bash
rm /tmp/uuidmappings.db
export FLASK_ENV=development
export FLASK_APP=./uuid_master/app.py
python -m flask run