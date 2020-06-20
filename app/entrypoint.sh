#!/bin/sh

start () {
    ENVIRONMENT=$1; shift

    case $ENVIRONMENT in
        development)
            start_development
        ;;
        production)
            start_production
        ;;
        *)
            echo "[!] Invalid or no environment specified. Available environments: development, staging, production"
            exit 1
        ;;
    esac
}

start_development () {
    export PILETA_ENV=development
    python3 run.py runserver 
}

start_production () {
    echo "[!] Unavailable environment: production"
    exit 1
}

gen_migration() {
    python3 run.py db -o revision -a "$*"
}

migrate() {
    python3 run.py db -o migrate
}

downgrade() {
    python3 run.py db -o downgrade
}

help() {
    echo "Available Commands"
    echo ""
    echo "start: Starts aplication"
    echo "gen_migration: Creates a new migration file"
    echo "migrate: Executes migrations"
    echo "downgrade: Reverse last migration"
    echo ""
}

if [ $# -eq 0 ]; then
    echo "No commands supplied"
    help
    exit 1
fi

COMMAND=$1; shift
case $COMMAND in
    start)
        start $*
    ;;
    gen_migration)
        gen_migration $*
    ;;
    migrate)
        migrate
    ;;
    downgrade)
        downgrade
    ;;
    *)
        help
        echo "Invalid command $COMMAND"
        exit 1
    ;;
esac