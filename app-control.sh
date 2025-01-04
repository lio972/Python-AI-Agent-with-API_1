#!/bin/bash

# Application Control Script
# Usage: ./app-control.sh [start|stop|restart|status]

APP_NAME="ai-agent-calculator"
DOCKER_IMAGE="ai-agent-calculator"
PORT=5000

case "$1" in
  start)
    echo "Starting application..."
    docker build -t $DOCKER_IMAGE . && \
    docker run -d -p $PORT:$PORT --name $APP_NAME $DOCKER_IMAGE
    ;;
  stop)
    echo "Stopping application..."
    docker stop $APP_NAME && docker rm $APP_NAME
    ;;
  restart)
    echo "Restarting application..."
    docker stop $APP_NAME && docker rm $APP_NAME
    docker build -t $DOCKER_IMAGE . && \
    docker run -d -p $PORT:$PORT --name $APP_NAME $DOCKER_IMAGE
    ;;
  status)
    docker ps -a | grep $APP_NAME
    ;;
  *)
    echo "Usage: $0 {start|stop|restart|status}"
    exit 1
    ;;
esac
