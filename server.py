import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15552))
socket.listen(5)
#client, address = socket.accept()
response = " "
while 1:
        client, address = socket.accept()
        response = client.recv(255)

        while response != "":

                if response != "":
                        print (response.decode())
                response = client.recv(255)
