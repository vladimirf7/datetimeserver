import socket
import sys


def send_udp_request(message, ip = '127.0.0.1', port = 8000):
    print(f'Sending "{message}" to {ip}:{port}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(str.encode(message), (ip, port))
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(f'received reply: {data}')


if __name__ == '__main__':
    '''argv[1] - message
    argv[2] - optional port
    '''
    if len(sys.argv) > 2 and int(sys.argv[2]):
        send_udp_request(sys.argv[1], int(sys.argv[2]))
    else:
        send_udp_request(sys.argv[1])