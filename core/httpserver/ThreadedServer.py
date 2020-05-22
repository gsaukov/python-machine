from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse
from socketserver import ThreadingMixIn
from OriginMap import getMap as getOriginMap
from ValueMap import getMap as getValueMap
from PollutionMap import getMap as getPollutionMap


# https://python-visualization.github.io/folium/quickstart.html
# http://leaflet-extras.github.io/leaflet-providers/preview/

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/originmap':
            map = getOriginMap()
        elif parsed_path.path == '/valuemap':
            map = getValueMap()
        elif parsed_path.path == '/pollutionmap':
            map = getPollutionMap()
        else:
            map = getOriginMap()

        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write(map.encode())

        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':

    server = ThreadedHTTPServer(('', 8510), GetHandler) #can be bound to localhost only
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
