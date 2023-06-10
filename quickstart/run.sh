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
    BLUE='\033[0;34m'
    NC='\033[0m'
    echo ""
    echo ""
    echo "     The services are up!"
    echo ""
    echo "     To visit the website, please navigate to:"
    echo ""
    printf "          * ${BLUE}$(tput bold)http://localhost:8080${NC}\n"
    echo ""
    echo ""
    echo "     To view the admin panel, please navigate to:"
    echo ""
    printf "          * ${BLUE}$(tput bold)http://localhost:8000/admin${NC}\n"
    echo ""
    echo ""
    echo ""
    read
}
