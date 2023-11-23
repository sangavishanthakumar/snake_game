# game based on https://www.youtube.com/watch?v=1zVlRXd8f7g
import sys

import pygame
from game import Game

from pygame.math import Vector2

pygame.init()
# settings


buffer_size = 10
buffer_cell_size = 20
buffer_offset = 50

title_font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 40)

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 35
number_of_cells = 15

OFF_SET = 75

screen = pygame.display.set_mode((2 * OFF_SET + cell_size * number_of_cells, 2 * OFF_SET + cell_size * number_of_cells))

pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

game = Game(number_of_cells, OFF_SET, cell_size, DARK_GREEN, screen)

SNAKE_UPDATE = pygame.USEREVENT
# trigger the event every 200 ms
pygame.time.set_timer(SNAKE_UPDATE, 200)


def draw_buffer(screen, buffer_values, buffer_size, x_start, y_start, cell_width, cell_height, font, gap):
    for i in range(buffer_size):
        # X-Position bleibt konstant, da der Buffer vertikal gezeichnet wird
        x = x_start

        # Y-Position berechnet sich aus der Startposition, der Höhe jeder Zelle und dem Abstand zwischen ihnen
        y = y_start + i * (cell_height + gap)

        # Zeichnen Sie den Hintergrund des Registers
        pygame.draw.rect(screen, (128, 128, 128), (x, y, cell_width, cell_height))

        # Fügen Sie den Text des Registerwerts hinzu
        text_surface = font.render(f"{buffer_values[i]:02X}", True, (255, 255, 255))

        # Zentrieren Sie den Text im Rechteck
        text_rect = text_surface.get_rect(center=(x + cell_width / 2, y + cell_height / 2))

        # Zeichnen Sie den Text auf das Rechteck
        screen.blit(text_surface, text_rect)


def draw_registers(screen, register_values, x_start, y_start, width, height, font):
    for i, value in enumerate(register_values):
        # register background
        pygame.draw.rect(screen, (0, 0, 0), (x_start, y_start + i * height, width, height))

        # register text
        if value != 0:
            text_surface = font.render(value, True, (255, 255, 255))
            screen.blit(text_surface, (x_start + 5, y_start + i * height + 5))


# register settings
cell_width = 50  # register width
cell_height = 20  # register heigt
gap = 0.5  # register gap

font_size = 20
buffer_font = pygame.font.Font(None, font_size)

# buffer placement
x_start = screen.get_width() - buffer_offset - cell_width
y_start = OFF_SET

# example buffer
# buffer_values = [0x10, 0x20, 0x30, 0x40, 0x50]

while True:
    for event in pygame.event.get():
        if game.speed_boost_active:
            pygame.time.set_timer(SNAKE_UPDATE, 100)
        else:
            pygame.time.set_timer(SNAKE_UPDATE, 200)
        if event.type == SNAKE_UPDATE:
            game.update()
        if event.type == pygame.QUIT:
            sys.exit()
        # add keyboard detection
        if event.type == pygame.KEYDOWN:
            if game.state == "STOPPED":
                game.state = "RUNNING"
                game.score = 0

            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)



    screen.fill(GREEN)

    if game.show_overflow_message:
        overflow_message_surface = score_font.render("Buffer Overflow!", True, (255, 0, 0))
        x_position = screen.get_width() // 2 - overflow_message_surface.get_width() // 2
        y_position = screen.get_height() // 2 - overflow_message_surface.get_height() // 2
        screen.blit(overflow_message_surface, (x_position, y_position))

    pygame.draw.rect(screen, DARK_GREEN,
                     (OFF_SET - 5, OFF_SET - 5, cell_size * number_of_cells + 10, cell_size * number_of_cells + 10), 5)
    game.draw()
    title_surface = title_font.render("Snake", True, DARK_GREEN)
    score_surface = score_font.render(str(game.score), True, DARK_GREEN)
    screen.blit(title_surface, (OFF_SET - 5, 20))
    screen.blit(score_surface, (OFF_SET - 5, OFF_SET + cell_size * number_of_cells + 10))

    # draw highscore
    if game.state == "STOPPED":
        highscore_surface = score_font.render("Highscore: " + str(game.highscore), True, DARK_GREEN)
        screen.blit(highscore_surface, (OFF_SET, OFF_SET + cell_size * number_of_cells + 30))

    # draw buffer
    # draw_buffer(screen, buffer_values, 5, x_start, y_start, cell_width, cell_height, buffer_font, gap)
    draw_registers(screen, game.register_values, x_start, y_start, cell_width, cell_height, buffer_font)

    pygame.display.update()
    clock.tick(60)  # 60 fps
