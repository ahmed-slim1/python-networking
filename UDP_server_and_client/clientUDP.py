import socket

#                           IP v4            UDP protocol
sock  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

Rdata = ""

while Rdata != "exit" :

    Sdata = input("(CLIENT)> ") #data you want to send it
    Sdata = Sdata.encode("UTF-8") # encode it

    sock.sendto(Sdata,("127.0.0.1",5555))

    Rdata , address = sock.recvfrom(1024) # max bufsize : The number of bytes to be read from the UDP socket.
    Rdata = Rdata.decode("UTF-8")

    print("(SERVER)>"+Rdata)


exit()



