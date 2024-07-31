import socket

ip = socket.gethostbyname("google.com") #gave ip when you gave host

host = socket.gethostbyaddr("142.201.150.64") # gave host when you gave ip

service_name = socket.getservbyport(1) # gave service work on port

service_port = socket.getservbyname("http") # gave the port number of service


