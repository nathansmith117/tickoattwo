#! /usr/bin/python3

import pygame
from tickoattwo import TickoatTwo

pygame.init()

def main():
    tick_oat_two = TickoatTwo()

    while True:
        tick_oat_two.update()
        tick_oat_two.draw()


if __name__ == "__main__":
    main()
