#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import time
import json


async def robot_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        """
        publish_fmt = {
            "BatteryStatus": 100,
            "CurrentPosition": 0,
            "Velocity": 50,
            "Obstacle":"NO",
            "Timestamp":int(time.time()),
            "Sensor":{
                "O2": 10,
                "CO2": 10,
                "Humidity": 10,
                "Temperature": 10
            }
        }

        publish_data = json.dumps(publish_fmt)
        await websocket.send(publish_data)
        """
        data = await websocket.recv()
        data = json.loads(data)
        print(data)
        #key_input = await websocket.recv()
        #print(key_input)

while True:
    asyncio.get_event_loop().run_until_complete(robot_client())
    time.sleep(0.5)