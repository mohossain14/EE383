#TCP Client in Python

from socket import *

serverName = '10.84.58.56'

serverPort = 50000

clientSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM for TCP Socket

#Establish connection to server first
clientSocket.connect((serverName, serverPort))

msg = input('INPUT a messasge: ')

#Send the message to the server through the TCP connection
clientSocket.send(msg.encode())

#Receive response from the server
response_msg = clientSocket.recv(2048)

print('Msg from server: ' + response_msg.decode())

clientSocket.close()