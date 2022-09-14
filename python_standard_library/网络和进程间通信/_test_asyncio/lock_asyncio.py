"""
asyncio lock 设计为 与 thread 模块类似的结构

非线程安全， 不能用于线程同步
不接受timeout参数， 请使用asyncio.wait_for()函数执行带有超时的操作

"""
import asyncio

"""
Lock
"""


async def _test_lock():
    """
    公平锁
    """
    lock = asyncio.Lock()
    async with lock:
        pass


"""
Event, 通知多个 asyncio 任务已经有事件发生
"""

async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('got it !')

async def _test_event():
    event = asyncio.Event()
    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))
    # Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    event.set()
    await waiter_task


"""
Condition

综合 Lock 与 Event
"""

async def _test_condition():
    cond = asyncio.Condition()
    async with cond:
        await cond.wait()


"""
信号量

内部计数器 acquire()调用递减， release()调用递增。 不能小于零， 为0时acquire会阻塞
"""

async def _test_semphore():
    sem = asyncio.Semaphore(10)
    async with sem:
        pass


if __name__ == '__main__':
    asyncio.run(_test_event())