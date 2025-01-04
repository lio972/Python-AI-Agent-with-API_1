const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// Import the AIAgent class
const { AIAgent } = require('./agent.js');
const agent = new AIAgent();

// Middleware to parse JSON
app.use(express.json());

// Serve static files
app.use(express.static('public'));

// API Endpoints
app.post('/calculate', (req, res) => {
  const { operation, numbers } = req.body;
  
  try {
    let result;
    if (operation === 'sqrt') {
      result = agent.calculate(operation, numbers[0]);
    } else {
      result = agent.calculate(operation, ...numbers);
    }
    res.json({ result: result.toString() });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

app.post('/cancel', (req, res) => {
  res.json({ message: 'Operation canceled' });
});

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    operations_supported: Object.keys(agent.operations),
    current_operation: null
  });
});

// Serve the HTML file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
