#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import time
import json


async def robot_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        publish_data = {
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

        json_data = json.dumps(publish_data)
        await websocket.send(json_data)

        data = await websocket.recv()
        data = json.loads(data)
        print(data)
        await asyncio.sleep(0.5)

while True:
    asyncio.get_event_loop().run_until_complete(robot_client())