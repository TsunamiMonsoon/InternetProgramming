# HTTP server using sockets. This server will send a file

import socket
from HTTP_Server_Example import reader_writer
import mimetypes


def send_file_response(rw, message, content_type='text/plain', status=200, status_remark='OK'):
    # first line
    rw.write("HTTP/1.1 {} {}\n".format(status, status_remark))
    # headers
    rw.write("content-type: {}\n".format(content_type))
    rw.write("content-length: {}\n".format(len(message)))
    # blank line
    rw.write("\n")
    # message body
    rw.socket.sendall(message)


if __name__ == "__main__":
    listener = socket.socket()
    listener.bind(("", 12345))
    listener.listen(0)

    while True:
        (sock, addr) = listener.accept()
        rw = reader_writer(sock)
        filename = "Webpage.html"
        with open(filename, 'rb') as file:
            data = file.read()
        mtype = mimetypes.guess_type(filename)
        print(mtype)
        send_file_response(rw, data, content_type=mtype)

        sock.close()
