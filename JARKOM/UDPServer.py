import socket
from datetime import datetime

# Konfigurasi server
serverIP = "127.0.0.1"
serverPort = 12000

# Buat socket UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))

print("Server berjalan dan menunggu pesan...")

while True:
    data, clientAddress = serverSocket.recvfrom(2048)
    message = data.decode()

    # Proses 1: Inversi huruf besar/kecil
    inversed = message.swapcase()

    # Proses 2: Hitung jumlah karakter
    count = len(message.strip())

    # Proses 3: Hapus spasi kosong di awal/akhir
    stripped = message.strip()

    # Proses 4: Tambahkan timestamp
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    # Proses 5: Tambahkan pesan konfirmasi
    result = f"{inversed} {timestamp} | Panjang: {count} | Data telah diproses"

    # Kirim hasil ke client
    serverSocket.sendto(result.encode(), clientAddress)
    print(f"Data '{message}' dari {clientAddress} telah diproses dan dikirim kembali.")
