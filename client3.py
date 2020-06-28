import socket
HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = b""
        while data != "\n":
            data = s.recv(1024)
        sent = input("> ").encode()
        s.sendall(sent)
        data = b""
        while not data:
            data = s.recv(1024)
        print("Received:", data.decode())