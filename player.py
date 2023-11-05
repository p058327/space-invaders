from entity import Entity
import settings as st
from bullet import Bullet


class Player(Entity):
    def __init__(self, img, health, position):
        super().__init__(img, health, position)

    def move(self, keys):
        if keys == 'left':
            self.position.x -= max(1, st.SCREEN_WIDTH // 500 * st.SPACESHIP_SPEED)
        if keys == 'right':
            self.position.x += max(1, st.SCREEN_WIDTH // 500 * st.SPACESHIP_SPEED)
        self.rect.center = self.position
        self.rect.clamp_ip(st.SCREEN_RECT)

    def shoot(self):
        return Bullet(st.SHIP_BULLET_IMAGE, 1, self.rect.center, -1)
