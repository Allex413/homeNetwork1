
import socket

clientSocet = socket.socket()
clientSocet.connect(('127.0.0.1', 50000))


# clientSocet.sendall("Привет, сервер".encode(encoding="utf-8"))

# цикл отправки сооббщения
while True:
  messageSend = input("Введите сообщение: ")
  if messageSend == 'by by':
    break
  clientSocet.sendall(messageSend.encode(encoding="utf-8"))
# цикл приема сообщения
  while True:
    data = clientSocet.recv(1024)
    receivedMsg = data.decode(encoding="utf-8")
    print("Принято", receivedMsg)

clientSocet.close()
