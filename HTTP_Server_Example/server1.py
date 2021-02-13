# HTTP server using sockets. This server will send a string message only

import socket
from HTTP_Server_Example import reader_writer


def send_string_response(rw, message, content_type='text/html', status=200, status_remark='OK'):
    # first line
    rw.write("HTTP/1.1 {} {}\n".format(status, status_remark))
    # headers
    rw.write("content-type: {}\n".format(content_type))
    rw.write("content-length: {}\n".format(rw.encoded_length(message)))
    # blank line
    rw.write("\n")
    # message body
    rw.write(message)


if __name__ == "__main__":
    listener = socket.socket()
    listener.bind(("", 12345))
    listener.listen(0)

    while True:
        sock = socket.socket()
        (sock, addr) = listener.accept()
        rw = reader_writer(sock)
        send_string_response(rw, "<h1> Hello There!</h1>")

        sock.close()
