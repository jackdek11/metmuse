#!/bin/bash
#
# **************************************************************
# Authored by Jack de Kock, https://github.com/jackdek11
# 2nd June 2023
# **************************************************************
#

sigterm_handler() { 
    tput reset
    docker compose down --remove-orphans
    exit 1
}

## Setup signal trap
trap 'trap " " SIGINT SIGTERM SIGHUP; kill 0; wait; sigterm_handler' SIGINT SIGTERM SIGHUP

docker compose down --remove-orphans
{
    docker compose up --build -d 
    tput reset
    # Stall user, allow for rq processes to start before navigating to FE
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "[INFO] Bringing serverices up"
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "[INFO] Services almost up ..."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    echo "."
    sleep 0.75
    tput reset
    sleep 0.75
    BLUE='\033[0;34m'
    NC='\033[0m'
    echo ""
    echo ""
    echo "     The services are up!"
    echo ""
    echo "     To visit the website, navigate to:"
    echo ""
    printf "          * ${BLUE}$(tput bold)http://localhost:8080${NC}\n"
    echo ""
    echo ""
    echo "     To visit the admin panel, navigate to:"
    echo ""
    printf "          * ${BLUE}$(tput bold)http://localhost:8000/admin${NC}\n"
    echo ""
    echo ""
    echo ""
    read
} || {
    tput reset
    BLUE='\033[0;34m'
    NC='\033[0m'
    echo ""
    echo ""
    echo "     The was an issue bring up the services."
    echo "     Please ensure that you have follow the setup guide for running the project"
    echo ""
    printf "          * ${BLUE}$(tput bold)https://github.com/jackdek11/metmuse/blob/main/README.md${NC}\n"
    echo ""
    echo ""
}
