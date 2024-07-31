import socket

#                       ip V4             men UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# connection  server_ip   port_data out this port
sock.bind(("127.0.0.1",5555))


Rdata =""

while Rdata != "exit" :

# Rdata save data user send it , address save the User_ip and User_port
    Rdata ,address = sock.recvfrom(1024) # max bufsize : The number of bytes to be read from the UDP socket.

# Rdata has user data in Binary (encoded) than we decode this data
    Rdata = Rdata.decode("UTF-8")

    print("(CLIENT)> "+Rdata)

# Sdata this data we want to send for user
    Sdata = input("(SERVER)> ")

# we need to encode this data
    Sdata = Sdata.encode("UTF-8")


# to send data we need data and User_ip and User_port to send this data
    sock.sendto(Sdata,address)

exit()