# Python-AI-Agent-with-API_1

# AI Agent - Calculator with CLI and UI

The AI Agent is a Python-based calculator with both a **command-line interface (CLI)** and a **web-based user interface (UI)**. It supports basic and advanced mathematical operations, a **cancel operation** feature, and a **health check** functionality. It runs entirely within WebContainer's constraints and requires no external dependencies.

---

## System Components and Their Roles

### 1. CLI (Command Line Interface)
- **Purpose**: Provides direct command-line access to the calculator functionality
- **Usage**: Ideal for quick calculations and scripting
- **Features**:
  - Interactive prompt for operations
  - Supports all mathematical operations
  - Health check and cancel operation commands
- **File**: `agent.py`

### 2. Server
- **Purpose**: Hosts the web interface and API endpoints
- **Usage**: Serves as the backend for web UI and API access
- **Features**:
  - RESTful API endpoints
  - Web server for UI
  - Handles all calculation requests
- **Files**: `server.py` (Python) and `server.js` (Node.js)

### 3. Agent
- **Purpose**: Core calculation engine
- **Usage**: Performs all mathematical operations
- **Features**:
  - Implements all supported operations
  - Error handling for invalid inputs
  - Pure business logic implementation
- **Files**: `agent.py` and `agent.js`

### 4. API
- **Purpose**: Provides programmatic access to calculator functionality
- **Usage**: Integration with other applications
- **Features**:
  - RESTful endpoints for calculations
  - Health check endpoint
  - Cancel operation endpoint
- **Access**: Available through both server implementations

---

## Making API Calls

### Windows (Command Prompt)
```cmd
:: Calculate addition
curl -X POST http://localhost:5000/calculate ^
  -H "Content-Type: application/json" ^
  -d "{\"operation\": \"add\", \"numbers\": [5, 3]}"

:: Health check
curl -X GET http://localhost:5000/health

:: Cancel operation
curl -X POST http://localhost:5000/cancel
```

### Windows (PowerShell)
```powershell
# Calculate addition
Invoke-WebRequest -Uri http://localhost:5000/calculate `
  -Method POST `
  -Headers @{"Content-Type"="application/json"} `
  -Body '{"operation": "add", "numbers": [5, 3]}'

# Health check
Invoke-WebRequest -Uri http://localhost:5000/health -Method GET

# Cancel operation
Invoke-WebRequest -Uri http://localhost:5000/cancel -Method POST
```

### Linux (Bash)
```bash
# Calculate addition
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "numbers": [5, 3]}'

# Health check
curl -X GET http://localhost:5000/health

# Cancel operation
curl -X POST http://localhost:5000/cancel
```

---

## Docker Prerequisites

### For Windows:
1. Install Docker Desktop: https://docs.docker.com/desktop/install/windows-install/
2. Enable WSL 2 backend (recommended)
3. Allocate at least 4GB RAM in Docker settings
4. Enable Kubernetes if needed (optional)

### For Linux:
1. Install Docker Engine: https://docs.docker.com/engine/install/
2. Add your user to the docker group:
   ```bash
   sudo usermod -aG docker $USER
   newgrp docker
   ```
3. Verify installation:
   ```bash
   docker --version
   ```

---

## Essential Docker Commands (20/80 Rule)

### Basic Commands
```bash
# Build image
docker build -t <image-name> .

# Run container
docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>

# List running containers
docker ps

# List all containers
docker ps -a

# Stop container
docker stop <container-name>

# Remove container
docker rm <container-name>

# View logs
docker logs <container-name>

# Execute command in running container
docker exec -it <container-name> <command>
```

### Debugging Commands
```bash
# Inspect container details
docker inspect <container-name>

# View resource usage
docker stats <container-name>

# Copy files to/from container
docker cp <container-name>:<path> <local-path>
docker cp <local-path> <container-name>:<path>

# Remove unused images
docker image prune
```

### System Management
```bash
# List images
docker images

# Remove image
docker rmi <image-id>

# Clean up system
docker system prune

# View disk usage
docker system df
```

---

## Getting Started

### 1. Running Locally

#### Prerequisites
- Python 3.9 or higher
- Node.js (for server.js)
- npm (for Node.js dependencies)
- Docker (for containerized deployment)

#### Installation
```bash
# Install Node.js dependencies
npm install

# Make control script executable (Linux/Mac)
chmod +x app-control.sh
```

#### Application Control
```bash
# Linux/Mac
./app-control.sh start
./app-control.sh stop
./app-control.sh restart
./app-control.sh status

# Windows
.\app-control.ps1 start
.\app-control.ps1 stop
.\app-control.ps1 restart
.\app-control.ps1 status
```

#### Running the Server
```bash
# Node.js server
npm run start

# Python server
python3 server.py
```

#### Running the CLI
```bash
python3 agent.py
```

### 2. Running with Docker

#### Build the Docker Image
```bash
docker build -t ai-agent-calculator .
```

#### Run the Container
```bash
# Run in detached mode
docker run -d -p 5000:5000 --name ai-agent ai-agent-calculator

# Run in interactive mode
docker run -it -p 5000:5000 --name ai-agent ai-agent-calculator
```

#### Debugging and Container Access
```bash
# Get container logs
docker logs ai-agent

# Access running container shell
docker exec -it ai-agent /bin/bash

# Stop container
docker stop ai-agent

# Remove container
docker rm ai-agent
```

### 3. Accessing the Web UI
Open your browser and navigate to:
```
http://localhost:5000
```

---

## API Documentation

The AI Agent provides RESTful API endpoints for programmatic access:

### 1. Calculate Operation
**Endpoint**: `POST /calculate`

**Request Body**:
```json
{
  "operation": "add",
  "numbers": [5, 3]
}
```

**Response**:
```json
{
  "result": 8
}
```

### 2. Cancel Operation
**Endpoint**: `POST /cancel`

**Response**:
```json
{
  "message": "Operation canceled"
}
```

### 3. Health Check
**Endpoint**: `GET /health`

**Response**:
```json
{
  "status": "healthy",
  "operations_supported": ["add", "subtract", "multiply", "divide", "sqrt", "power"],
  "current_operation": null
}
```

---

## Usage Examples

### Web UI Usage
1. Select Operation: Choose an operation from the dropdown menu
2. Enter Numbers: Provide the required numbers in the input fields
3. Calculate: Click the "Calculate" button to see the result
4. Cancel Operation: Click the "Cancel" button to stop the current operation
5. Health Check: Click the "Health Check" button to view system status

### CLI Usage
```bash
$ python3 agent.py
AI Agent Calculator
Available operations: add, subtract, multiply, divide, sqrt, power
Type 'cancel' to cancel the current operation or 'health' to check status.

Enter operation: add
Enter first number: 5
Enter second number: 3
Result: 8.0

Enter operation: health
Status: {'status': 'healthy', 'operations_supported': ['add', 'subtract', 'multiply', 'divide', 'sqrt', 'power'], 'current_operation': 'add'}

Enter operation: cancel
Operation canceled.

Enter operation: exit
```

### API Usage Example (cURL)
```bash
# Calculate addition
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "numbers": [5, 3]}'

# Health check
curl -X GET http://localhost:5000/health

# Cancel operation
curl -X POST http://localhost:5000/cancel
```

---

## Development

This project was developed to work within WebContainer's constraints:
- No external dependencies
- Uses only Python standard library
- Runs entirely in the browser environment

---

## License

This project is open-source and available for use under the MIT License.
