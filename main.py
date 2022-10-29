#! /usr/bin/python3

import asyncio
import pygame
from tickoattwo import TickoatTwo

pygame.init()

async def main():
    tick_oat_two = TickoatTwo()

    while True:
        tick_oat_two.update()
        tick_oat_two.draw()
        await asyncio.sleep(0)


asyncio.run(main())
