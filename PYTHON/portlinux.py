import socket
ip = input("enter ip: ")


for port in range(1, 101):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print('open' + str(port))
        print(sock.recv(1024))
        sock.close()
    except:
        pass
