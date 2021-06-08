import json


publish_fmt = { 
    "Mode": ["Auto", "Manual"],
    "Homing": ["YES", "NO"],
    "STOP": ["YES", "NO"],
    "TargetPosition": "m",
    "Velocity": "m/s",
    "Lamp": ["YES", "NO"],
    "Buzzer": ["YES", "NO"],
    "Timestamp":0
}


publish_data = json.dumps(publish_fmt)

print(publish_data)

print(publish_fmt["Mode"])