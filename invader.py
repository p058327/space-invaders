import pygame

from entity import Entity
import settings as st
from bullet import Bullet


class Invader(Entity):
    def __init__(self, img, health, position, score, movement='straight'):
        super().__init__(img, health, position)
        self.score = score
        self.direction = 1
        self.down = 0
        self.movement = movement

    def update(self):
        if self.movement == 'straight':
            if self.direction:
                self.rect.move_ip(st.SCREEN_WIDTH // 700 * self.direction * st.INVADER_SPEED,
                                  self.down * st.SCREEN_HEIGHT // 50)
            self.rect.clamp_ip(st.SCREEN_RECT)
        if self.movement == 'parabola':
            self.position.rotate_ip(self.direction * st.INVADER_SPEED)
            self.rect.center = self.position

    def shoot(self):
        return Bullet(st.INVADERS_BULLET_IMAGE, 1, self.rect.center, 1)

    def color(self):
        color = {0: 'black', 1: 'red', 2: 'yellow', 3: 'white'}
        self.image.fill(color[self.life], special_flags=pygame.BLEND_RGB_MIN)


def get_invaders_groups(game_stage):
    list_invaders_groups = []
    invaders_group = pygame.sprite.Group()
    for i in range(1, 5):
        for j in range(1, 9):
            invader = Invader(st.INVADER_IMAGE(), 2,
                              pygame.math.Vector2(st.SCREEN_WIDTH // 15 * j, st.SCREEN_HEIGHT // 15 * i), 10)
            invader.color()
            invaders_group.add(invader)
    list_invaders_groups.append(invaders_group)
    if game_stage > 1:
        invaders_group = pygame.sprite.Group()
        for i in range(1, 8):
            invader = Invader(st.INVADER_IMAGE(), 3, pygame.math.Vector2(st.SCREEN_WIDTH // 10 * i, st.SCREEN_HEIGHT // 3), 10, 'parabola')
            invader.color()
            invaders_group.add(invader)
        list_invaders_groups.append(invaders_group)
    return list_invaders_groups
