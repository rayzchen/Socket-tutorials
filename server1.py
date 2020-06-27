import socket
HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Connected to", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Received:", data.decode())
                conn.sendall(data)