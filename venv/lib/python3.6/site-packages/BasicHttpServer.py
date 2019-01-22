#!/usr/bin/python
"""
    description: A basic http server
    author : Ashwani Singh
    created on : 24 Nov, 2015
"""

from http.server import HTTPServer, CGIHTTPRequestHandler
from optparse import OptionParser


class BasicHttpServer:
    port = 8080
    host = '127.0.0.1'
    httpd = None

    def __init__(self, hostname='127.0.0.1', portno=8080):
        self.port = int(portno)
        self.host = hostname
        self.create()

    def create(self):
        httpd = HTTPServer((self.host, self.port), CGIHTTPRequestHandler)
        self.httpd = httpd

    def start(self):
        print("Starting simple http server on %s:%d" % (self.host, self.port))
        self.httpd.serve_forever()

"""
    Main function
"""


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-a", "--hostname", action="store", dest="hostname",
                      default='127.0.0.1', help="hostname for server defaults to 127.0.0.1")
    parser.add_option("-p", "--port", action="store", dest="port",
                      default=8080, help="port for server defaults to 8080")
    parsed_options,parsed_args = parser.parse_args()

    host = parsed_options.hostname if parsed_options.hostname else '127.0.0.1'
    port = int(parsed_options.port) if parsed_options.port else 8080

    try:
        # creating new simple http server
        http_server = BasicHttpServer(host, port)
        http_server.start()
    except OSError as oserr:
        print("Failed to start server on %s:%d" % (host, int(port)))
        print("OS Error: " + str(oserr))

if __name__ == "__main__":
    main()
