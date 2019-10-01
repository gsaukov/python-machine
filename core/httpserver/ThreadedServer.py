from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse
from socketserver import ThreadingMixIn
from core.httpserver import OriginMap
from core.httpserver import ValueMap
from core.httpserver import PollutionMap
import threading

# https://python-visualization.github.io/folium/quickstart.html
# http://leaflet-extras.github.io/leaflet-providers/preview/

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/originmap':
            map = OriginMap.getMap()
        elif parsed_path.path == '/valuemap':
            map = ValueMap.getMap()
        elif parsed_path.path == '/pollutionmap':
            map = PollutionMap.getMap()
        else:
            map = OriginMap.getMap()

        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write(map.encode())

        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8510), GetHandler)
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()