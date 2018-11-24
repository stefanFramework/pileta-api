#!/bin/sh
APP_NAME="pileta-api"
EXTERNAL_PORT=4000
INTERNAL_PORT=80

print_bold() {
    MESSAGE=$1; shift
    echo "\033[1;32m$MESSAGE\033[0m"
}

stop_app() {
    CONTAINER_ID=$(docker ps -aqf "name=$APP_NAME")

    # if process exists, then stop and remove
    if [ ! -z "$CONTAINER_ID" ]; then
        docker stop $CONTAINER_ID && docker rm $CONTAINER_ID
    fi
}

build() {
    print_bold "Building $APP_NAME ..."
    stop_app && docker rmi -f $(docker images -q $APP_NAME) && docker build -t $APP_NAME .
    print_bold "Succesfully created image $APP_NAME"
}

start() {
    print_bold "Starting $APP_NAME ..."
    stop_app && docker run -d -p $EXTERNAL_PORT:$INTERNAL_PORT --name $APP_NAME $APP_NAME
    print_bold "$APP_NAME is up and running"
}

stop() {
    print_bold "Stopping $APP_NAME ..."
    stop_app
    print_bold "$APP_NAME successfully stopped"
}

tests() {
    echo "No Test suite available at the moment"
}

logs() {
    echo "No Log files available at the moment"
}

help_menu() {
    # echo "\033[1;32m$MESSAGE\033[0m"
    print_bold "Available Commands"
    echo ""
    echo "\033[1;34mbuild\033[0m    Build the Docker Image"
    echo "start    Runs the Docker Container"
    echo "\033[1;34mstop\033[0m     Stops the Docker Container"
    echo "tests    Run unit test suite"
    echo "\033[1;34mlogs\033[0m     tail -f to the application logs"
    echo ""
}

COMMAND=$1; shift
case $COMMAND in
    build)
        build
    ;;
    start)
        start
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