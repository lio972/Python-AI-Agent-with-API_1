from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from agent import AIAgent

agent = AIAgent()

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/calculate':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            operation = data.get('operation')
            numbers = data.get('numbers', [])
            
            try:
                if operation == 'sqrt':
                    result = agent.calculate(operation, numbers[0])
                else:
                    result = agent.calculate(operation, *numbers)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'result': str(result)}).encode())
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        
        elif self.path == '/cancel':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Operation canceled'}).encode())
        
        else:
            self.send_error(404, 'Endpoint not found')

    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'status': 'healthy',
                'operations_supported': list(agent.operations.keys()),
                'current_operation': None
            }).encode())
        
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        
        else:
            self.send_error(404, 'Endpoint not found')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
