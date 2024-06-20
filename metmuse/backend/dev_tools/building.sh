#!/bin/sh
#
# **************************************************************
# Authored by Jack de Kock, https://github.com/jackdek11
# 11th June 2023
# **************************************************************
#

# shellcheck disable=SC2164
cd ../../../quickstart/
docker-compose down --remove-orphans
docker-compose up -d db redis
# shellcheck disable=SC2164
cd ../metmuse/backend/
sleep 8
python3 manage.py migrate
python3 manage.py add_admin
python3 manage.py loaddata fixtures/*
python3 manage.py runserver
