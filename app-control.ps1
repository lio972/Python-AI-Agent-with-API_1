<#
.SYNOPSIS
Application Control Script for Windows

.DESCRIPTION
This script provides start, stop, restart, and status control for the AI Agent application using Docker.

.PARAMETER Action
The action to perform: start, stop, restart, or status

.EXAMPLE
.\app-control.ps1 start
.\app-control.ps1 stop
.\app-control.ps1 restart
.\app-control.ps1 status
#>

param (
    [string]$Action = "help"
)

$APP_NAME = "ai-agent-calculator"
$DOCKER_IMAGE = "ai-agent-calculator"
$PORT = 5000

switch ($Action.ToLower()) {
    "start" {
        Write-Host "Starting application..."
        docker build -t $DOCKER_IMAGE .
        docker run -d -p ${PORT}:${PORT} --name $APP_NAME $DOCKER_IMAGE
    }
    "stop" {
        Write-Host "Stopping application..."
        docker stop $APP_NAME
        docker rm $APP_NAME
    }
    "restart" {
        Write-Host "Restarting application..."
        docker stop $APP_NAME
        docker rm $APP_NAME
        docker build -t $DOCKER_IMAGE .
        docker run -d -p ${PORT}:${PORT} --name $APP_NAME $DOCKER_IMAGE
    }
    "status" {
        docker ps -a | Select-String $APP_NAME
    }
    default {
        Write-Host "Usage: .\app-control.ps1 {start|stop|restart|status}"
    }
}
