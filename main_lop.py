import pygame

from space_invaders_game import Manager, drow_stars, continued
import settings as st

screen = st.SCREEN
clock = st.CLOCK
FPS = st.FPS

number_stages = 2
manger = Manager(1)
run = True
while run:
    pygame.font.init()
    clock.tick(FPS)
    drow_stars(st.SCREEN)
    events = pygame.event.get()

    if manger.game_mode():
        if manger.winner_game():
            if manger.game_stage == number_stages:
                manger.stage_victory(None)
            else:
                manger.stage_victory()
            waiting = continued(events)
            if waiting:
                manger = Manager(2, manger.score)
        else:
            manger.game_over()
            waiting = continued(events)
            if waiting:
                manger = Manager(1)
    else:

        manger.update_screen()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            manger.player.move('left')
        if keys[pygame.K_RIGHT]:
            manger.player.move('right')

        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if len(manger.player_bullets) < 3:
                    shoot = manger.player.shoot()
                    manger.player_bullets.add(shoot)

    for event in events:
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
