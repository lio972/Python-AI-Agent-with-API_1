# Python-AI-Agent-with-API_1

# AI Agent - Calculator with CLI and UI

The AI Agent is a Python-based calculator with both a **command-line interface (CLI)** and a **web-based user interface (UI)**. It supports basic and advanced mathematical operations, a **cancel operation** feature, and a **health check** functionality. It runs entirely within WebContainer's constraints and requires no external dependencies.

---

## Cloud and Server Deployment Security

When deploying the AI Agent to cloud environments or production servers, additional security measures must be implemented to protect against common attacks. Below are key security considerations and implementations:

### 1. Network Security
- **Implementation**:
  ```bash
  # Use security groups (AWS) or firewall rules (GCP/Azure)
  # Allow only necessary ports (e.g., 443 for HTTPS)
  # Block all other incoming traffic
  ```
- **Best Practices**:
  - Use Virtual Private Cloud (VPC) with private subnets
  - Implement Network Access Control Lists (NACLs)
  - Use security groups with least privilege principle
  - Enable VPC flow logs for monitoring

### 2. Web Application Firewall (WAF)
- **Implementation**:
  ```bash
  # AWS WAF example
  aws waf create-web-acl --name MyWebACL \
    --default-action "Block" \
    --scope REGIONAL \
    --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=MyWebACLMetric
  ```
- **Best Practices**:
  - Enable WAF with OWASP Top 10 rules
  - Block common attack patterns (SQLi, XSS, etc.)
  - Set up rate-based rules
  - Monitor and analyze blocked requests

### 3. DDoS Protection
- **Implementation**:
  ```bash
  # AWS Shield Advanced example
  aws shield create-protection --name MyDDoSProtection \
    --resource-arn arn:aws:elasticloadbalancing:region:account-id:loadbalancer/app/MyLoadBalancer/50dc6c495c0c9188
  ```
- **Best Practices**:
  - Enable DDoS protection services (AWS Shield, Cloudflare, etc.)
  - Use Content Delivery Network (CDN)
  - Implement auto-scaling for traffic spikes
  - Set up health checks and failover

### 4. Data Encryption
- **Implementation**:
  ```bash
  # Enable SSL/TLS
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
  ```
- **Best Practices**:
  - Use HTTPS with strong TLS configurations (TLS 1.2+)
  - Encrypt data at rest (AES-256)
  - Use KMS for key management
  - Implement certificate rotation

### 5. Access Control
- **Implementation**:
  ```bash
  # IAM policy example
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:GetObject"
        ],
        "Resource": "arn:aws:s3:::my-bucket/*"
      }
    ]
  }
  ```
- **Best Practices**:
  - Implement least privilege access
  - Use IAM roles instead of access keys
  - Enable multi-factor authentication (MFA)
  - Regularly review permissions

### 6. Monitoring and Logging
- **Implementation**:
  ```bash
  # CloudWatch Logs example
  aws logs create-log-group --log-group-name MyAppLogs
  aws logs create-log-stream --log-group-name MyAppLogs --log-stream-name MyAppStream
  ```
- **Best Practices**:
  - Enable CloudTrail for API logging
  - Set up CloudWatch alarms
  - Implement centralized logging
  - Use SIEM tools for threat detection

### 7. Container Security
- **Implementation**:
  ```bash
  # Docker security scan
  docker scan my-image
  ```
- **Best Practices**:
  - Use minimal base images
  - Scan images for vulnerabilities
  - Implement image signing
  - Use container runtime security tools

### 8. Secret Management
- **Implementation**:
  ```bash
  # AWS Secrets Manager example
  aws secretsmanager create-secret --name MySecret --secret-string '{"username":"admin","password":"P@ssw0rd"}'
  ```
- **Best Practices**:
  - Never hardcode secrets
  - Use secret management services
  - Rotate secrets regularly
  - Restrict access to secrets

### 9. Backup and Disaster Recovery
- **Implementation**:
  ```bash
  # AWS Backup example
  aws backup create-backup-vault --backup-vault-name MyBackupVault
  aws backup create-backup-plan --backup-plan file://backup-plan.json
  ```
- **Best Practices**:
  - Implement automated backups
  - Test recovery procedures
  - Use multi-region replication
  - Maintain backup retention policies

### 10. Patch Management
- **Implementation**:
  ```bash
  # Automated patching example
  sudo apt-get update && sudo apt-get upgrade -y
  ```
- **Best Practices**:
  - Implement automated patching
  - Monitor for security updates
  - Test patches in staging
  - Maintain patch schedules

---

## System Architecture

### Architecture Overview
```
+-------------------+       +-------------------+       +-------------------+
|    Web Browser    |       |   Command Line    |       | External Systems  |
|   (User Interface)|       |  Interface (CLI)  |       |   (API Clients)   |
+--------+----------+       +---------+---------+       +---------+---------+
         |                            |                           |
         |                            |                           |
         v                            v                           v
+--------+----------+       +---------+---------+       +---------+---------+
|   Web Server      |<----->|   Agent Core      |<----->|   REST API        |
| (server.py/js)    |       | (agent.py/js)     |       | Endpoints         |
+--------+----------+       +---------+---------+       +---------+---------+
         |                            |                           |
         |                            |                           |
         v                            v                           v
+--------+----------+       +---------+---------+       +---------+---------+
|  HTTP Requests    |       |  Direct Calls     |       |  HTTP Requests    |
|  (HTML/JSON)      |       |  (Python/JS)      |       |  (JSON)           |
+-------------------+       +-------------------+       +-------------------+
```

### Component Roles and Interactions

1. **Web Browser (UI)**
   - **Role**: Provides user-friendly interface for calculations
   - **Interactions**:
     - Sends HTTP requests to Web Server
     - Receives HTML/JSON responses
     - Handles user input/output

2. **Command Line Interface (CLI)**
   - **Role**: Direct access to calculator functionality
   - **Interactions**:
     - Directly calls Agent Core methods
     - Handles text-based input/output
     - Provides immediate feedback

3. **Web Server**
   - **Role**: Handles HTTP requests and serves UI/API
   - **Interactions**:
     - Receives requests from Web Browser and API clients
     - Calls Agent Core for calculations
     - Returns HTML/JSON responses

4. **Agent Core**
   - **Role**: Performs all mathematical operations
   - **Interactions**:
     - Receives requests from Web Server and CLI
     - Performs calculations
     - Returns results to caller

5. **REST API**
   - **Role**: Provides programmatic access to calculator
   - **Interactions**:
     - Receives JSON requests from external systems
     - Calls Agent Core for calculations
     - Returns JSON responses

---

## Security Best Practices

### 1. Input Validation
- **Implementation**:
  ```python
  def validate_input(numbers, operation):
      if not isinstance(numbers, list):
          raise ValueError("Numbers must be a list")
      if operation not in VALID_OPERATIONS:
          raise ValueError("Invalid operation")
      for num in numbers:
          if not isinstance(num, (int, float)):
              raise ValueError("Numbers must be numeric")
  ```
- **Best Practices**:
  - Validate all user inputs
  - Use strict type checking
  - Implement range checks for numbers

### 2. Rate Limiting
- **Implementation** (using Express.js middleware):
  ```javascript
  const rateLimit = require('express-rate-limit');

  const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100 // limit each IP to 100 requests per windowMs
  });

  app.use(limiter);
  ```
- **Best Practices**:
  - Implement rate limiting on API endpoints
  - Use appropriate window sizes
  - Provide clear rate limit headers

### 3. HTTPS Enforcement
- **Implementation** (in production):
  ```javascript
  app.use((req, res, next) => {
    if (!req.secure) {
      return res.redirect('https://' + req.headers.host + req.url);
    }
    next();
  });
  ```
- **Best Practices**:
  - Always use HTTPS in production
  - Redirect HTTP to HTTPS
  - Use HSTS headers

### 4. Security Headers
- **Implementation**:
  ```javascript
  const helmet = require('helmet');
  app.use(helmet());
  ```
- **Best Practices**:
  - Set Content Security Policy (CSP)
  - Enable XSS protection
  - Prevent MIME type sniffing
  - Set X-Frame-Options

### 5. Error Handling
- **Implementation**:
  ```python
  try:
      result = agent.calculate(operation, *numbers)
  except Exception as e:
      return {
          'error': str(e),
          'status': 400
      }
  ```
- **Best Practices**:
  - Never expose stack traces
  - Use generic error messages
  - Log errors securely

### 6. Authentication (for API)
- **Implementation** (Basic Auth example):
  ```javascript
  const basicAuth = require('express-basic-auth');

  app.use('/api', basicAuth({
    users: { 'admin': 'securepassword' },
    challenge: true
  }));
  ```
- **Best Practices**:
  - Use token-based authentication (JWT)
  - Implement proper password hashing
  - Use secure session management

### 7. Dependency Security
- **Implementation**:
  ```bash
  npm audit
  pip-audit
  ```
- **Best Practices**:
  - Regularly update dependencies
  - Use security scanners
  - Remove unused dependencies

### 8. Logging and Monitoring
- **Implementation**:
  ```javascript
  const morgan = require('morgan');
  app.use(morgan('combined'));
  ```
- **Best Practices**:
  - Log security-relevant events
  - Implement log rotation
  - Monitor for suspicious activity

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
