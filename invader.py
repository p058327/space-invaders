import random
import pygame

from entity import Entity
import settings as st
from bullet import Bullet


class Invader(Entity):
    def __init__(self, img, health, position):
        super().__init__(img, health, position)
        self.direction = 1
        self.down = 0

    def update(self):
        if self.direction:
            self.rect.move_ip(self.direction * st.SCREEN_WIDTH // 500 * st.INVADER_SPEED, self.down * st.SCREEN_HEIGHT // 50)
        self.rect.clamp_ip(st.SCREEN_RECT)

    def shoot(self):
        return Bullet(st.BULLET_image, 1, self.rect.center, 1)


class InvadersGroup:
    def __init__(self):
        self.invaders_group = pygame.sprite.Group()
        for i in range(1, 5):
            for j in range(1, 9):
                invader = Invader(st.INVADER_image, 1, (st.SCREEN_WIDTH // 20 * j, st.SCREEN_HEIGHT // 20 * i))
                self.invaders_group.add(invader)
        print(self.invaders_group)

    def change_floor_and_direction(self):
        making_descent = 0
        change_direction = 1
        for invader in self.invaders_group:
            if invader.rect.right >= st.SCREEN_WIDTH or invader.rect.left <= 0:
                if invader.rect.right >= st.SCREEN_WIDTH:
                    making_descent = 1
                change_direction = -1
        for invader in self.invaders_group:
            invader.down = making_descent
            invader.direction = invader.direction * change_direction

    def invaders_shoots(self):
        if random.random() > 0.99:
            shooting_invader = random.choice(self.invaders_group.sprites())
            return shooting_invader.shoot()
