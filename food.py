import pygame, random
from pygame.math import Vector2


class Food:
    def __init__(self, snake_body, OFF_SET, cell_size, DARK_GREEN, screen, number_of_cells):
        self.number_of_cells = number_of_cells
        self.position = self.generate_random_pos(snake_body)
        # access x, y coordinates:
        # self.position.x
        # self.position.y
        self.OFF_SET = OFF_SET
        self.cell_size = cell_size
        self.DARK_GREEN = DARK_GREEN
        self.screen = screen


    def draw(self):
        food_rect = pygame.Rect(self.OFF_SET + self.position.x * self.cell_size,
                                self.OFF_SET + self.position.y * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, self.DARK_GREEN, food_rect)

    def generate_random_cell(self):
        x = random.randint(0, self.number_of_cells - 1)
        y = random.randint(0, self.number_of_cells - 1)
        return Vector2(x, y)

    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()
        while position in snake_body:
            x = random.randint(0, self.number_of_cells - 1)
            y = random.randint(0, self.number_of_cells - 1)
            position = self.generate_random_cell()

        return position
