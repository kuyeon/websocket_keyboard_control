#!/usr/bin/env python

# WS server example

import asyncio
import keyboard
import websockets
import json
import time
import threading


DEFAULT_VELOCITY = 5
vel = DEFAULT_VELOCITY
publish_data = {}

async def dic_to_json(dic_fmt):
    json_fmt = json.dumps(dic_fmt)
    return json_fmt
    

def KeyBoard_Vel_Ctrl():
    global vel

    if keyboard.is_pressed(keyboard.KEY_UP):
        if vel < 50:
            vel += 5
    elif keyboard.is_pressed(keyboard.KEY_DOWN):
        if vel > -50:
            vel -= 5
    else:
        pass



async def web_server(websocket, path):
    publish_data = { 
        "Mode": "Manual",
        "Homing": "NO",
        "STOP": "NO",
        "TargetPosition": 40000,
        "Velocity": vel,
        "Lamp": "NO",
        "Buzzer": "NO",
        "Timestamp": int(time.time())
    }

    json_data = await dic_to_json(publish_data)
    await websocket.send(json_data)

    client_data = await websocket.recv()
    converted_data = json.loads(client_data)
    print(converted_data)

    thread1 = threading.Thread(target=KeyBoard_Vel_Ctrl)
    thread1.start()

    
start_server = websockets.serve(web_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

