sigterm_handler() { 
    echo "here"
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
    echo ""
    echo "     Services are up!"
    echo "     To visit the website, please navigate to:"

    echo ""
    echo ""
    printf "          * ${BLUE}$(tput bold)http://localhost:8080${NC}\n"
    printf "          * ${BLUE}$(tput bold)http://127.0.0.1:8080${NC}"
    echo ""
    echo ""
    echo ""
    echo ""
    read
} 
