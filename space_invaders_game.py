import pygame
import random

from stars import stars
from player import Player
from invader import get_invaders_groups
import settings as st

# screen = st.SCREEN
clock = st.CLOCK
FPS = st.FPS


def drow_stars(screen):
    screen.fill('BLACK')
    for star in stars:
        star.draw()
        star.fall()
        star.check_if_i_should_reappear_on_top()


def continued(events):
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return True
        return False


class Manager:
    def __init__(self, game_stage, score=0, screen=st.SCREEN):
        self.screen = screen
        self.game_stage = game_stage
        self.invaders_groups = get_invaders_groups(game_stage)
        self.player = Player(st.SPACESHIP_IMAGE, 3, st.SPACESHIP_POS)
        self.player_bullets = pygame.sprite.Group()
        self.invaders_bullets = pygame.sprite.Group()
        self.score = score

    def check_collisions(self):
        for group in self.invaders_groups:
            collide = pygame.sprite.groupcollide(self.player_bullets, group, False, False)
            for i in collide:
                i.life -= 1
                for invader in collide[i]:
                    invader.life -= 1
                    invader.color()
        collide = pygame.sprite.groupcollide(self.player_bullets, self.invaders_bullets, False, False)
        for i in collide:
            i.life -= 1
            for invader in collide[i]:
                invader.life -= 1
        collide = pygame.sprite.spritecollide(self.player, self.invaders_bullets, False)
        if collide:
            self.player.life -= 1
            for i in collide:
                i.life -= 1

    def change_floor_and_direction_of_invaders(self):
        for group in self.invaders_groups:
            making_descent = 0
            change_direction = 1
            for invader in group:
                right = invader.rect.right >= st.SCREEN_WIDTH
                if right or invader.rect.left <= 0:
                    making_descent = int(right)
                    change_direction = -1
                    break

            for invader in group:
                invader.down = making_descent
                invader.direction = invader.direction * change_direction

    def invaders_shoots(self):
        for group in self.invaders_groups:
            if group:
                if random.random() > 0.99:
                    shooting_invader = random.choice(group.sprites())
                    return shooting_invader.shoot()

    def del_dead(self):
        for group in self.invaders_groups:
            for invader in group:
                if invader.life == 0:
                    self.score += invader.score
                    invader.kill()
        for bullet in self.invaders_bullets:
            if bullet.life == 0:
                bullet.kill()
        for bullet in self.player_bullets:
            if bullet.life == 0:
                bullet.kill()

    def update_screen(self):
        self.check_collisions()
        self.del_dead()
        self.change_floor_and_direction_of_invaders()

        self.display()

        for group in self.invaders_groups:
            group.update()
        self.invaders_bullets.update()
        self.player_bullets.update()
        self.player.update()

        for group in self.invaders_groups:
            group.draw(self.screen)
        self.player_bullets.draw(self.screen)
        self.invaders_bullets.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)

        shoot = self.invaders_shoots()
        if shoot:
            self.invaders_bullets.add(shoot)

    def game_mode(self):
        invaders_situation = False
        for group in self.invaders_groups:
            if group:
                invaders_situation = True
        if self.player.life < 1 or not invaders_situation or self.check_enemies_height():
            return True
        return False

    def winner_game(self):
        if self.player.life < 1:
            return 0
        return 1

    def game_over(self):
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render('game over', True, 'green')
        text_rect = text.get_rect()
        text_rect.center = (st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 2)
        self.screen.blit(text, text_rect)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render('Press Enter for a replay', True, 'cyan')
        text_rect = text.get_rect()
        text_rect.center = (st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 8)
        self.screen.blit(text, text_rect)

    def check_enemies_height(self):
        for group in self.invaders_groups:
            for invader in group:
                if invader.rect.bottom >= self.player.rect.top:
                    return True
                return False

    def display(self):
        life_font = pygame.font.Font('freesansbold.ttf', 30)
        life_text = life_font.render('life : ' + f'{self.player.life}', True, 'purple')
        life_position = pygame.Vector2(20, st.SCREEN_HEIGHT - 40)
        self.screen.blit(life_text, life_position)
        score_font = pygame.font.Font('freesansbold.ttf', 30)
        score_text = score_font.render('score : ' + f'{self.score}', True, 'purple')
        score_rect = score_text.get_rect()
        score_position = pygame.Vector2(st.SCREEN_WIDTH - score_rect.width, st.SCREEN_HEIGHT - 40)
        self.screen.blit(score_text, score_position)

    def stage_victory(self, next_step=True):
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render('Great victory ! ! !', True, 'blue')
        text_rect = text.get_rect()
        text_rect.center = (st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 2)
        self.screen.blit(text, text_rect)
        score_font = pygame.font.Font('freesansbold.ttf', 80)
        score_text = score_font.render(f'score: {self.score}', True, 'blue')
        score_position = pygame.Vector2(st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 4)
        self.screen.blit(score_text, score_position)
        if next_step:
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render('Press Enter to continue', True, 'cyan')
            text_rect = text.get_rect()
            text_rect.center = (st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 8)
            self.screen.blit(text, text_rect)

    def end_game(self):
        if self.winner_game():
            self.stage_victory()
            waiting = continued(events)
            if waiting:
                manger = Manager(2, self.score)
        else:
            self.game_over()
            waiting = continued(events)
            if waiting:
                manger = Manager(1)
