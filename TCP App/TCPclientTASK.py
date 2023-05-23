#TCP client
# Ali mohamed abdelaty
from socket import *
serverIP= '127.0.0.1'
serverPort= 1350
while True:
    sentence = input(" enter sentence or Exit tp disconnect : ")
    if sentence=="Exit" :
        exit()
    else:
        clientSocket= socket(AF_INET, SOCK_STREAM)
        clientSocket.bind(('127.0.0.1',0))
        clientSocket.connect((serverIP, serverPort))
        clientSocket.send(sentence.encode())
        lengthMessage= clientSocket.recv(1024)
        print ('  recieved nessage FromServer : ' , lengthMessage ,' byte ')
        clientSocket.close()