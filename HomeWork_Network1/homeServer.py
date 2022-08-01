
import socket

myFirstSocket = socket.socket()
myFirstSocket.bind(("", 50000))
myFirstSocket.listen(1)

while True:
  clientSocket, clientAdres = myFirstSocket.accept()
  messageSend = input("Введите сообщение: ")
  if messageSend == 'by by':
    break
  clientSocket.sendall(messageSend.encode(encoding="utf-8"))

  while True:
    data = clientSocket.recv(1024)
    receivedMsg = data.decode(encoding="utf-8")
    print(receivedMsg)


clientSocket.close()  


