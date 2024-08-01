from http.server import BaseHTTPRequestHandler , HTTPServer

Host = "127.0.0.1"
Port = 5566

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("<h1> Write Html code</h1>".encode("UTF-8"))



class HTTPserver(HTTPServer):
    def __init__(self, host,port):
        server_addrs = (host,port)
        HTTPServer.__init__(self,server_addrs,RequestHandler)



def run_server(host,port):
    server = HTTPserver(host,port)
    print("Listen at {} ".format(Port))
    server.serve_forever()
    server.socket.close()



run_server(Host,Port)