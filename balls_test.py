from balls import Balls
import pygame

SCREEN_WIDTH = 780
SCREEN_HEIGHT = 780
IMG = pygame.image.load('dwsample-bmp-1920.bmp')
SIZE = SCREEN_WIDTH // 200, SCREEN_HEIGHT // 15
POS = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10 * 9)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
b = Balls(IMG, 2, SIZE, POS)

run = True
while run:
    clock.tick(FPS)

    screen.fill("cyan")

    b.update(-1)

    screen.blit(b.image, b.position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()

