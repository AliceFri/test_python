"""
子进程 用asyncio创建运行子进程

asyncio.create_subprocess_shell 等
"""
import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()
    print(f'[{cmd} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout] {stdout.decode()}')
    if stderr:
        print(f'[stderr] {stderr.decode()}')


async def gather_run():
    await asyncio.gather(run('ls'), run('echo "hello"'))


if __name__ == '__main__':
    # asyncio.run(run('sl'))
    asyncio.run(gather_run())