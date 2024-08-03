import asyncio
import websockets

async def send_message_and_listen():
    uri = "wss://melbet.com/games-frame/sockets/crash?whence=55&fcountry=125&ref=8&gr=62&appGuid=00000000-0000-0000-0000-000000000000&lng=en"
    async with websockets.connect(uri) as websocket:
        # Send the initial message {"type": 6}
        await websocket.send('{"type": 6}')
        print("Sent message: {'type': 6}")

        # Listen for incoming messages
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

asyncio.run(send_message_and_listen())
