import pygame
import random

from player import Player
from invader import Invader
import settings as st


IMG = st.SPACESHIP_image
screen = st.SCREEN
SPACESHIP_POS = st.SPACESHIP_POS
INVADER_POS = 100, 100
clock = st.CLOCK
FPS = st.FPS
b = Player(IMG, 2, SPACESHIP_POS)
f = pygame.sprite.Group()
r = Invader(st.INVADER_image, 1, INVADER_POS)
g = pygame.sprite.Group(r)
o = pygame.sprite.Group()


run = True
while run:
    clock.tick(FPS)

    screen.fill("cyan")

    f.update()
    f.draw(screen)

    g.update()
    g.draw(screen)

    # d = random.random()
    # if d > 0.95:
    #     d = random.choice(g)
    #     n = b.shoot()
    #     o.add(n)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        b.move('left')
    if keys[pygame.K_RIGHT]:
        b.move('right')

    screen.blit(b.image, b.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(f) < 3:
                v = b.shoot()
                f.add(v)

    pygame.display.flip()

pygame.quit()
