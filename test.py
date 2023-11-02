import pygame
import random

pygame.init()

WIDTH = 480
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

screen = pygame.display
screen.set_caption("Starry Night")
screen = screen.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)

yspeed = 5


class Star(object):
    def __init__(self, x, y, yspeed):
        self.colour = WHITE
        self.radius = 1
        self.x = x
        self.y = y
        self.yspeed = yspeed

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

    def fall(self):
        self.y += self.yspeed

    def check_if_i_should_reappear_on_top(self):
        if self.y >= HEIGHT:
            self.y = 0


stars = []

for i in range(100):
    x = random.randint(1, WIDTH - 1)
    y = random.randint(1, HEIGHT - 1)
    stars.append(Star(x, y, yspeed))

GameOn = True

while GameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOn = False

    screen.fill(BLACK)

    for star in stars:
        star.draw()
        star.fall()
        star.check_if_i_should_reappear_on_top()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
