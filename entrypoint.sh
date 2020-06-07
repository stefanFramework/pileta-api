#!/usr/bin/env bash

print_bold() {
    MESSAGE=$1; shift
    echo "\033[1;32m$MESSAGE\033[0m"
}

help_menu() {
   print_bold "Available Commands"
    echo ""
    echo "\033[1;34mbuild\033[0m    Build all the images"
    echo "run      Runs all the containers"
    echo "\033[1;34mstop\033[0m     Stops all the containers"
    echo "tests    Run unit test suite"
    echo "\033[1;34mlogs\033[0m     tail -f to the application logs"
    echo ""
}

build() {
    print_bold "Building ..."
    docker-compose build
    #docker-compose run --rm database sh -c "mysql -uroot -proot -ppileta_api < db/pileta_api.sql"
    print_bold "Building Succesfull"
}

run() {
    docker-compose up -d
}

stop() {
    docker-compose down
}

tests() {
    echo "No Test suite available at the moment"
}

logs() {
    echo "No Log files available at the moment"
}

COMMAND=$1; shift
case $COMMAND in
    build)
        build
    ;;
    run)
        run
    ;;
    stop)
        stop
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