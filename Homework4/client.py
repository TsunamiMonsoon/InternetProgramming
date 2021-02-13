import socket

# define host and port
host = "localhost"
port = 12345


# create a correct message string
def msg_string(_c, _a, _b, _p, _t):
    if _c == "E":
        message = _c + str(_a) + " "
        message += ' '.join(str(x) for x in _p)
    elif code == "S":
        message = _c + str(_a) + " " + str(_b) + " "
        message += ' '.join(str(x) for x in _p)
        message += " " + str(_t)
    else:
        message = _c + str(_a) + " " + str(_b) + " "
        message += ' '.join(str(x) for x in _p)
        message += " " + str(_t)
    return message


# send_data to server
def send_data(_c, _a, _b, _p, _t):
    sock = socket.socket()
    sock.connect((host, port))

    message = msg_string(_c, _a, _b, _p, _t)
    print("Sending: " + message)
    encoded_message = message.encode()
    sock.sendall(encoded_message)
    sock.shutdown(1)

    response = ""
    encoded_message = sock.recv(2048)
    while len(encoded_message) > 0:
        response += encoded_message.decode()
        encoded_message = sock.recv(2048)

    print("Received: " + response)
    print()

    # close sock and get response
    sock.close()
    return response


# used from test_polynomials.py variables
# code = S is successful response to bisection request
code = "S"
# represents the value use in bisection
a = 0
# also represent the value used in bisection
b = 2
# numbers represent the coefficients of polynomials
poly = [-945, 1689, -950, 230, -25, 1]
# tolerance value in bisection
tol = 1e-15

print()

response1 = send_data(code, a, b, poly, tol)
resCode = response1[0]

if resCode == "E":
    pass # filler code, does nothing at all
elif resCode == "S":
    a = float(response1[1:])
    code = "E"
    send_data(code, a, b, poly, tol)
