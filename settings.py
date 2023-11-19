import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GAME_STAGES = 3

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_RECT = SCREEN.get_rect()

SHIP = pygame.image.load('images/player.png').convert_alpha()
INVADERS = pygame.image.load('images/alien.bmp').convert_alpha()
SHIP_BULLET = pygame.image.load('images/bullet.png').convert_alpha()
INVADERS_BULLET = pygame.image.load('images/red.png').convert_alpha()

SHIP_SIZE = SCREEN_WIDTH // 25, SCREEN_HEIGHT // 15
INVADERS_SIZE = SCREEN_WIDTH // 20, SCREEN_HEIGHT // 20
SHIP_BULLET_SIZE = SCREEN_WIDTH // 80, SCREEN_HEIGHT // 30
INVADERS_BULLET_SIZE = SCREEN_WIDTH // 40, SCREEN_HEIGHT // 40

SPACESHIP_IMAGE = pygame.transform.scale(SHIP, SHIP_SIZE)
INVADER_IMAGE = lambda: pygame.transform.scale(INVADERS, INVADERS_SIZE)
SHIP_BULLET_IMAGE = pygame.transform.scale(SHIP_BULLET, SHIP_BULLET_SIZE)
INVADERS_BULLET_IMAGE = pygame.transform.scale(INVADERS_BULLET, INVADERS_BULLET_SIZE)

SPACESHIP_SPEED = 3
INVADER_SPEED = 3
BULLET_SPEED = 3

SCORE = 10
REDUCTION_SCORE = 50

SPACESHIP_POS = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.9)

CLOCK = pygame.time.Clock()
FPS = 60
