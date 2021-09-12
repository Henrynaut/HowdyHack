import asyncio
import websockets
import nest_asyncio
import main.py

nest_asyncio.apply()
__import__('IPython').embed()

async def communication():
    uri = "ws://127.0.0.1:3000/"
    async with websockets.connect(uri) as websocket:
        
        web_url = await websocket.recv()
        
        await websocket.send(main.computations(web_url))

asyncio.get_event_loop().run_until_complete(communication())
