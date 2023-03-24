import asyncio
import pathlib
import ssl
import websockets

async def chat(websocket, path):
    while True:
        msg = await websocket.recv()
        print(f"From Client: {msg}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('/var/www/html/stami/tiktokshazam/certs/cert.pem', '/var/www/html/stami/tiktokshazam/certs/key.pem')
start_server = websockets.serve(
	chat, 'localhost', 4727, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()