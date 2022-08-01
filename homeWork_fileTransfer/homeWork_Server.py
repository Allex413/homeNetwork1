
import socket

myFirstSocket = socket.socket()
myFirstSocket.bind(("", 50000))
myFirstSocket.listen(1)

while True:
    clientSocket, clientAdres = myFirstSocket.accept()
    f = open("321.gif", "wb")
    data = clientSocket.recv(1024)
    f.write(data)
    f.close()

clientSocket.close()  