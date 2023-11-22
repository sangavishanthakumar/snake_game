from snake import Snake
from food import Food


class Game:
    def __init__(self, number_of_cells, OFF_SET, cell_size, DARK_GREEN, screen):
        self.snake = Snake(OFF_SET, cell_size, DARK_GREEN, screen)
        self.food = Food(self.snake.body, OFF_SET, cell_size, DARK_GREEN, screen, number_of_cells)
        self.state = "STOPPED"
        self.number_of_cells = number_of_cells

    def draw(self):
        self.snake.draw()
        self.food.draw()

    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True

    def check_collision_with_edges(self):
        if self.snake.body[0].x == self.number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == self.number_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        # add game over behaviour
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
