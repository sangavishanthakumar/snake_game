import pygame
from pygame.math import Vector2


class Snake:
    def __init__(self, OFF_SET, cell_size, DARK_GREEN, screen):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
        self.add_segment = False
        self.OFF_SET = OFF_SET
        self.cell_size = cell_size
        self.DARK_GREEN = DARK_GREEN
        self.screen = screen

    def draw(self):
        for segment in self.body:
            segment_rect = (self.OFF_SET+segment.x * self.cell_size, self.OFF_SET+segment.y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, self.DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)  # enlarge snake
        if self.add_segment:
            self.add_segment = False
        # simulate movement
        else:
            self.body = self.body[:-1]  # remove last element

    def reset(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
