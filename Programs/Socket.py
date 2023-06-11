import socket

# Open socket (send and receive data).
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to host(domain name), port (Dial the phone).
mySocket.connect(('data.pr4e.org', 80))

# Get data and encode (Convert to utf-8).
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# Send Data.
mySocket.send(cmd)

# Receive data until the socket is closed.
while True:
    # Wait until data received == 512 characters.
    data = mySocket.recv(512)
    # If socket is closed by remote server, break.
    if len(data) < 1:
        break
    # Decode the data (Convert to Unicode).
    print(data.decode(), end='')

# Close the socket.
mySocket.close()