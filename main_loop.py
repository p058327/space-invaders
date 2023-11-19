import pygame
from manager import Manager, launch_screen

manager = Manager()

run = True
while run:
    launch_screen()

    events = pygame.event.get()
    if manager.play:
        manager.update_screen()
        manager.move_player()
        manager.player_shoots(events)

    if manager.end_stage(events):
        manager = Manager()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
