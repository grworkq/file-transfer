import pathlib, socket

HOST = '127.0.0.1'
PORT = 65432

paths = input('Путь к файлу (Укажите, пожалуйста, абсолютный путь): ')
path = pathlib.Path(paths)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    size_name = len(path.name.encode('utf-8'))
    sock.sendall(size_name.to_bytes(8))
    sock.sendall(path.name.encode('utf-8'))
    size = path.stat().st_size
    sock.sendall(size.to_bytes(8, byteorder="big"))
    with open(path, 'rb') as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sock.sendall(chunk)
