import arcade
import random
import math

# Размеры виртуального экрана
VIRTUAL_SCREEN_WIDTH = 320
VIRTUAL_SCREEN_HEIGHT = 200

# Размеры реального экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Paratrooper Clone"

BULLET_SPEED = 5
HELICOPTER_SPEED = 2
HELICOPTER_SPAWN_INTERVAL = 2.0  # Интервал спавна в секундах
EXPLOSION_TEXTURES = ["explosion1.png", "explosion2.png", "explosion3.png", "explosion4.png"]

class Bullet(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.angle = 0

    def update(self):
        rad_angle = math.radians(self.angle)
        self.center_x += BULLET_SPEED * math.cos(rad_angle)
        self.center_y += BULLET_SPEED * math.sin(rad_angle)
        if self.center_x < 0 or self.center_x > VIRTUAL_SCREEN_WIDTH or self.center_y < 0 or self.center_y > VIRTUAL_SCREEN_HEIGHT:
            self.remove_from_sprite_lists()

class Helicopter(arcade.Sprite):
    def __init__(self, image, scale, sound):
        super().__init__(image, scale)
        self.sound = sound
        self.sound_player = self.sound.play(loop=True)

    def update(self):
        self.center_x += HELICOPTER_SPEED
        if self.center_x > VIRTUAL_SCREEN_WIDTH:
            self.sound.stop(self.sound_player)
            self.remove_from_sprite_lists()

    def destroy(self, explosion_sound):
        self.sound.stop(self.sound_player)
        explosion = Explosion(self.center_x, self.center_y, explosion_sound)
        self.remove_from_sprite_lists()
        return explosion

class Explosion(arcade.Sprite):
    def __init__(self, center_x, center_y, explosion_sound):
        super().__init__()
        self.textures = [arcade.load_texture(texture) for texture in EXPLOSION_TEXTURES]
        self.current_texture = 0
        self.texture = self.textures[self.current_texture]
        self.center_x = center_x
        self.center_y = center_y
        self.explosion_sound = explosion_sound
        arcade.play_sound(self.explosion_sound)

    def update(self):
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.texture = self.textures[self.current_texture]
        else:
            self.remove_from_sprite_lists()

class ParatrooperGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = None
        self.bullet_list = None
        self.helicopter_list = None
        self.explosion_list = None
        self.time_since_last_spawn = 0
        self.left_pressed = False
        self.right_pressed = False
        self.shoot_sound = arcade.load_sound("FX292.mp3")  # Замените "FX292.mp3" на ваш путь к звуку выстрела
        self.helicopter_sound = arcade.load_sound("heli.ogg.mp3")  # Замените "heli.ogg.mp3" на ваш путь к звуку вертолета
        self.explosion_sound = arcade.load_sound("explosion.mp3")  # Замените "explosion.mp3" на ваш путь к звуку взрыва

    def setup(self):
        self.player = arcade.SpriteCircle(5, arcade.color.AZURE)  # Размер уменьшен для соответствия виртуальному экрану
        self.player.center_x = VIRTUAL_SCREEN_WIDTH // 2
        self.player.center_y = 10
        self.bullet_list = arcade.SpriteList()
        self.helicopter_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        # Масштабируем сцену
        arcade.set_viewport(0, VIRTUAL_SCREEN_WIDTH, 0, VIRTUAL_SCREEN_HEIGHT)

        self.player.draw()
        self.bullet_list.draw()
        self.helicopter_list.draw()
        self.explosion_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            self.shoot_bullet()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def shoot_bullet(self):
        bullet = Bullet("bullet_image.png", 0.5)  # Замените "bullet_image.png" на ваш путь к изображению пули
        bullet.angle = self.player.angle
        rad_angle = math.radians(bullet.angle)
        bullet.center_x = self.player.center_x + 10 * math.cos(rad_angle)
        bullet.center_y = self.player.center_y + 10 * math.sin(rad_angle)
        self.bullet_list.append(bullet)
        arcade.play_sound(self.shoot_sound)

    def spawn_helicopter(self):
        helicopter = Helicopter("helicopter_image.png", 0.5, self.helicopter_sound)  # Замените "helicopter_image.png" на ваш путь к изображению вертолета
        helicopter.center_x = 0
        helicopter.center_y = random.randint(VIRTUAL_SCREEN_HEIGHT - 50, VIRTUAL_SCREEN_HEIGHT - 25)
        self.helicopter_list.append(helicopter)

    def on_update(self, delta_time):
        self.bullet_list.update()
        self.helicopter_list.update()
        self.explosion_list.update()

        self.time_since_last_spawn += delta_time
        if self.time_since_last_spawn > HELICOPTER_SPAWN_INTERVAL:
            self.spawn_helicopter()
            self.time_since_last_spawn = 0

        if self.left_pressed:
            self.player.angle += 5
        if self.right_pressed:
            self.player.angle -= 5

        # Проверка столкновений пуль и вертолетов
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.helicopter_list)
            for helicopter in hit_list:
                explosion = helicopter.destroy(self.explosion_sound)
                self.explosion_list.append(explosion)
                bullet.remove_from_sprite_lists()

def main():
    game = ParatrooperGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
