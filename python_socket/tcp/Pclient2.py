import socket

HOST = '127.0.0.1'
PORT = 8888


def main():
    # 設定為TCP連線
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # 連線到 HOST: PORT
    server.connect((HOST, PORT))

    while True:
        s_msg = input('請輸入:')
        server.send(s_msg.encode())

        recv_msg = server.recv(1024)
        print('server: ' + recv_msg.decode())

        if s_msg == 'end':
            server.close()
            break


if __name__ == '__main__':
    main()
