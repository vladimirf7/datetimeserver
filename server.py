import socket
import sys
from datetime import datetime, timezone


def start_server(port = 8000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f'Starting server on port {port}')
    sock.bind(('', port))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print(f'received message: {data}')
        if data.decode() == 'datetime':
            sock.sendto(datetime.now(timezone.utc).isoformat().encode(), addr)
        if data.decode() == 'date':
            sock.sendto(datetime.now(timezone.utc).strftime('%Y-%m-%d').encode(), addr)
        if data.decode() == 'time':
            # import pdb; pdb.set_trace()
            sock.sendto(datetime.now(timezone.utc).strftime('%H:%M:%S %Z').encode(), addr)


if __name__ == "__main__":
    if len(sys.argv) > 1 and int(sys.argv[1]):
        start_server(int(sys.argv[1]))
    else:
        start_server()