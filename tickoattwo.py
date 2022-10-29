import pygame
from game_board import *
from settings import Settings
from turn_display import TurnDisplay
import sys
import time

class TickoatTwo:

    def __init__(self):
        pygame.init()

        # Settings.
        self.settings: Settings = Settings()

        # Screen.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(self.settings.caption)

        # Timing.
        self.fps = 0
        self.last_update = time.time()

        # Game board.
        self.game_board: GameBoard = GameBoard(pygame.Rect(10, 10, 300, 300), self)

        # Turn display.
        self.turn_display: TurnDisplay = TurnDisplay(pygame.Rect(320, 10, 100, 100), self)


    def draw(self) -> None:
        # Full background.
        self.screen.fill(self.settings.background_color, self.screen_rect)

        self.game_board.draw()
        self.turn_display.draw()

        # Update display.
        pygame.display.update()


    def update(self) -> None:
        self.event_loop()

        # Get fps.
        current_time = time.time()
        self.fps = current_time - self.last_update
        self.last_update = current_time

        if self.fps != 0:
            self.fps = 1.0 / self.fps


    def reset(self) -> None:
        self.game_board.reset()
        self.turn_display.reset()
    

    def event_loop(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = self.game_board.screen_point_to_board(pygame.mouse.get_pos())

                if pos == ():
                    continue

                if pygame.mouse.get_pressed()[0]:
                    self.game_board.set_line(pos, HORIZONTAL_LINE)
                elif pygame.mouse.get_pressed()[2]:
                    self.game_board.set_line(pos, VERTICAL_LINE)

                if self.game_board.is_there_3_in_a_row():
                    print("Three in a row!")
                    self.reset()
