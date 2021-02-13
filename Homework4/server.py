import socket
import logging
from Homework4 import polynomials
# this type of import didnt work
# from Homework4.polynomials import *


# define host and port
host = "localhost"
port = 12345

# start connection
listener = socket.socket()
# bind
listener.bind((host, port))

listener.listen()

while 1:
    # communicate through connection
    conn = listener.accept()
    # get the sock from conn
    sock = conn[0]

    # request comes from the client
    request = ""
    encoded_message = sock.recv(2048)
    while len(encoded_message) > 0:
        request += encoded_message.decode()
        encoded_message = sock.recv(2048)

    logging.info(" request received |" + request + "|")
    print("request received |" + request + "|")
    if len(request) == 0:
        message = "XEmpty request"
        logging.error(" response " + message)
        sock.sendall(message.encode())
        sock.shutdown(1)
    else:
        request_code = request[0]
        # code E, successful response to evaluate request
        if request_code == "E":
            try:
                parameters = request[1:].split(' ')
                args = [float(x) for x in parameters]

                x = args[0]
                poly = args[1:]

                value = polynomials.evaluate(x, poly)

                message = "E" + str(value)
                logging.info("response " + message)
                sock.sendall(message.encode())
                sock.shutdown(1)
            except Exception as ex:
                logging.error("Input value conversion error " + request[1:])
                logging.error(str(ex))
                message = "XInvalid format numeric data: " + request[1:]
                logging.error("response " + message)
                sock.sendall(message.encode())
                sock.shutdown(1)

        # Code S for successful response to bisection request
        elif request_code == "S":
            try:
                parameters = request[1:].split(' ')
                args = [float(x) for x in parameters]

                a = args[0]
                b = args[1]
                poly = args[2:8]
                tol = args[8]

                value = polynomials.bisection(a, b, poly, tol)

                message = "S" + str(value)
                logging.info("response " + message)
                sock.sendall(message.encode())
                sock.shutdown(1)
            except Exception as ex:
                logging.error("Input value conversion error " + request[1:])
                logging.error(str(ex))
                message = "XInvalid format numeric data: " + request[1:]
                logging.error("response " + message)
                sock.sendall(message.encode())
                sock.shutdown(1)

        else:
            # error message for XInvalid request
            message = "XInvalid request code: " + request_code
            logging.error("response " + message)
            sock.sendall(message.encode())
            sock.shutdown(1)

    # close socket
    sock.close()
