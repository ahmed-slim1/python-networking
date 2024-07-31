import socket
#                      IP v4              TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#        server ip      service port
sock.bind(('127.0.0.1', 5555))

# max number of device connecting in same time
sock.listen(5)

Sdata = ""

while Sdata != "exit":

    connection,address = sock.accept()

    Rdata = connection.recv(1024)

    Rdata = Rdata.decode("UTF-8")

    print("CLINT : ",Rdata)

    Sdata = input("SERVER: ")

    Sdata = Sdata.encode("UTF-8")

    connection.send(Sdata)


sock.close()