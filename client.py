
import socket

hote ="localhost"
port = 15552
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
        socket.connect((hote, port))
        print ("Connection on {}".format(port))
        while True :

                message = input()
                socket.send("{}".format(message).encode())
except:
        print("sa marche pas")
        
socket.close()
