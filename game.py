from snake import Snake
from food import Food
from speedboost import SpeedBoost


class Game:
    def __init__(self, number_of_cells, OFF_SET, cell_size, DARK_GREEN, screen):
        self.snake = Snake(OFF_SET, cell_size, DARK_GREEN, screen)
        self.food = Food(self.snake.body, OFF_SET, cell_size, DARK_GREEN, screen, number_of_cells)
        self.speed_boost = SpeedBoost(number_of_cells, OFF_SET, cell_size, screen)
        self.state = "STOPPED"
        self.number_of_cells = number_of_cells
        self.speed_boost_active = False
        self.speed_boost_timer = 0
        self.score = 0
        self.highscore = 0

    def draw(self):
        self.snake.draw()
        self.food.draw()
        # self.speed_boost.draw()

    def update(self):
        if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()
            # self.check_collision_with_speed_boost()

        if self.speed_boost_active:
            self.speed_boost_timer -= 1
            if self.speed_boost_timer <= 0:
                self.speed_boost_active = False

    # def check_collision_with_speed_boost(self):
    #     if self.snake.body[0] == self.speed_boost.position:
    #         self.speed_boost_active = True
    #         self.speed_boost_timer = 300
    #         self.speed_boost.position = self.speed_boost.generate_new_position(self.snake.body)

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True

            self.speed_boost_active = True
            self.speed_boost_timer = 300

            self.score += 1

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
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
