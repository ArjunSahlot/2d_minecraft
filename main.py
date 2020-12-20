import pygame
from constants import *
from world import World


# Window Management
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Minecraft")


def main(window):
    pygame.init()
    clock = pygame.time.Clock()
    world = World()

    while True:
        clock.tick(FPS)
        window.fill(BLACK)
        events = pygame.event.get()
        world.update(window, events)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.display.update()


main(WINDOW)
