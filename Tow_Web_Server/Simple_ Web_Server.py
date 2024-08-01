import http.server
import socketserver

Port = 5555
Host ='127.0.0.1'

Handler = http.server.SimpleHTTPRequestHandler
server = socketserver.TCPServer((Host,Port), Handler)
def run():
    print("serving at port ",Port)
    server.serve_forever()

run()


#In this web server most have a file.html in same directory