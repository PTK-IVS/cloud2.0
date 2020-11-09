from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
# sock.connect(('79.137.175.47', 10008))
# sock.connect(('52.59.232.90', 10008))
sock.connect(('127.0.0.1', 10008))

i = 2
while i:
    sock.send(b'5000 180002R10010100 ')
    # 5000 180050E30500000
    sock.settimeout(60)  # установка таймаута
    data = sock.recv(1024)
    print(data)
    sock.send(b'5000 180002R10010100 ')
    # 5000 180050E30500000
    data = sock.recv(1024)
    i -= 1
    print(data)
