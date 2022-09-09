import socket

# socket.SOCK_STREAM    TCP
# socket.SOCK_DGRAM     UDP
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('sz-dl-339.autox.sz', 18002))
    s.listen(5)     # 限制 pending 的链接数目

    print('Server Start Listening')
    print('Wait For Connection ...')

    while True:
        conn, addr = s.accept()
        print(f'Connected By {addr}')

        while True:
             data = conn.recv(1024)
             print(data)
             conn.send(b"Server Received Your Message")