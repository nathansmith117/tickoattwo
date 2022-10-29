import pygame
from settings import Settings

BOARD_SIZE: int = 3

NONE_LINE: int = -1
HORIZONTAL_LINE: int = 0
VERTICAL_LINE: int = 1

class GameBoard:

    def __init__(self, rect: pygame.Rect, tick_oat_two):
        pygame.init()

        # Tick oat two class.
        self.tick_oat_two = tick_oat_two
        self.screen: pygame.Surface = self.tick_oat_two.screen
        self.screen_rect: pygame.Rect = self.tick_oat_two.screen_rect
        self.settings: Settings = self.tick_oat_two.settings

        # Size.
        self.rect: pygame.Rect = rect

        # Board.
        # Format [[has_horizontal, has_vertical] ...]
        self.board_data: list = []
        self.board_outline: list = []

        # Lines.
        self.last_line_added: tuple = ()
        self.horizontal_line: tuple = ()
        self.vertical_line: tuple = ()

        # Boxs.
        self.box_size: int = 0

        self.reset()


    def reset(self) -> None:

        # Screen and settings.
        self.screen = self.tick_oat_two.screen
        self.screen_rect = self.tick_oat_two.screen_rect
        self.settings: Settings = self.tick_oat_two.settings

        # Board.
        self.board_data = []

        for x in range(BOARD_SIZE ** 2):
            self.board_data.append([False, False])

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
        box_center = self.box_size // 2
        start_pos = self.box_size // 3
        end_pos = self.box_size - start_pos
        horizontal_line_y = start_pos + ((end_pos - start_pos) // 3)
        self.horizontal_line = ((start_pos, horizontal_line_y), (end_pos, horizontal_line_y))
        self.vertical_line = ((box_center, start_pos), (box_center, end_pos))

        # Format ((x, y) line)
        self.last_line_added: tuple = ((0, 0), NONE_LINE)


    def set_line(self, pos: tuple, line: int) -> None:
        self.last_line_added = (pos, line)
        self.board_data[pos[0] + (pos[1] * BOARD_SIZE)][line] = True


    def get_box(self, pos: tuple) -> tuple:
        return tuple(self.board_data[pos[0] + (pos[1] * BOARD_SIZE)])


    def draw_box(self, pos: tuple) -> None:

        # No board.
        if self.board_data == []:
            return

        current_box = self.get_box(pos)

        # Draw position.
        draw_x = self.rect.left + (pos[0] * self.box_size)
        draw_y = self.rect.top + (pos[1] * self.box_size)

        # Draw.
        if current_box[HORIZONTAL_LINE]:
            pygame.draw.line(
                self.screen,
                self.settings.horizontal_line_color,
                (self.horizontal_line[0][0] + draw_x, self.horizontal_line[0][1] + draw_y),
                (self.horizontal_line[1][0] + draw_x, self.horizontal_line[1][1] + draw_y)
            )
        if current_box[VERTICAL_LINE]:
            pygame.draw.line(
                self.screen,
                self.settings.vertical_line_color,
                (self.vertical_line[0][0] + draw_x, self.vertical_line[0][1] + draw_y),
                (self.vertical_line[1][0] + draw_x, self.vertical_line[1][1] + draw_y)
            )


    # Returns emply tuple if point not on board.
    def screen_point_to_board(self, pos: tuple) -> tuple:
        x_pos: int = (pos[0] - self.rect.left) // self.box_size
        y_pos: int = (pos[1] - self.rect.top) // self.box_size

        # Not on board.
        if x_pos not in range(BOARD_SIZE):
            return ()
        elif y_pos not in range(BOARD_SIZE):
            return ()

        return (x_pos, y_pos)


    def draw(self) -> None:

        # Background.
        pygame.draw.rect(self.screen, self.settings.board_background_color, self.rect)

        # No board lines.
        if self.board_outline == []:
            return

        # Draw board lines.
        for line in self.board_outline:
            pygame.draw.line(self.screen, self.settings.board_outline_color, line[0], line[1])

        # Draw board data.
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                self.draw_box((x, y))


    def is_t_formed_at_pos(self, pos: tuple) -> bool:
        box_value = self.get_box(pos)
        return box_value[0] and box_value[1]
    

    def is_there_3_in_a_row(self) -> bool:

        # No board.
        if self.board_data == []:
            return False

        # List of places were a t is formed.
        t_data = []

        for y in range(BOARD_SIZE):
            t_data.append([])

            for x in range(BOARD_SIZE):
                t_data[y].append(self.is_t_formed_at_pos((x, y)))

        # Check rows.
        for y in t_data:
            if y[0] and y[1] and y[2]:
                return True

        # Check columns.
        for x in range(BOARD_SIZE):
            if t_data[0][x] and t_data[1][x] and t_data[2][x]:
                return True

        # Check left to right sideways.
        if t_data[0][0] and t_data[1][1] and t_data[2][2]:
            return True

        # Check right to left sideways.
        if t_data[2][0] and t_data[1][1] and t_data[0][2]:
            return True

        return False
