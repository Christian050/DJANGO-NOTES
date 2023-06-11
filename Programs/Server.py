from socket import *

def createServer():
    # Create a socket.
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # Bind socket to port 9000
        serversocket.bind(('localhost', 9000))
        # Listen to queue more than one execution(Request).
        serversocket.listen(5)
        # Wait to receive incoming requests.
        while(1):
            # Accept to block until data received.(Connected on browser side)
            (clientsocket, address) = serversocket.accept()
            
            # Read(Receive) 5000 Characters.
            rd = clientsocket.recv(5000).decode()
            # Split based on new lines.
            pieces = rd.split('\n')
            if (len(pieces) > 0) : print(pieces[0])
            
            # Construct response.
            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n'
            data += '<html><body>Hello World</body></html>\r\n\r\n'
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
            
    except KeyboardInterrupt:
        print('\nShutting Down...\n');
    except Exception as exc:
        print('Error:\n');
        print(exc)  
     
    # Clean(close) Socket. 
    serversocket.close()

print('Access http://localhost:9000')
createServer()