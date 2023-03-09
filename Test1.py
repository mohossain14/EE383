# UDP Server using Python

from socket import * 

#Define a UDP socket 
serverPort = 12002 #Port Number of server

#Create a socket 
serverSocket = socket(AF_INET, SOCK_DGRAM) #AF means Address Family INET means internet DGRAM means datagram (UDP)

#Configure port and IP Address for the socket
serverSocket.bind(('', serverPort))

print('The UDP server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048) #2048 is packet size that can be recieved
    modifiedMessage        = message.decode().upper()
    print('Message from client:' + message.decode())

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)