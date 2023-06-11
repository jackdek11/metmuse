#!/bin/sh
#
# **************************************************************
# Authored by Jack de Kock, https://github.com/jackdek11
# 11th June 2023
# **************************************************************
#

python3 manage.py migrate
python3 manage.py add_admin
python3 manage.py collectstatic --noinput
python3 manage.py loaddata fixtures/*
python3 -m uvicorn backend.asgi:application --host 0.0.0.0
