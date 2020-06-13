
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



COMMAND=$1; shift
case $COMMAND in
    start)
        start $*
    ;;
    migrate)
        migrate $*
    ;;
    *)
        echo "Invalid command $COMMAND"
        exit 1
    ;;
esac