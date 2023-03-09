#TCP Server in Python

from socket import *

serverPort = 12000 #Server port should be known by all clients

serverName = '10.84.58.45'

serverSocket = socket(AF_INET, SOCK_STREAM) 

serverSocket.bind(('', serverPort)) #Bind the socket to the certain port numb and IP

#Start listening over this port
serverSocket.listen(1)  #1:Get connected with maximum 1 client at a time

print('The server is ready to receive')

while True:
    dataCommunicationSocket, addr = serverSocket.accept()

    msg = dataCommunicationSocket.recv(2048)

    msg_string = msg.decode()

    print('MSG from client: ' + msg_string)

    #Convert the message to uppercase
    upperMsg = msg_string.upper()

    #Send back to client
    dataCommunicationSocket.send(upperMsg.encode())


    #Close the data communication socket 
    dataCommunicationSocket.close()




