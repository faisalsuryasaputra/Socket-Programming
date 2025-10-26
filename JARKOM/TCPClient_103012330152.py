import socket

serverName = "127.0.0.1"
serverPort = 65432

# Buat socket TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print(f"Terhubung ke server di {serverName}:{serverPort}")

while True:
    message = input("Masukkan data (atau 'exit' untuk keluar): ")
    clientSocket.send(message.encode())

    if message.lower() == "exit":
        break

    modifiedMessage = clientSocket.recv(1024).decode()
    print("Respon dari server:", modifiedMessage)

clientSocket.close()
