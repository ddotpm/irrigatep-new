#!/bin/bash

# Function to display help message
show_help() {
    echo "Development script for IrrigateP"
    echo
    echo "Usage:"
    echo "  ./dev.sh [command]"
    echo
    echo "Commands:"
    echo "  up              Start development environment"
    echo "  down            Stop development environment"
    echo "  logs            Show logs from all services"
    echo "  migrate         Run database migrations"
    echo "  shell-backend   Open a shell in the backend container"
    echo "  shell-frontend  Open a shell in the frontend container"
    echo "  test           Run tests"
    echo "  help           Show this help message"
}

# Check if command is provided
if [ $# -eq 0 ]; then
    show_help
    exit 1
fi

# Process commands
case "$1" in
    up)
        docker-compose up -d
        ;;
    down)
        docker-compose down
        ;;
    logs)
        docker-compose logs -f
        ;;
    migrate)
        docker-compose exec backend alembic upgrade head
        ;;
    shell-backend)
        docker-compose exec backend /bin/bash
        ;;
    shell-frontend)
        docker-compose exec frontend /bin/sh
        ;;
    test)
        docker-compose exec backend pytest
        ;;
    help)
        show_help
        ;;
    *)
        echo "Unknown command: $1"
        show_help
        exit 1
        ;;
esac 