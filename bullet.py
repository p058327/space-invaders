from entity import Entity
from settings import SCREEN_HEIGHT, BULLET_SPEED

print(-1 * SCREEN_HEIGHT // 20000 * BULLET_SPEED)


class Bullet(Entity):
    def __init__(self, img, health, position, direction):
        super().__init__(img, health, position)
        self.direction = direction

    def update(self):
        self.rect.move_ip(0, self.direction * SCREEN_HEIGHT // 400 * BULLET_SPEED)
        # check if sprite has gone of screen
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
