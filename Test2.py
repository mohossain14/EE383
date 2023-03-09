# UDP Client

from socket import * 

#ServerPortNumber
serverPort = 12002

#ServerIP
serverIP = '10.84.86.134'

#Create UDP Socket for client side
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Replace raw_input with input in new version
message = input('Input lower case sentence:')

clientSocket.sendto(message.encode(), (serverIP, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()