import math
import pygame
import settings as st


class Entity(pygame.sprite.Sprite):
    def __init__(self, img, health, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.life = health
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = position


class Bullet(Entity):
    def __init__(self, img, health, position, direction):
        super().__init__(img, health, position)
        self.direction = direction

    def update(self):
        self.rect.move_ip(0, self.direction * st.SCREEN_HEIGHT // 400 * st.BULLET_SPEED)
        # check if sprite has gone of screen
        if self.rect.bottom < 0 or self.rect.top > st.SCREEN_HEIGHT:
            self.kill()


class Player(Entity):
    def __init__(self, img, health, position):
        super().__init__(img, health, position)

    def move(self, keys):
        if keys == 'left' and self.rect.left > 0:
            self.position.x -= max(1, st.SCREEN_WIDTH // 500 * st.SPACESHIP_SPEED)
        if keys == 'right' and self.rect.right < st.SCREEN_WIDTH:
            self.position.x += max(1, st.SCREEN_WIDTH // 500 * st.SPACESHIP_SPEED)
        self.rect.center = self.position
        self.rect.clamp_ip(st.SCREEN_RECT)

    def shoot(self):
        return Bullet(st.SHIP_BULLET_IMAGE, 1, self.rect.center, -1)


class Invader(Entity):
    def __init__(self, img, health, position, movement):
        super().__init__(img, health, position)
        self.score = st.SCORE * self.life
        self.direction = 1
        self.movement = movement
        self.angle = 0

    def update(self):
        if self.movement == 'horizontal':
            self.rect.move_ip(st.SCREEN_WIDTH // 700 * self.direction * st.INVADER_SPEED, 0)
            self.rect.clamp_ip(st.SCREEN_RECT)
        if self.movement == 'circle':
            self.rect.move_ip(int(math.cos(self.angle) * 8), int(math.sin(self.angle) * 8))
            self.angle -= 0.01 * st.INVADER_SPEED

    def shoot(self):
        return Bullet(st.INVADERS_BULLET_IMAGE, 1, self.rect.center, 1)

    def color(self):
        color = {0: 'black', 1: 'red', 2: 'yellow', 3: 'white'}
        self.image.fill(color[self.life], special_flags=pygame.BLEND_RGB_MIN)
