import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, img, health, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.life = health
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = position

    def health(self):
        self.life -= 1
