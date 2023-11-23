import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self, OFF_SET, cell_size, DARK_GREEN, screen):
        self.body = [Vector2(6, 5), Vector2(5, 5), Vector2(4, 5)]
        self.direction = Vector2(1, 0)
        self.add_segment = False
        self.OFF_SET = OFF_SET
        self.cell_size = cell_size
        self.DARK_GREEN = DARK_GREEN
        self.screen = screen

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
        self.body.insert(0, self.body[0] + self.direction)  # enlarge snake
        if self.add_segment:
            self.add_segment = False
        # simulate movement
        else:
            self.body = self.body[:-1]  # remove last element

    def reset(self):
        self.body = [Vector2(6, 5), Vector2(5, 5), Vector2(4, 5)]
        self.direction = Vector2(1, 0)
