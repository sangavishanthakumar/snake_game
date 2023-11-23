import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self, OFF_SET, cell_size, DARK_GREEN, screen, number_of_cells):
        self.body = [Vector2(6, 5), Vector2(5, 5), Vector2(4, 5)]
        self.direction = Vector2(1, 0)
        self.add_segment = False
        self.OFF_SET = OFF_SET
        self.cell_size = cell_size
        self.DARK_GREEN = DARK_GREEN
        self.screen = screen
        self.god_mode = False
        self.number_of_cells = number_of_cells

    def draw(self):
        for index, segment in enumerate(self.body):
            x = self.OFF_SET + segment.x * self.cell_size
            y = self.OFF_SET + segment.y * self.cell_size
            segment_rect = pygame.Rect(x, y, self.cell_size, self.cell_size)

            if index == 0:
                pygame.draw.rect(self.screen, self.DARK_GREEN, segment_rect) # change head colour here
            else:
                pygame.draw.rect(self.screen, self.DARK_GREEN, segment_rect) # change body colour here

    def update(self):
        new_head = self.body[0] + self.direction

        if self.god_mode:
            new_head.x = new_head.x % self.number_of_cells
            new_head.y = new_head.y % self.number_of_cells
        else:
            if not 0 <= new_head.x < self.number_of_cells or not 0 <= new_head.y < self.number_of_cells:
                pass

        self.body.insert(0, new_head)
        if not self.add_segment:
            self.body.pop()
        else:
            self.add_segment = False


    def reset(self):
        self.body = [Vector2(6, 5), Vector2(5, 5), Vector2(4, 5)]
        self.direction = Vector2(1, 0)
