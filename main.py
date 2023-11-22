# game based on https://www.youtube.com/watch?v=1zVlRXd8f7g
import sys

import pygame
from game import Game

from pygame.math import Vector2

pygame.init()

# settings

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 15
number_of_cells = 10

OFF_SET = 75

screen = pygame.display.set_mode((2*OFF_SET+cell_size * number_of_cells, 2*OFF_SET+cell_size * number_of_cells))

pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

game = Game(number_of_cells, OFF_SET, cell_size, DARK_GREEN, screen)

SNAKE_UPDATE = pygame.USEREVENT
# trigger the event every 200 ms
pygame.time.set_timer(SNAKE_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()
        if event.type == pygame.QUIT:
            sys.exit()
        # add keyboard detection
        if event.type == pygame.KEYDOWN:
            if game.state =="STOPPED":
                game.state="RUNNING"

            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)
    screen.fill(GREEN)
    pygame.draw.rect(screen, DARK_GREEN, (OFF_SET-5, OFF_SET-5, cell_size*number_of_cells+1,cell_size*number_of_cells+1 ), 5)
    game.draw()

    pygame.display.update()
    clock.tick(60)  # 60 fps
