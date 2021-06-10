#!/usr/bin/env python
"""
Title: Websocket Data Transfer and Keyboard Control
Update: 2021-06-10
Author: Park Kuyeon
Reviewer: Hong Beomjin
E-mail: kuyeon99@gmail.com
guthub: https://github.com/ky-devblog/websocket_keyboard_control

Description: 서버-클라이언트 데이터 송수신, 키보드 입력으로 속도값 변경
"""
# WS server example
import asyncio       # 비동기 처리
import keyboard      # 키보드 입력 감지
import websockets    # 웹소켓 모듈
import json          # 제이슨
import time          # 시간
import threading     # 쓰레드 사용

# 전역 변수
DEFAULT_VELOCITY = 0      # 속도값 초기화
vel = DEFAULT_VELOCITY


# 사전형을 JSON 형식으로 변환
def dic_to_json(dic_fmt):
    json_fmt = json.dumps(dic_fmt)
    return json_fmt
    

# 키보드 입력을 받아 속도값을 변경
def KeyBoard_Vel_Ctrl():
    global vel
    
    while True:
        if keyboard.is_pressed(keyboard.KEY_UP):
            if vel < 50:
                vel += 10
            elif vel > 50:
                vel = 50
            time.sleep(0.2)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            if vel > -50:
                vel -= 10
            elif vel < -50:
                vel = -50
            time.sleep(0.2)


# 웹소켓 서버
async def web_server(websocket, path):
    global vel

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

    # 데이터 송신 to 클라이언트
    json_data = dic_to_json(publish_data)
    await websocket.send(json_data)

    # 데이터 수신 from 클라이언트
    client_data = await websocket.recv()
    converted_data = json.loads(client_data)
    print(converted_data)


start_server = websockets.serve(web_server, "localhost", 8765)


# 서버 시작
asyncio.get_event_loop().run_until_complete(start_server)
print("---------> starting server...")
time.sleep(3) # 키입력 방지용 딜레이


# 키보드 입력 쓰레드 시작
print("------------------> Threading start")
time.sleep(3)
thread1 = threading.Thread(target=KeyBoard_Vel_Ctrl)
thread1.start()


# 서버를 영원히 실행
print("-----------------------------------> Complete")
asyncio.get_event_loop().run_forever()