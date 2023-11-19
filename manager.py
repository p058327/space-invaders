import pygame
import random

from stars import stars
from entity import Player, Invader
import settings as st


clock = pygame.time.Clock()


def drow_stars(screen):
    screen.fill('BLACK')
    for star in stars:
        star.draw()
        star.fall()
        star.check_if_i_should_reappear_on_top()


def launch_screen():
    pygame.init()
    clock.tick(st.FPS)
    drow_stars(st.SCREEN)


class Manager:
    def __init__(self):
        self.screen = st.SCREEN
        self.game_stage = 1
        self.invaders_groups = self.get_invaders_groups()
        self.player = Player(st.SPACESHIP_IMAGE, 3, st.SPACESHIP_POS)
        self.player_bullets = pygame.sprite.Group()
        self.invaders_bullets = pygame.sprite.Group()
        self.score = 0
        self.play = True

    def get_invaders_groups(self):
        all_invaders_groups = []
        invaders_group = pygame.sprite.Group()
        for i in range(1, 2 + self.game_stage):
            for j in range(1, 9):
                invader = Invader(st.INVADER_IMAGE(), 2,
                                  pygame.math.Vector2(st.SCREEN_WIDTH // 15 * j, st.SCREEN_HEIGHT // 15 * i), 'horizontal')
                invader.color()
                invaders_group.add(invader)
        all_invaders_groups.append(invaders_group)
        if self.game_stage > 1:
            invaders_group = pygame.sprite.Group()
            num_invaders = 2 + self.game_stage
            for i in range(1, num_invaders):
                invader = Invader(st.INVADER_IMAGE(), 3,
                                  pygame.math.Vector2(st.SCREEN_WIDTH // num_invaders * i, st.SCREEN_HEIGHT // 2), 'circle')
                invader.color()
                invaders_group.add(invader)
            all_invaders_groups.append(invaders_group)
        return all_invaders_groups

    def update_screen(self):
        self.check_collisions()
        self.del_dead()
        self.change_floor_and_direction_of_invaders()
        self.data_display()

        self.invaders_bullets.update()
        self.player_bullets.update()
        self.player.update()
        for group in self.invaders_groups:
            group.update()

        self.player_bullets.draw(self.screen)
        self.invaders_bullets.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        for group in self.invaders_groups:
            group.draw(self.screen)

        shot = self.invaders_shoots()
        if shot:
            self.invaders_bullets.add(shot)

    def check_collisions(self):
        collide = pygame.sprite.spritecollide(self.player, self.invaders_bullets, False)
        if collide:
            self.player.life -= 1
            self.score -= min(st.REDUCTION_SCORE, self.score)
            for i in collide:
                i.life -= 1
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
            self.score += st.SCORE // 3
            for invader in collide[i]:
                invader.life -= 1

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

    def change_floor_and_direction_of_invaders(self):
        for group in self.invaders_groups:
            making_descent = 0
            change_direction = 1
            for invader in group:
                if invader.rect.right >= st.SCREEN_WIDTH or invader.rect.left <= 0:
                    making_descent = 1
                    change_direction = -1
                    break
            for invader in group:
                if invader.movement == 'horizontal':
                    invader.rect.move_ip(0, making_descent * st.SCREEN_HEIGHT // 20)
                    invader.direction = invader.direction * change_direction

    def invaders_shoots(self):
        for group in self.invaders_groups:
            if group:
                if random.random() > 0.99:
                    shooting_invader = random.choice(group.sprites())
                    return shooting_invader.shoot()

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move('left')
        if keys[pygame.K_RIGHT]:
            self.player.move('right')

    def player_shoots(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if len(self.player_bullets) < 10 // self.game_stage:
                    shoot = self.player.shoot()
                    self.player_bullets.add(shoot)

    def end_stage(self, events):
        invaders_exist = False
        for group in self.invaders_groups:
            if group:
                invaders_exist = True
                break
        if self.player.life < 1 or self.check_enemies_height():
            self.play = False
            self.game_over()
            continued = self.continued(events)
            if continued:
                return True
        if not invaders_exist:
            self.play = False
            self.stage_victory()
            continued = self.continued(events)
            if self.game_stage < st.GAME_STAGES:
                self.next_label(continued)
            else:
                if continued:
                    return True
        return False

    def check_enemies_height(self):
        for group in self.invaders_groups:
            for invader in group:
                if invader.rect.bottom >= self.player.rect.top:
                    return True
                return False

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

    def data_display(self):
        color = 'purple'
        score_font = pygame.font.Font('freesansbold.ttf', 30)
        score_text = score_font.render('score : ' + f'{self.score}', True, color)
        score_rect = score_text.get_rect()
        score_position = pygame.Vector2(st.SCREEN_WIDTH - score_rect.width, st.SCREEN_HEIGHT - 40)
        self.screen.blit(score_text, score_position)
        if self.player.life == 1:
            color = 'red'
        life_font = pygame.font.Font('freesansbold.ttf', 30)
        life_text = life_font.render('life : ' + f'{self.player.life}', True, color)
        life_position = pygame.Vector2(20, st.SCREEN_HEIGHT - 40)
        self.screen.blit(life_text, life_position)

    def continued(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True
        return False

    def next_label(self, continued):
        if continued:
            self.game_stage += 1
            self.invaders_groups = self.get_invaders_groups()
            self.player = Player(st.SPACESHIP_IMAGE, 3 + (self.game_stage // 2), st.SPACESHIP_POS)
            self.player_bullets = pygame.sprite.Group()
            self.invaders_bullets = pygame.sprite.Group()
            self.play = True

    def stage_victory(self):
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render('Great victory ! ! !', True, 'blue')
        text_rect = text.get_rect()
        text_rect.center = (st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 2)
        self.screen.blit(text, text_rect)
        score_font = pygame.font.Font('freesansbold.ttf', 80)
        score_text = score_font.render(f'score: {self.score}', True, 'blue')
        score_position = pygame.Vector2(st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 4)
        self.screen.blit(score_text, score_position)
        if self.game_stage < st.GAME_STAGES:
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render('Press Enter to continue', True, 'cyan')
            text_rect = text.get_rect()
            text_rect.center = (st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 8)
            self.screen.blit(text, text_rect)
        else:
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render('Press Enter for a replay', True, 'cyan')
            text_rect = text.get_rect()
            text_rect.center = (st.SCREEN_WIDTH // 2, st.SCREEN_HEIGHT // 8)
            self.screen.blit(text, text_rect)
