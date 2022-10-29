import asyncio
import pygame
from tickoattwo import TickoatTwo

# Try explicitly to declare all your globals at once to facilitate compilation later.
COUNT_DOWN = 3

# Do init here and load any assets right now to avoid lag at runtime or network errors.

pygame.init()

async def main():
    global COUNT_DOWN

    COUNT_DOWN = 3

    tick_oat_two = TickoatTwo()

    while True:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop, maybe less on some mobile devices

        tick_oat_two.update()
        tick_oat_two.draw()

        await asyncio.sleep(0)  # Very important, and keep it 0

        if not COUNT_DOWN:
            return

        COUNT_DOWN = COUNT_DOWN - 1

# This is the program entry point:
asyncio.run(main())

# Do not add anything from here
# asyncio.run is non-blocking on pygame-wasm
