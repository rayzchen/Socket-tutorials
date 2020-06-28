import socket, threading
HOST = "127.0.0.1"
PORT = 5555

def listen():
    while True:
        data = b""
        while not data:
            data = s.recv(1024)
        print("\b\bReceived:", data.decode() + "\n> ", end = "")

def get_input():
    global sent
    while True:
        sent = input("> ").encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    sent = b""
    listen_thread = threading.Thread(target = listen)
    input_thread = threading.Thread(target = get_input)
    listen_thread.start()
    input_thread.start()
    while True:
        if sent:
            s.sendall(sent)
            sent = b""