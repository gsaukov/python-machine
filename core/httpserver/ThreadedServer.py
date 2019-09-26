from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse
from socketserver import ThreadingMixIn
from core.httpserver import Webmap

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)

        map = Webmap.getMap()

        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write(map.encode())
        self.finish()
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), GetHandler)
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()