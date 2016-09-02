import socket
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTPRequestHandler class
class RequestHandler(BaseHTTPRequestHandler):
    timeout = 0
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Wait exponentially.
        RequestHandler.timeout += 1
        time.sleep(pow(2, self.timeout) / 1000.0)
        print('Sleeping {}'.format(RequestHandler.timeout))

        # Send message back to client
        message = 'I\'m ' + socket.gethostname()
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


def main():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('running server...')
    httpd.serve_forever()


if __name__ == "__main__":
    main()