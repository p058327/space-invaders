import pygame
from space_invaders_game import Manager, launch_screen
import settings as st

manger = Manager()

run = True
while run:
    launch_screen()

    events = pygame.event.get()
    if manger.play:
        manger.update_screen()
        manger.move_player()
        manger.player_shoots(events)

    if manger.end_stage(events):
        manger = Manager()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
