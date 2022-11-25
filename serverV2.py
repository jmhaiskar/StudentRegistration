# socket.socket (socket_family, socket_type, protocol=0)
# socket_type - TCP : socket.SOCK_STREAM, UDP : socket.SOCK_DGRAM
# socket_family - socket.AF_UNIX , socket.AF_INET

# Socket methods
# These are the general socket methods we can use in both clients and servers:
# socket.recv(buflen): receives data from the socket
# socket.recvfrom(buflen): receives data and the sender's address
# socket.recv_into(buffer): receives data into a buffer
# socket.recvfrom_into(buffer): receives data into a buffer.
# socket.send(bytes): sends bytes data to the specified target.
# socket.sendto(data, address): sends data to a given address.
# socket.sendall(data): sends all the data in the buffer to the socket.
# socket.close(): releases the memory and finishes the connection.

# Server socket methods

# socket.bind(address): connect to the address with the socket
# socket.listen(count): maximum number of connections
# socket.accept(): accept connections from the client
# lsof -nti:5000 | xargs kill -9

import socket
import threading
import json
from random import seed
from random import randint
from datetime import datetime



hostname=socket.gethostname()   
bind_ip=socket.gethostbyname(hostname)   
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+bind_ip)   

bind_port =5000 # need to open this port if using Linux

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print ("[*] Listening on {:s}:{:d}".format(bind_ip,bind_port))

# this is our client-handling thread
def handle_client(client_socket, addr):
    # print out what the client sent
     
    request = client_socket.recv(1024).decode()
    print ("[*] Received: {:s} from {:s} : {:d} ".format(request ,addr[0],addr[1]))
    
    seed(datetime.now())
    
    data = []
    for x in range(5):  # 0 to 4
        data.append(randint(1,100))    # 1 to 100 (included)
    
    print("data: " , data)
    
    dataJson = json.dumps({"a": data, "msg1": "bye"})

    # send back a packet
    client_socket.send(dataJson.encode())
    client_socket.close()

while True:
    client,addr = server.accept()
    print ("[*] Accepted connection from: {:16s}:{:d}".format(addr[0],addr[1]))
    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,addr,))
    client_handler.start()