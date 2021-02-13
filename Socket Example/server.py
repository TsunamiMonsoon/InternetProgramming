# implement a TCP server socket
import socket
import logging

ip = ""
port = 12345


def binom(n, m):
    b = 1
    for i in range(0, m):
        b = b * (n - i) // (i + 1)
        return b


# 1. create a socket
sock = socket.socket()

# 2. bind with IP address and PORT number
sock.bind((ip, port))

# 3. generate listener and let the server wait for a connection request
sock.listen()

# 5. accept the request
while True:
    (sock_client, address) = sock.accept()  # waits for a connection request
    # when successful it returns a socket and and address
    # to use to communicate with the client

# 6. read the data inside the request
# 6.1 get data from the request
print(address)
logging.info("Connection is successfully est")
loggin.error()
bytes = sock_client.recv(2048)
client_data = ""

while len(bytes) > 0:
    client_data += bytes.decode()
    bytes = sock_client.recv(2048)
print(client_data)

# 6.2 parse the data
# receiving data is "number space number", e.g. "10 20" => [10, 20]
list_of_parts = client_data.split(" ")
# if input is "12 6" => ["12", "6"]
# if input is "12  6" => ["12", "", "6"]
if len(list_of_parts) != 2:
    response_code = "E"
    response_message = "incorrect number of parameter sent"
else:
    # error handling code for wrong types of parameters
    try:
        # 6.3 compute the binomial function
        result = binom(int(list_of_parts[0]), int(list_of_parts[1]))
        # 6.4 create a response message
        response_code = "B"
        response_message = str(result)
    except:
        response_code = "E"
        response_message = "Conversion or computation error"
response = response_code + response_message  # B12345

# 7. send response
sock_client.sendall(response.encode())  # encode() converts string to bytes stream

sock_client.shutdown(1)

# 8. close the socket
sock_client.close()
