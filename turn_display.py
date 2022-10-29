import pygame
from game_board import *
from settings import Settings
from random import choice

class TurnDisplay:

    def __init__(self, rect, tick_oat_two):
        pygame.init()

        # Tick oat two class.
        self.tick_oat_two = tick_oat_two
        self.screen: pygame.Surface = self.tick_oat_two.screen
        self.screen_rect: pygame.Rect = self.tick_oat_two.screen_rect
        self.settings: Settings = self.tick_oat_two.settings

        # Size.
        self.rect: pygame.Rect = rect

        # Lines.
        self.horizontal_line: tuple = ()
        self.vertical_line: tuple = ()

        # Boxs.
        self.box_width: int = 0

        # Current line.
        self.current_line: int = 0

        self.reset()


    def reset(self) -> None:

        # Screen and settings.
        self.screen = self.tick_oat_two.screen
        self.screen_rect = self.tick_oat_two.screen_rect
        self.settings: Settings = self.tick_oat_two.settings

        # Box width.
        self.box_width = self.rect.width

        # Lines.
        box_center = self.box_width // 2
        start_pos = self.box_width // 3
        end_pos = self.box_width - start_pos
        horizontal_line_y = start_pos + ((end_pos - start_pos) // 3)

        horizontal_line = [[start_pos, horizontal_line_y], [end_pos, horizontal_line_y]]
        vertical_line = [[box_center, start_pos], [box_center, end_pos]]

        # Move to position.
        move_to_position = lambda x: (x[0] + self.rect.left, x[1] + self.rect.top)
        self.horizontal_line = tuple(map(move_to_position, horizontal_line))
        self.vertical_line = tuple(map(move_to_position, vertical_line))

        # Current line.
        self.current_line = choice([HORIZONTAL_LINE, VERTICAL_LINE])


    def swap_current_line(self) -> None:
        self.current_line ^= 1


    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.settings.turn_display_background_color, self.rect)

        if self.current_line == HORIZONTAL_LINE:
            pygame.draw.line(
                self.screen,
                self.settings.horizontal_line_color,
                self.horizontal_line[0],
                self.horizontal_line[1]
            )
        elif self.current_line == VERTICAL_LINE:
            pygame.draw.line(
                self.screen,
                self.settings.vertical_line_color,
                self.vertical_line[0],
                self.vertical_line[1]
            )
