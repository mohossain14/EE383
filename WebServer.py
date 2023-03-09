from socket import *
from sys import *

serverSocket = socket.socket(socket.AF_INET, SOCK_STREAM)

serverPort = 80

serverSocket.bind(("", serverPort))

serverSocket.listen(1)

while True:
    print('Server is ready to receive')

    connectionSocket, addr = serverSocket.accept()


try:
    message = connectionSocket.recv(1024).decode()
    print(message)

    filename = message.split()[1]

    f = open(filename[1:])

    outputdata = f.read()

    connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
    connectionSocket.close()

except 