import socket
import sys


def send_udp_request(message, port = 8000, ip = '127.0.0.1'):
    print(f'Sending "{message}" to {ip}:{port}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    sock.sendto(str.encode(message), (ip, port))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(f'received reply: {data}')


if __name__ == '__main__':
    if len(sys.argv) > 1 and int(sys.argv[1]):
        port = int(sys.argv[1])
    else:
        port = 8000
    for req in ['date', 'time', 'datetime']:
        send_udp_request(req, port)
        print()