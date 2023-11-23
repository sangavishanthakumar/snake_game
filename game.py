from snake import Snake
from food import Food
from speedboost import SpeedBoost


class Game:
    def __init__(self, number_of_cells, OFF_SET, cell_size, DARK_GREEN, screen):
        self.show_overflow_message = False
        self.snake = Snake(OFF_SET, cell_size, DARK_GREEN, screen, number_of_cells)
        self.food = Food(self.snake.body, OFF_SET, cell_size, DARK_GREEN, screen, number_of_cells)
        self.speed_boost = SpeedBoost(number_of_cells, OFF_SET, cell_size, screen)
        self.state = "STOPPED"
        self.number_of_cells = number_of_cells
        self.speed_boost_active = False
        self.speed_boost_timer = 0
        self.score = 0
        self.highscore = 0
        self.buffer = 0
        self.buffer_limit = 5  # get buffer overflow when the highscore is > 5
        self.god_mode_timer = 0
        self.register_values = ['0x00'] * 5  # init 5 "registers" for the buffer

    def draw(self):
        self.snake.draw()
        self.food.draw()
        # self.speed_boost.draw()

    def update(self):
        if self.god_mode_timer > 0:
            self.god_mode_timer -= 1
            if self.god_mode_timer <= 0:
                self.snake.god_mode = False

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

            self.update_buffer()

            self.update_registers()

    def update_registers(self):
        hex_score = hex(self.score)[2:].upper().zfill(2)
        for i in range(len(self.register_values)):
            if self.register_values[i] == '0x00':
                self.register_values[i] = '0x'+hex_score
                break
        if self.score == 5:
            self.trigger_buffer_overflow()

    def trigger_buffer_overflow(self):
        self.show_overflow_message =  True
        self.register_values = ['0xFF'] * 5

    def check_collision_with_edges(self):
        if self.snake.body[0].x == self.number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == self.number_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def update_buffer(self):
        self.buffer += 1
        if self.buffer >= self.buffer_limit:
            self.activate_god_mode()
            self.buffer = 0

    def activate_god_mode(self):
        self.snake.god_mode = True
        self.god_mode_timer = 600

    def game_over(self):
        # add game over behaviour
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.buffer = 0
        self.register_values = ['0x00'] * 5
