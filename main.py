import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# VARIABLES

BLACK = (255, 255, 255)

# EVENT LOOP


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
