#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json
import keyboard
import time

DEFAULT_VELOCITY = 5
vel = DEFAULT_VELOCITY

publish_fmt = { 
    "Mode": "Manual",
    "Homing": "NO",
    "STOP": "NO",
    "TargetPosition": 40000,
    "Velocity": vel,
    "Lamp": "NO",
    "Buzzer": "NO",
    "Timestamp": int(time.time())
}

async def pub_data():
    global vel, publish_fmt

    data = json.dumps(publish_fmt)
    return data
    


async def Velocity_Control():
    if keyboard.read_key() == keyboard.KEY_UP:
        global vel
        if vel < 50:
            vel += 5
            return vel
        elif vel == 50:
            return vel
    elif keyboard.read_key() == keyboard.KEY_DOWN:
        if vel > -50:
            vel -= 5
            return vel
        elif vel == -50:
            return vel


async def web_server(websocket, path):
    global vel, publish_fmt

    publish_data = await pub_data()
    await websocket.send(publish_data)

    #subscribe_data = await websocket.recv()
    #subscribe_data = json.loads(subscribe_data)
    #print(subscribe_data)

    publish_fmt["Velocity"] = await asyncio.wait_for(Velocity_Control(), timeout=1.0)




start_server = websockets.serve(web_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
