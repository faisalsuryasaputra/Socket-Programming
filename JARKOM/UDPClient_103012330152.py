import socket

serverName = "127.0.0.1"
serverPort = 12000

# Buat socket UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Input dari user
message = input("Masukkan data yang ingin dikirim ke server: ")

# Kirim data
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Terima hasil dari server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Hasil dari server:", modifiedMessage.decode())

# Tutup koneksi
clientSocket.close()
