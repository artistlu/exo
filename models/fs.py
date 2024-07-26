from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class ModelFileHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.environ.get('MODEL_DIR', '.'), **kwargs)

if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', 8082), ModelFileHandler)
    httpd.serve_forever()