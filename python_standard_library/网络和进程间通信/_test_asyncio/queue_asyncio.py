import asyncio
import random
import time

"""
asyncio 队列被设计成与 queue 模块类似。尽管 asyncio队列不是线程安全的，但是他们是被设计专用于 async/await 代码。

队列能被用于多个的并发任务的工作量分配
"""

async def worker(name, queue):
    while True:
        sleep_for = await queue.get()
        await asyncio.sleep(sleep_for)
        queue.task_done()
        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    queue = asyncio.Queue()

    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    for task in tasks:
        task.cancel()
    # wait until all worker tasks are cancelled
    await asyncio.gather(*tasks, return_exceptions=True)

    print(f'===== {total_slept_for:.2f}  {total_sleep_time:.2f}')


if __name__ == '__main__':
    asyncio.run(main())