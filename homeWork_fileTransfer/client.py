import socket

clientSocet = socket.socket()
clientSocet.connect(('127.0.0.1', 50001))

# conn, addr = clientSocet.accept()
print("connected")

file = open("123.jpg", "rb")
while True:
    data = file.read(4096)
    clientSocet.send(data)
    if not data:
        break
file.close()
print("file sended")