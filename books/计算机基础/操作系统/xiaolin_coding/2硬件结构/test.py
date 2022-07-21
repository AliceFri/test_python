import time

if __name__ == '__main__':
    arr = [[0] * 10000 for i in range(10000)]

    t1 = time.time()

    for a in range(10000):
        for b in range(10000):
            arr[a][b] = 0
    t2 = time.time()
    print(t2 - t1)

    for a in range(10000):
        for b in range(10000):
            arr[b][a] = 0

    t3 = time.time()
    print(t3 - t2)
