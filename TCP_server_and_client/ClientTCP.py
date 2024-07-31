import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 5555))

Sdata = ""
while Sdata != "exit":

    sdata = input("CLINT : ")

    sdata = sdata.encode("UTF-8")

    sock.send(sdata)

    Rdata = sock.recv(1024)

    data = Rdata.decode("UTF-8")

    print("SERVER: ",data)

sock.close()
