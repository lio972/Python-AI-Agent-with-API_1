# Python-AI-Agent-with-API_1

# AI Agent - Calculator with CLI and UI

The AI Agent is a Python-based calculator with both a **command-line interface (CLI)** and a **web-based user interface (UI)**. It supports basic and advanced mathematical operations, a **cancel operation** feature, and a **health check** functionality. It runs entirely within WebContainer's constraints and requires no external dependencies.

---

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division
- **Advanced Operations**: Square root and power calculations
- **Cancel Operation**: Stop the current operation
- **Health Check**: Check the system status and supported operations
- **Interactive CLI**: Simple command-line prompts for easy use
- **Web UI**: User-friendly interface for calculations
- **Error Handling**: Graceful handling of invalid inputs and operations
- **API Endpoints**: RESTful API for programmatic access
- **Docker Support**: Containerized deployment

---

## Available Operations

| Operation  | Description                     | Example Input       |
|------------|---------------------------------|---------------------|
| `add`      | Add two numbers                 | 5 + 3 = 8           |
| `subtract` | Subtract two numbers            | 5 - 3 = 2           |
| `multiply` | Multiply two numbers            | 5 * 3 = 15          |
| `divide`   | Divide two numbers              | 6 / 3 = 2           |
| `sqrt`     | Square root of a number         | √9 = 3              |
| `power`    | Raise a number to a power       | 2^3 = 8             |

---

## Getting Started

### 1. Running Locally

#### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

#### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/python_ai_agent_with_api_hkhu3t.git
cd python_ai_agent_with_api_hkhu3t

# Install dependencies
pip install -r requirements.txt
```

#### Running the Server
```bash
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
docker run -p 5000:5000 ai-agent-calculator
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
