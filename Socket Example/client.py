# implement TCP client
import socket

n = 20
m = 10

# 1. create a socket
sock = socket.socket()

# 2. make a connection to the server. IP and PORT of the server
sock.connect(('127.0.0.1', 12345))

# 3. write() to send a request to the server
# 3.1 make a request using 'n' and 'm' we need to create something like number space number
request = str(n) + " " + str(m)

# 3.2 send the created request to the server
sock.sendall(request.encode())  # the parameter must be a byte stream

# 3.3 signal the server there's no more data to be sent
sock.shutdown(1)

# 4. read() to receive
bytes = sock.recv(2048)
response = ""

while len(bytes) > 0:
    response = bytes.decode()
    bytes = sock.recv(2048)
# 5. print the response
print(response)

# 6. close the socket
sock.close()
