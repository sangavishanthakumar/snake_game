import pygame
import random
from pygame.math import Vector2

class SpeedBoost:
    def __init__(self, number_of_cells, OFF_SET, cell_size, screen):
        self.number_of_cells = number_of_cells
        self.OFF_SET = OFF_SET
        self.cell_size = cell_size
        self.screen = screen
        self.position = self.generate_new_position([])

    # draw red rect for a speed bost object
    # def draw(self):
    #     # Zeichnen Sie den SpeedBoost auf dem Bildschirm
    #     boost_rect = pygame.Rect(self.OFF_SET + self.position.x * self.cell_size,
    #                              self.OFF_SET + self.position.y * self.cell_size,
    #                              self.cell_size, self.cell_size)
    #     pygame.draw.rect(self.screen, (255, 0, 0), boost_rect)

    def generate_new_position(self, snake_body):
        while True:
            x = random.randint(0, self.number_of_cells - 1)
            y = random.randint(0, self.number_of_cells - 1)
            position = Vector2(x, y)
            if position not in snake_body:
                return position
