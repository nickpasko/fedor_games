import arcade
import random
import math
import copy
# Размеры реального экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_CELL_SIZE = 10
SCREEN_TITLE = "Snake Clone"
WAITING_TIME = 1 / 10

class Coin(arcade.SpriteCircle):
    def __init__(self, size, color):
        super().__init__(size, color)
        self.center_x = -100
        self.center_y = -100

    def jump(self):
        self.center_x = random.randint(1, (SCREEN_WIDTH / SCREEN_CELL_SIZE) - 1) * SCREEN_CELL_SIZE
        self.center_y = random.randint(1, (SCREEN_HEIGHT / SCREEN_CELL_SIZE) - 1) * SCREEN_CELL_SIZE


class SnakeSegment(arcade.Sprite):
    def __init__(self, center_x, center_y, direction, filename):
        super().__init__(filename)
        self.center_x = center_x
        self.center_y = center_y
        self.direction = direction
        self.name = filename

    def updatePosition(self, direction):
        if direction == arcade.key.LEFT:
            self.center_x -= SCREEN_CELL_SIZE
        elif direction == arcade.key.RIGHT:
            self.center_x += SCREEN_CELL_SIZE
        elif direction == arcade.key.UP:
            self.center_y += SCREEN_CELL_SIZE
        elif direction == arcade.key.DOWN:
            self.center_y -= SCREEN_CELL_SIZE

        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
    def updateDirection(self, direction):
        if direction == arcade.key.LEFT:
            self.angle = 90
        elif direction == arcade.key.RIGHT:
            self.angle = -90
        elif direction == arcade.key.UP:
            self.angle = 0
        elif direction == arcade.key.DOWN:
            self.angle = 180
        self.direction = direction

class SnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.waiter = 0
        self.snake_sound = arcade.load_sound("Snake.m4a")
        self.coin_sound = arcade.load_sound("Coin.m4a")
        self.snakeBody = []
        self.snakeBody.append(SnakeSegment(SCREEN_CELL_SIZE, SCREEN_CELL_SIZE, arcade.key.UP, "SnakeHead.png"))
        self.snakeLen = 1
        self.coin = Coin(4, arcade.color.GOLD)
        self.snakeDirection = arcade.key.UP

    def setup(self):
        self.coin.jump()
    def on_draw(self):
        arcade.start_render()
        for bodySegment in self.snakeBody:
            bodySegment.draw()
        self.coin.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT and not self.snakeDirection == arcade.key.RIGHT:
            self.snakeDirection = key
        elif key == arcade.key.RIGHT and not self.snakeDirection == arcade.key.LEFT:
            self.snakeDirection = key
        elif key == arcade.key.UP and not self.snakeDirection == arcade.key.DOWN:
            self.snakeDirection = key
        elif key == arcade.key.DOWN and not self.snakeDirection == arcade.key.UP:
            self.snakeDirection = key

    def on_update(self, delta_time: float):
        fileName = ""
        self.waiter += delta_time
        if self.waiter < WAITING_TIME:
            return
        self.waiter = 0
        arcade.play_sound(self.snake_sound)
        for i in range(1, self.snakeLen):
            if self.snakeBody[0].center_x == self.snakeBody[i].center_x and self.snakeBody[0].center_y == self.snakeBody[i].center_y:
                exit
        if arcade.check_for_collision(self.snakeBody[0], self.coin):
            arcade.play_sound(self.coin_sound)
            self.snakeLen += 1
            if self.snakeLen == 2:
                fileName = "SnakeTail.png"
            elif self.snakeLen > 2:
                fileName = "SnakeBody.png"
            self.snakeBody.insert(1, SnakeSegment(self.snakeBody[0].center_x, self.snakeBody[0].center_y, self.snakeBody[0].direction, fileName))
            self.coin.jump()
        else:
            # for i in range(1, self.snakeLen):
            #     self.snakeBody[i].updatePosition(self.snakeBody[i].direction)

            for i in range(self.snakeLen-1, 0, -1):
                self.snakeBody[i].center_x = self.snakeBody[i-1].center_x
                self.snakeBody[i].center_y = self.snakeBody[i-1].center_y
                self.snakeBody[i].updateDirection(self.snakeBody[i-1].direction)

        self.snakeBody[0].updatePosition(self.snakeDirection)
        self.snakeBody[0].updateDirection(self.snakeDirection)

def main():
    game = SnakeGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
