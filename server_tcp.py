import socket
import sys
from datetime import datetime, timezone


def start_tcp_server(port = 8000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.settimeout(5)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data.decode() == 'datetime':
                    conn.sendall(datetime.now(timezone.utc).isoformat().encode())
                elif data.decode() == 'date':
                    conn.sendall(datetime.now(timezone.utc).strftime('%Y-%m-%d').encode())
                elif data.decode() == 'time':
                    conn.sendall(datetime.now(timezone.utc).strftime('%H:%M:%S %Z').encode())
                else:
                    conn.sendall('Unknown request'.encode())


if __name__ == '__main__':
    if len(sys.argv) > 1 and int(sys.argv[1]):
        start_tcp_server(int(sys.argv[1]))
    else:
        start_tcp_server()