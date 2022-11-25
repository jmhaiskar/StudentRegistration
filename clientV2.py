import socket
import json

def client_program():
    host = "172.31.66.144" 
    port = 5000  # socket server port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input
    client_socket.send(message.encode())  # send message

    while message.lower().strip() != 'bye':
        data = client_socket.recv(1024).decode() # receive response
        print(data)
        dataJson = json.loads(data)
        arr = dataJson.get("a")
        message = dataJson.get("msg1")
       
        print('Received from server: ', arr)  # show in terminal
        print('Received from server: ' + message)  # show in terminal

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()