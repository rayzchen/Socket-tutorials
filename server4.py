import socket, threading
HOST = "127.0.0.1"
PORT = 5555

def listen(socket):
    while True:
        data = b""
        while not data:
            data = socket.recv(1024)
        sent[socket] = data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn1, addr1 = s.accept()
    print("Connected to", addr1)
    conn2, addr2 = s.accept()
    print("Connected to", addr2)
    sent = {conn1:b"", conn2:b""}
    thread1 = threading.Thread(target = listen, args = (conn1, ))
    thread2 = threading.Thread(target = listen, args = (conn2, ))
    thread1.start()
    thread2.start()
    while True:
        if sent[conn1]:
            conn2.sendall(sent[conn1])
            print(addr1, "sends", sent[conn1].decode())
            sent[conn1] = b""
        if sent[conn2]:
            conn1.sendall(sent[conn2])
            print(addr2, "sends", sent[conn2].decode())
            sent[conn2] = b""