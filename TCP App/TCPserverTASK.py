# TCP server
# Ali mohamed abdelaty
from socket import *

serverPort = 1350
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
print("listining at  : ", serverSocket.getsockname())

while True:
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    print("server ", connectionSocket.getsockname())
    print(" socket connection between ", serverSocket.getsockname(), " and ", connectionSocket.getsockname())

    sentence = connectionSocket.recv(1024)
    #    capitalizedSentence= sentence.decode()
    print(' Recieved message from client is : ', sentence.decode())
    realmessage = sentence.decode()
    size = str(len(realmessage))
    connectionSocket.send(size.encode())
    #    size = len((sentence.encode('utf-8')))
    #    connectionSocket.send(str(size.encode()))
    #    print('size of client message is : ' , size)
    #    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
