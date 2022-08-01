
from email import message
import socket

clientSocet = socket.socket()
clientSocet.connect(('127.0.0.1', 50000))
f =  open("123.gif", "rb")
l = f.read(1024)
while True:
    clientSocet.sendall(l)
    l = f.read(1024)
  
f.close()
clientSocet.close()


