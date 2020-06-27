import socket
HOST = "127.0.0.1"
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn1, addr1 = s.accept()
    with conn1:
        print("Connected to", addr1)
        conn2, addr2 = s.accept()
        with conn2:
            print("Connected to", addr2)
            while True:
                conn1.sendall(b"\n")
                data = b""
                while not data:
                    data = conn1.recv(1024)
                print(addr1, "sends", data.decode())
                conn2.sendall(data)
                conn2.sendall(b"\n")
                data = b""
                while not data:
                    data = conn2.recv(1024)
                print(addr2, "sends", data.decode())
                conn1.sendall(data)