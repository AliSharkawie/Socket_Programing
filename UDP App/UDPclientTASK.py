#UDP_Client
#Ali mohamed abdelaty
from socket import*
#import sys
clientPort = int(input('enter client portNumber '))
serverIP = '127.0.0.1'
serverPort=1000
clientSocket = socket(AF_INET,SOCK_DGRAM)
#clientPort = int(sys.argv[1])
clientSocket.bind(('127.0.0.1',clientPort))
message=input('enter message' )
#message= sys.avrg[2]
clientSocket.sendto(message.encode(),(serverIP, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close()