import arcade
import random
import math

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

    def move(self):
        self.center_x = random.randint(1, (SCREEN_WIDTH / SCREEN_CELL_SIZE) - 1) * SCREEN_CELL_SIZE
        self.center_y = random.randint(1, (SCREEN_HEIGHT / SCREEN_CELL_SIZE) - 1) * SCREEN_CELL_SIZE


class Snake(arcade.SpriteSolidColor):
    def __init__(self, center_x, center_y, size, color):
        super().__init__(size, size, color)
        self.center_x = center_x
        self.center_y = center_y
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = True
        self.down_pressed = False

    def update(self):
        if self.left_pressed:
            self.center_x -= SCREEN_CELL_SIZE
        elif self.right_pressed:
            self.center_x += SCREEN_CELL_SIZE
        elif self.up_pressed:
            self.center_y += SCREEN_CELL_SIZE
        elif self.down_pressed:
            self.center_y -= SCREEN_CELL_SIZE

        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT

class SnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.waiter = 0
        self.snake_sound = arcade.load_sound("Snake.m4a")
        self.coin_sound = arcade.load_sound("Coin.m4a")

    def setup(self):
        self.player = Snake(SCREEN_CELL_SIZE, SCREEN_CELL_SIZE, SCREEN_CELL_SIZE-1, arcade.color.RED)
        self.coin = Coin(4, arcade.color.GOLD)
        self.coin.move()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT and not self.player.right_pressed:
            self.player.left_pressed = True
            self.player.right_pressed = False
            self.player.up_pressed = False
            self.player.down_pressed = False
        elif key == arcade.key.RIGHT and not self.player.left_pressed:
            self.player.left_pressed = False
            self.player.right_pressed = True
            self.player.up_pressed = False
            self.player.down_pressed = False
        elif key == arcade.key.UP and not self.player.down_pressed:
            self.player.left_pressed = False
            self.player.right_pressed = False
            self.player.up_pressed = True
            self.player.down_pressed = False
        elif key == arcade.key.DOWN and not self.player.up_pressed:
            self.player.left_pressed = False
            self.player.right_pressed = False
            self.player.up_pressed = False
            self.player.down_pressed = True

    # def on_key_release(self, key, modifiers):
    #     if key == arcade.key.LEFT:
    #         self.player.left_pressed = False
    #     elif key == arcade.key.RIGHT:
    #         self.player.right_pressed = False
    #     elif key == arcade.key.UP:
    #         self.player.up_pressed = False
    #     elif key == arcade.key.DOWN:
    #         self.player.down_pressed = False

    def on_update(self, delta_time: float):
        self.waiter += delta_time
        if self.waiter < WAITING_TIME:
            return
        self.waiter = 0
        self.player.update()
        arcade.play_sound(self.snake_sound)
        if arcade.check_for_collision(self.player, self.coin):
            arcade.play_sound(self.coin_sound)
            self.coin.move()

def main():
    game = SnakeGame()
    game.setup()
    # arcade.schedule(game.on_update, 5)
    arcade.run()

if __name__ == "__main__":
    main()
