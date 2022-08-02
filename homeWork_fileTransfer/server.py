import socket

myFirstSocket = socket.socket()
myFirstSocket.bind(("", 50001))
myFirstSocket.listen(1)
print("connected")

file = open("321.jpg", "wb")
while True:
    clientSocket, clientAdres = myFirstSocket.accept()
    data = clientSocket.recv(4096)
    file.write(data)
    if not data:
        break
file.close()
