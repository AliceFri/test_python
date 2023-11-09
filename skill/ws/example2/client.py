import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8001"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")
        return greeting


def run_hello():
    a = asyncio.run(hello())
    print('a:', a)


if __name__ == "__main__":
    run_hello()
