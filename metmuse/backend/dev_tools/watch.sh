#!/bin/bash
#
# **************************************************************
# Authored by Jack de Kock, https://github.com/jackdek11
# 25th June 2023
# **************************************************************
#

sigterm_handler() {
    tput reset
    cd ../../../quickstart/
    docker compose down rq-worker rq-scheduler
    cd -
    exit 1
}

## Setup signal trap
trap 'trap " " SIGINT SIGTERM SIGHUP; kill 0; wait; sigterm_handler' SIGINT SIGTERM SIGHUP

{
    cd ../../../quickstart/
    docker-compose up -d --build rq-worker rq-scheduler
    docker logs -f rq-worker
}