#!/bin/sh

print_bold() {
    MESSAGE=$1; shift
    echo "\033[1;32m$MESSAGE\033[0m"
}

help_menu() {
   print_bold "Available Commands"
    echo ""
    echo "\033[1;34mbuild\033[0m    Build all the images"
    echo "start    Runs all the containers"
    echo "\033[1;34mstop\033[0m     Stops all the containers"
    echo "restart  Restart all the containers"
    echo "\033[1;34mtests\033[0m    Run unit test suite"
    echo "logs     Executes a tail -f to the application logs"
    echo "\033[1;34mexecute\033[0m  Executes a command inside de container"
    echo ""
}

build() {
    print_bold "Building ..."
    docker-compose build
    print_bold "Building Succesfull"
}

start() {
    docker-compose up -d
}

stop() {
    docker-compose down
}

restart() {
    stop
    start
}

tests() {
    echo "No Test suite available at the moment"
}

logs() {
    docker logs -f pileta_api
}

execute() {
    docker exec pileta_api sh entrypoint.sh "$@"
}

COMMAND=$1; shift
case $COMMAND in
    execute)
        execute $*
    ;;
    build)
        build
    ;;
    start)
        start
    ;;
    stop)
        stop
    ;;
    restart)
        restart
    ;;
    tests)
        tests
    ;;
    logs)
        logs
    ;;
    *)
        help_menu
        echo "Invalid command $COMMAND"
        exit 1
    ;;
esac