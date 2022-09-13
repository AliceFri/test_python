# https://juejin.cn/post/6874034712819302414
# https://blog.csdn.net/Chasing__Dreams/article/details/107841722
# IO 涉及 用户态 和 内核态 的切换
"""
BIO
阻塞的， 使用多线程 解决并发问题(多个客户端连接)，
socket.read(), write()函数 堵塞，只能空等

服务端主线程是不能阻塞的，所以要给每一个 TCP 连接配一个线程
缺点： 线程是很贵的资源， 线程池优化也解决不了高并发问题

---------------------------------------------------------

NIO  设置read(),write()函数不堵塞
可以一个线程， hold住所有连接了。
保存所有连接， while 循环遍历所有连接

优点：单线程
缺点：长循环

---------------------------------------------------------

SELECT, POLL    多路复用(一次传入多个连接，避免每个连接都询问)

多路复用器是内核级实现，
一次系统调用询问所有的IO状态，而不是每一个IO都问一次，减少了用户态到内核态的切换

select有1024个连接限制， poll没有， poll的限制是系统连接数上限

优点： 一次系统调用， 减少 用户态 -> 内核态 的切换

缺点： 内核自己还是去遍历所有的连接

---------------------------------------------------------

EPOLL

内核自己开辟空间记录所有的连接，

epoll_create(): 开辟一块空间保存监听对象
epoll_ctr():    往epoll中添加一个类型的监听
epoll_wait():   查询结果，堵塞的，但是可以设置超时时间

优点：  1. 查询结果，不用传递监听的socket数组了
       2. 内核监听状态变化， 而不是遍历查询了

缺点：  1. 单线程， 同步

----------------------------------------------------------

AIO:    异步  注册CallBack, 内核负责读取数据回调。

----------------------------------------------------------

多路复用器 + 多线程

1. 每个 select 都运行在独立的 Thread 中
2. 其中一个 select 作为控制器，在接到连接进来后，把连接分配给不同的 select 去注册
3. 剩下的复数的 select 负责连接的读写

"""
import collections
import select
import socket
import threading

HOST = socket.gethostname()
PORT = 18002


def bio_server():
    def _sub_conn(conn: socket.socket):
        while True:
            result = conn.recv(5).decode("utf-8")
            if result == "end":
                break
            print(result)
        conn.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    while True:
        print("wait accept")
        conn, addr = server.accept()  # 主socket一直在处理连接， 生成的socket负责通信
        print(conn)
        threading.Thread(target=_sub_conn, args=(conn,)).start()


def bio_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    while True:
        data = input("客户端发送数据： ").strip()
        print(client.send(data.encode("utf-8")))
        if data == "end":
            client.close()
            break


# -----------------------------------------------------------------------


def nio_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    server.setblocking(False)  # 设置成非阻塞
    connections = collections.deque()

    while True:
        # print('wait accept')
        try:
            conn, addr = server.accept()
        except BlockingIOError as e:
            pass
        except Exception as e:
            pass
        else:
            conn.setblocking(False)
            connections.append(conn)

        remove = []
        for i in range(len(connections)):
            conn = connections[i]
            try:
                data = conn.recv(5).decode("utf-8")
                print(data)
                if data == "end":
                    conn.close()
                    remove.append(conn)
                    break
            except Exception as e:
                pass

        connections = [i for i in connections if i not in remove]


# 共用 bio_client

# -----------------------------------------------------------------------


def select_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    server.setblocking(False)  # 设置成非阻塞
    rlist = collections.deque([server])
    wlist = collections.deque()
    xlist = collections.deque()

    while True:
        print("wait accept")
        read_list, write_list, error_list = select.select(rlist, wlist, xlist)
        for socket_item in read_list:
            if socket_item == server:
                conn, addr = socket_item.accept()
                conn.setblocking(False)
                rlist.append(conn)
            else:
                print(socket_item.recv(5).decode("utf-8"))

        for write_item in write_list:
            pass

        for error_item in error_list:
            error_item.close()
            rlist.remove(error_item)


# -----------------------------------------------------------------------


def epoll_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    server.setblocking(False)  # 设置成非阻塞

    connections = {}
    epoll_obj = select.epoll()
    print(f"files: {server.fileno()}")
    epoll_obj.register(
        server.fileno(), select.EPOLLIN | select.EPOLLOUT | select.EPOLLERR
    )

    while True:
        print("wait accept")
        events = epoll_obj.poll()
        print(events)

        for fd, event in events:
            if fd == server.fileno():
                conn, address = server.accept()
                conn.setblocking(False)
                epoll_obj.register(conn.fileno(), select.EPOLLIN)
                connections[conn.fileno()] = conn
            else:
                if event & select.EPOLLIN:
                    data = connections[fd].recv(5).decode("utf-8")
                    if data == "end" or not data:
                        epoll_obj.unregister(fd)
                        connections[fd].close()
                        del connections[fd]
                    else:
                        print(data)
                elif event & select.EPOLLOUT:
                    print(event, "out")
                    pass
                elif event & select.EPOLLERR:
                    print(f"{fd} error")
                    epoll_obj.unregister(fd)
                    connections[fd].close()
                    del connections[fd]


if __name__ == "__main__":
    pass
