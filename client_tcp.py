import socket
import sys


def send_request(port = 8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', port))
        s.sendall(b"time")
        data = s.recv(1024)
        print(f"Received {data}")
        s.sendall(b"date")
        data = s.recv(1024)
        print(f"Received {data}")
        s.sendall(b"datetime")
        data = s.recv(1024)
        print(f"Received {data}")


if __name__ == '__main__':
    if len(sys.argv) > 1 and int(sys.argv[1]):
        send_request(int(sys.argv[1]))
    else:
        send_request()