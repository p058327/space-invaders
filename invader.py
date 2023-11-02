from entity import Entity
import settings as st
from bullet import Bullet


class Invader(Entity):
    def __init__(self, img, health, position):
        super().__init__(img, health, position)
        self.direction = 1

    def update(self):
        if self.rect.right >= st.SCREEN_WIDTH:
            self.rect.move_ip(0, st.SCREEN_HEIGHT // 200 * st.INVADER_SPEED)
        self.determine_direction()
        if self.direction:
            self.rect.move_ip(self.direction * st.SCREEN_WIDTH // 200 * st.INVADER_SPEED, 0)
        self.rect.clamp_ip(st.SCREEN_RECT)

    def determine_direction(self):
        if self.rect.right >= st.SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1

    def shoot(self):
        return Bullet(st.BULLET_image, 1, self.rect.center, 1)
