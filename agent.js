class AIAgent {
  constructor() {
    this.operations = {
      'add': (x, y) => x + y,
      'subtract': (x, y) => x - y,
      'multiply': (x, y) => x * y,
      'divide': (x, y) => y !== 0 ? x / y : 'Error: Division by zero',
      'sqrt': (x) => x >= 0 ? Math.sqrt(x) : 'Error: Negative number',
      'power': (x, y) => Math.pow(x, y)
    };
  }

  calculate(operation, ...args) {
    if (!this.operations[operation]) {
      throw new Error('Invalid operation');
    }
    return this.operations[operation](...args);
  }
}

module.exports = { AIAgent };
