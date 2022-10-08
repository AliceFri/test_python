"""
asyncio 是用来编写 并发 代码的库， 使用 async/await 语法

asyncio 提供 高层级 API:
    1. 协程与任务
    2. 流
    3. 同步原语
    4. 子进程集
    5. 队列集
    6. 异常

低层级 API：
    1. 事件循环
    2. Futures
    3. 传输和协议
    4. 策略
    5. 平台支持
"""
import asyncio
import time


# 协程和任务


async def t1():
    """
    打印 hello 等待 1s 再打印 world
    """

    print('hello')
    await asyncio.sleep(1)
    print('world')


async def t2():
    """
    调用 t1
    """
    await t1()


"""
运行一个协程
1. asyncio.run()
2. 等待一个协程， 如 t2
3. asyncio.create_task() 函数并发运行作为 asyncio 任务的多个协程
"""


async def say_after(delay: int, what: str):
    await asyncio.sleep(delay)
    print(what)


async def say_helloworld():
    """
    会等待 1s 打印 hello， 而后等待 2s 打印 world
    """
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")


async def async_say_helloworld():
    """
    通过 asyncio.create_task, 并发运行作为 asyncio 任务的多个协程
    """

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")
    # Wait until both tasks are completed (should take around 2 seconds.)
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


"""
awaitable 对象

主要 协程， 任务 和 Future
"""

"""
并发运行 任务
awaitable asyncio.gather(*aws, return_exceptions=False)
"""


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i = {i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def run_gather():
    """
    测试 asyncio.gather 等同于 create_task 然后 await
    """
    print(f"started at {time.strftime('%X')}")
    L = await asyncio.gather(factorial('A', 4), factorial('B', 4), factorial('C', 5))
    print(f"finished at {time.strftime('%X')}")
    print(L)

"""
asyncio.wait_for    带超时时间的等待
asyncio.wait        在超时发生时不会取消可等待对象。
"""


if __name__ == '__main__':
    # asyncio.run(t2())
    asyncio.run(say_helloworld())
    # asyncio.run(async_say_helloworld())
    # asyncio.run(run_gather())