import pygame
from settings import Settings

pygame.init()

BOARD_SIZE = 3

HORIZONTAL_LINE: int = 0
VERTICAL_LINE: int = 1

class GameBoard:

    def __init__(self, rect, tick_oat_two):

        # Tick oat two class.
        self.tick_oat_two = tick_oat_two
        self.screen = self.tick_oat_two.screen
        self.screen_rect = self.tick_oat_two.screen_rect
        self.settings: Settings = self.tick_oat_two.settings

        # Size.
        self.rect = rect

        # Board.
        # Format [[has_horizontal, has_vertical] ...]
        self.board_data: list = []
        self.board_outline: list = []

        # Lines.
        self.horizontal_line: tuple = ()
        self.vertical_line: tuple = ()

        # Boxs.
        self.box_size: int = 0

        self.reset()


    def reset(self) -> None:
        # Board.
        self.board_data = [[False, False]] * (BOARD_SIZE ** 2)

        first_line_pos = int((1 / 3) * self.rect.width)
        second_line_pos = int((2 / 3) * self.rect.width)

        # Box size.
        self.box_size = self.rect.width // BOARD_SIZE

        # Board lines.
        # Format [((start_x, start_y), (end_x, end_y)) ... ]
        self.board_outline = [
            (
            (self.rect.left + first_line_pos, self.rect.top),
            (self.rect.left + first_line_pos, self.rect.top + self.rect.height)
            ),

            (
            (self.rect.left + second_line_pos, self.rect.top),
            (self.rect.left + second_line_pos, self.rect.top + self.rect.height)
            ),

            (
            (self.rect.left, self.rect.top + first_line_pos),
            (self.rect.left + self.rect.width, self.rect.top + first_line_pos)
            ),

            (
            (self.rect.left, self.rect.top + second_line_pos),
            (self.rect.left + self.rect.width, self.rect.top + second_line_pos),
            )
        ]

        # Lines.


    def set_line(self, x: int, y: int, line: int) -> None:
        self.board_data[x + (y * BOARD_SIZE)][line] = True


    def get_box(self, x: int, y: int) -> tuple:
        return tuple(self.board_data[x + (y * BOARD_SIZE)])


    def draw_box(self, x: int, y: int) -> None:

        # No board.
        if self.board_data == []:
            return

        current_box = self.get_box(x, y)

        # Draw position.
        draw_x = self.rect.left + (x * self.box_size)
        draw_y = self.rect.top + (y * self.box_size)

        # Draw.
        if current_box[HORIZONTAL_LINE] or True:
            pygame.draw.rect(self.screen, 0xff0000, (draw_x, draw_y, self.box_size, self.box_size))
        if current_box[VERTICAL_LINE]:
            pygame.draw.rect(self.screen, 0xff0000, (draw_x, draw_y, self.box_size, self.box_size))


    def draw(self) -> None:

        # No board lines.
        if self.board_outline == []:
            return

        # Draw board lines.
        for line in self.board_outline:
            pygame.draw.line(self.screen, self.settings.board_outline_color, line[0], line[1])

        # Draw board data.
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                self.draw_box(x, y)
