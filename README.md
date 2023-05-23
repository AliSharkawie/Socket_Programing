# Socket_Programing 

build client/server applications that communicate using sockets 

Two socket types 
▪ UDP: unreliable datagram 
▪ TCP: reliable, byte stream-oriented

Application discription 
1. client reads a line of characters (data) from its keyboard andsends data to server
2. server receives the data and converts characters to uppercase
3. server sends modified data to client
4. client receives modified data and displays line on its screen 



extra explanation :
    socket(AF_INET, SOCK_DGRAM ) :
      1) AF_INET:
          The primary purpose of AF_INET was to allow for other possible network protocols or 
          address families (AF is for address family; AF_INET is for the (IPv4) internet protocol 
          family). 
          • Socket are characterized by their domain, type and transport protocol.
          • Common domains are:
          ➢ AF_UNIX: address format is UNIX pathname
          ➢ AF_INET: address format is host and port number
          ➢ (there are actually many other options which can be used here for specialized 
          purposes).
          ➢ Usually we use AF_INET for socket programming
      2) SOCK_DGRAM: arguemt indicates socket type is udp or tcp
          ➢ SOCK_STREAM = TCP 
          ➢ SOCK_DGRAM = UDP
          
          
  *) socket.recvfrom – This method receives UDP message
  *) socket.sendto – This method transmits UDP message
  *) socket.close – This method closes socket
  *) socket.gethostname – Returns a hostname
  *) socket.bind(' ', port ) – This method binds address hostname(' ‘ is translated to local host), port number to socket.
  If port = 0 then the OS assigns a dynamic port number
  Note: Line serverIP = '127.0.0.1' can be replaced by serverName = gethostname()
   
       


