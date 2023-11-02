import pygame
import random

from stars import stars
from player import Player
from invader import InvadersGroup
import settings as st

screen = st.SCREEN
clock = st.CLOCK
FPS = st.FPS


def drow_stars():
    screen.fill('BLACK')
    for star in stars:
        star.draw()
        star.fall()
        star.check_if_i_should_reappear_on_top()


class Manager:
    def __init__(self):
        self.invaders_object = InvadersGroup()
        self.player = Player(st.SPACESHIP_image, 2, st.SPACESHIP_POS)
        self.player_bullets = pygame.sprite.Group()
        self.invaders_bullets = pygame.sprite.Group()

    def check_collisions(self):
        v = pygame.sprite.groupcollide(self.player_bullets, self.invaders_object.invaders_group, True, True)
        if v:
            print(v.items())
        pygame.sprite.groupcollide(self.player_bullets, self.invaders_bullets, True, True)

    def main_lop(self):
        run = True
        while run:
            clock.tick(FPS)
            drow_stars()

            self.check_collisions()
            self.invaders_object.change_floor_and_direction()

            self.invaders_bullets.update()
            self.player_bullets.update()
            self.invaders_object.invaders_group.update()
            self.player.update()

            self.invaders_object.invaders_group.draw(screen)
            self.player_bullets.draw(screen)
            self.invaders_bullets.draw(screen)

            shoot = self.invaders_object.invaders_shoots()
            if shoot:
                self.invaders_bullets.add(shoot)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move('left')
            if keys[pygame.K_RIGHT]:
                self.player.move('right')

            screen.blit(self.player.image, self.player.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if len(self.player_bullets) < 3:
                        shoot = self.player.shoot()
                        self.player_bullets.add(shoot)

            pygame.display.flip()

        pygame.quit()


l = Manager()
l.main_lop()
