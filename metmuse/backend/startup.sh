#!/bin/sh

sudo rm db.sqlite3
python3 manage.py migrate
python3 manage.py loaddata fixtures.json
python3 manage.py runserver