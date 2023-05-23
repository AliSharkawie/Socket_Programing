#UDP Server
# Ali mohamed abdelaty

from socket import *
serverPort = 1000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1',serverPort))
print ("The server is ready to receive ")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('this message : ',message.decode() )
    print ('it recieved from ',clientAddress)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)