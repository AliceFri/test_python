import socket
from time import sleep

HOST ='sz-dl-339.autox.sz'
PORT = 18002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

if __name__ == '__main__':

    while True:
        s.send(b"Please input msg:")
        data = s.recv(1024)
        print(data)
        sleep(2)