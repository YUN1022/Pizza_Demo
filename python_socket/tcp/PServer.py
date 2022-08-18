import socket

BIND_IP = '127.0.0.1'
BIND_PORT = 8888


def main():
    # 設定為TCP連線
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # 監聽
    server.bind((BIND_IP, BIND_PORT))
    # 最大連線數並開始接聽
    server.listen(5)

    print(f'Listening on {BIND_IP}:{BIND_PORT}')

    while True:
        client, addr = server.accept()
        print(client)
        print(f'連接地址: {addr}')

        data = client.recv(1024)
        print(data.decode())

        client.send('好的'.encode())


if __name__ == '__main__':
    main()
