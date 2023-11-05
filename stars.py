import settings as st
import pygame
import random

screen = st.SCREEN


class Star:
    def __init__(self, x_position, y_position):
        self.colour = 'WHITE'
        self.radius = 1
        self.x = x_position
        self.y = y_position

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

    def fall(self):
        self.y += st.SCREEN_HEIGHT // 100

    def check_if_i_should_reappear_on_top(self):
        if self.y >= st.SCREEN_HEIGHT:
            self.y = 0


stars = []
for i in range(200):
    x = random.randint(1, st.SCREEN_WIDTH - 1)
    y = random.randint(1, st.SCREEN_HEIGHT - 1)
    stars.append(Star(x, y))
