import pygame

class Settings:

    def __init__(self):
        pygame.init()

        # Screen.
        self.screen_width: int = 800
        self.screen_height: int = 480
        self.caption: str = "Tick Oat Two"

        # Background.
        self.background_color: int = 0x000000

        # Board.
        self.board_background_color: int = 0x000000
        self.board_outline_color: int = 0xffffff
        self.horizontal_line_color: int = 0xff0000
        self.vertical_line_color: int = 0x0000ff

        # Turn display.
        self.turn_display_background_color: int = 0x202020
        self.turn_display_outline_color: int = 0xffffff
