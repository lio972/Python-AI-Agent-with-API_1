# Release Notes: AI Agent Calculator v1.0.0

## Overview
This release introduces the **AI Agent Calculator**, a powerful tool with both a **command-line interface (CLI)** and a **web-based user interface (UI)**. It supports basic and advanced mathematical operations, a **cancel operation** feature, and a **health check** functionality. This version is stable and ready for production use.

---

## New Features

### 1. **Command-Line Interface (CLI)**
- Interactive command-line interface for quick calculations
- Supports all basic and advanced operations:
  - Addition (`add`)
  - Subtraction (`subtract`)
  - Multiplication (`multiply`)
  - Division (`divide`)
  - Square root (`sqrt`)
  - Power (`power`)
- Cancel operation functionality (`cancel`)
- Health check command (`health`) to display system status

### 2. **Web-Based User Interface (UI)**
- User-friendly web interface for calculations
- Dropdown menu for operation selection
- Real-time result display
- Cancel operation button
- Health check button to view system status

### 3. **RESTful API**
- Programmatic access to calculator functionality
- Endpoints:
  - `POST /calculate`: Perform calculations
  - `POST /cancel`: Cancel current operation
  - `GET /health`: Check system status
- JSON-based request/response format
- Detailed API documentation included

### 4. **Docker Support**
- Containerized deployment using Docker
- Pre-built Docker image available
- Easy deployment to cloud or on-premise environments

### 5. **Security Features**
- Input validation for all operations
- Rate limiting to prevent abuse
- HTTPS enforcement for secure communication
- Basic authentication for API endpoints

---

## Bug Fixes
- Fixed division by zero error in `agent.py`
- Resolved UI display issues for negative results
- Corrected API response format for error cases
- Fixed Docker build issues for ARM-based systems (e.g., Raspberry Pi)

---

## Improvements
- Refactored core calculation logic for better performance
- Improved error handling in CLI and API
- Added unit tests for all operations
- Updated documentation with detailed usage examples
- Optimized Docker image size

---

## Known Issues
- Square root operation may return incorrect results for very large numbers
- Health check endpoint does not include memory usage information
- UI may not render correctly on older browsers

---

## Installation Instructions

### 1. Running Locally
```bash
# Clone the repository
git clone https://github.com/lio972/Python-AI-Agent-with-API_1.git
cd Python-AI-Agent-with-API_1

# Install dependencies
npm install

# Start the server
npm run start
```

### 2. Running with Docker
```bash
# Build the Docker image
docker build -t ai-agent-calculator .

# Run the container
docker run -d -p 5000:5000 --name ai-agent ai-agent-calculator
```

### 3. Accessing the Web UI
Open your browser and navigate to:
```
http://localhost:5000
```

---

## API Usage Examples

### Calculate Addition (cURL)
```bash
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "numbers": [5, 3]}'
```

### Health Check (cURL)
```bash
curl -X GET http://localhost:5000/health
```

### Cancel Operation (cURL)
```bash
curl -X POST http://localhost:5000/cancel
```

---

## CLI Usage Example
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

---

## Documentation
- Full documentation is available in the `README.md` file.
- API documentation is included in the repository under `/docs`.

---

## Contributors
- [Your Name] - Lead Developer
- [Contributor Name] - UI Design
- [Contributor Name] - Testing

---

## Changelog
### v1.0.0 (Initial Release)
- Added CLI, UI, and API functionality
- Implemented Docker support
- Added security features (input validation, rate limiting, HTTPS)
- Fixed division by zero and other bugs
- Improved performance and error handling

---

## Support
For issues or questions, please open an issue on [GitHub](https://github.com/lio972/Python-AI-Agent-with-API_1/issues) or contact us at [support@example.com](mailto:support@example.com).

---

## License
This project is open-source and available under the **MIT License**. See the `LICENSE` file for details.

---

Thank you for using the AI Agent Calculator! We hope you find it useful. 🚀
