import pygame
import random
from player import Player
from invader import Invader
import settings as st

screen = st.SCREEN
clock = st.CLOCK
FPS = st.FPS


class Star:
    def __init__(self, x_position, y_position):
        self.colour = 'WHITE'
        self.radius = 1
        self.x = x
        self.y = y

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


class Manager:
    pass


run = True
while run:
    clock.tick(FPS)
    screen.fill('BLACK')

    for star in stars:
        star.draw()
        star.fall()
        star.check_if_i_should_reappear_on_top()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
