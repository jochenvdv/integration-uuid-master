#!/usr/bin/env bash
mkdir -p /opt/uuid-master
poetry run gunicorn \
  -b localhost:5000 \
  -e SQLALCHEMY_DATABASE_URI="sqlite:////opt/uuid-master/database.sqlite" \
  uuid_master.app:app