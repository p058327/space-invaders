import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_RECT = SCREEN.get_rect()

SHIP = pygame.image.load('images/ship.bmp')
INVADERS = pygame.image.load('images/alien.bmp').convert_alpha()
BULLET = pygame.image.load('images/bullet.png').convert_alpha()

SHIP_SIZE = SCREEN_WIDTH // 30, SCREEN_HEIGHT // 15
INVADERS_SIZE = SCREEN_WIDTH // 15, SCREEN_HEIGHT // 15
BULLET_SIZE = SCREEN_WIDTH // 60, SCREEN_HEIGHT // 30

SPACESHIP_image = pygame.transform.scale(SHIP, SHIP_SIZE)
INVADER_image = pygame.transform.scale(INVADERS, INVADERS_SIZE)
BULLET_image = pygame.transform.scale(BULLET, BULLET_SIZE)

SPACESHIP_SPEED = 1
INVADER_SPEED = 1
BULLET_SPEED = 1

SPACESHIP_POS = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.9)

CLOCK = pygame.time.Clock()
FPS = 60

# d = "Bullet"
# print(d.upper())
