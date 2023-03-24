import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 4727):
        await asyncio.Future()  # run forever

asyncio.run(main())