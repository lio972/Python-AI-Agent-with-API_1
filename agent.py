import math

class AIAgent:
    def __init__(self):
        self.operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else 'Error: Division by zero',
            'sqrt': lambda x: math.sqrt(x) if x >= 0 else 'Error: Negative number',
            'power': lambda x, y: math.pow(x, y)
        }

    def calculate(self, operation, *args):
        try:
            if operation not in self.operations:
                raise ValueError("Invalid operation")
            return self.operations[operation](*args)
        except Exception as e:
            return str(e)
