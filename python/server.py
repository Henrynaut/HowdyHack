import asyncio
import websockets
import nest_asyncio

nest_asyncio.apply()
__import__('IPython').embed()

async def communication(websocket, path):
    #uri = await websocket.recv()
    await websocket.send(uri)
    waveData = await websocket.recv()  

start_server = websockets.serve(communication, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()