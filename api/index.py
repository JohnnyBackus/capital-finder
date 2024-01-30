from http.server import BaseHTTPRequestHandler
import platform
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = f"Hello, world! Using Python version {platform.python_version()}."
        self.wfile.write(message.encode('utf-8'))
   
        return