from typing import AsyncIterable
from pynput.keyboard import Key, Listener
import asyncio



async def main():
    print("hello")
    await asyncio.sleep(1)
    def on_press(key):
        print('{0} pressed'.format(
            key))

    def on_release(key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
        # Stop listener
            return False

# Collect events until released
    with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

while True:
    asyncio.run(main())