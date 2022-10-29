import pygame
from game_board import GameBoard
from settings import Settings
import time

pygame.init()

class TickoatTwo:

    def __init__(self):

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


    def draw(self) -> None:
        # Full background.
        self.screen.fill(self.settings.background_color, self.screen_rect)

        self.game_board.draw()

        # Update display.
        pygame.display.update()


    def update(self) -> None:

        # Get fps.
        current_time = time.time()
        self.fps = current_time - self.last_update
        self.last_update = current_time

        if self.fps != 0:
            self.fps = 1.0 / self.fps

        pygame.display.set_caption(f"fps {self.fps}")
