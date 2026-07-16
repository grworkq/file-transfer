import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(2)
    conn, addr = sock.accept()
    with conn:
        size_name = conn.recv(8)
        int_size_name = int.from_bytes(size_name, "big")
        name = conn.recv(int_size_name).decode()
        size = conn.recv(8)
        size = int.from_bytes(size)
        
        with open(f"server_files/{name}", "wb") as file:
            recev = 0
            while recev < size:
                chunk = conn.recv(4096)
                file.write(chunk)
                recev += len(chunk)

print("Файл успешно получен!")
print(f"Размер файла: {size} Байт")
print(f"Название файла: {name}")