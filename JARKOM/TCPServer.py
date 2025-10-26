import socket
from datetime import datetime

# Konfigurasi server
serverIP = "127.0.0.1"
serverPort = 65432

# Buat socket TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)

print(f"Server TCP berjalan di {serverIP}:{serverPort}")
connectionSocket, clientAddress = serverSocket.accept()
print(f"Terhubung dengan {clientAddress}")

while True:
    data = connectionSocket.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("Koneksi ditutup oleh client.")
        break

    print(f"Menerima data: {data}")

    # Proses 1: Inversi huruf besar/kecil
    inversed = data.swapcase()

    # Proses 2: Hitung jumlah karakter
    count = len(data.strip())

    # Proses 3: Hapus spasi kosong di awal/akhir
    stripped = data.strip()

    # Proses 4: Tambahkan timestamp
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    # Proses 5: Tambahkan pesan konfirmasi
    result = f"{inversed} {timestamp} | Data telah diproses ({count} karakter)"

    connectionSocket.send(result.encode())

connectionSocket.close()
serverSocket.close()
