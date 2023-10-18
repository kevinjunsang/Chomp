import pygame
import sys

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SAND_HEIGHT = 20
TILE_SIZE = 64  # tiles are squares height == width

# COLORS
WATER_COLOR = (114, 159, 232)
SAND_COLOR = (100, 25, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CHOMP!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR,
                 (0, SCREEN_HEIGHT - SAND_HEIGHT,
                  SCREEN_WIDTH, SAND_HEIGHT))
fish = pygame.image.load("assets/images/fishTile_081.png").convert()
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(fish,
            (SCREEN_WIDTH / 2 - TILE_SIZE / 2,
             SCREEN_HEIGHT / 2 - TILE_SIZE / 2))
# can designate by just identifying the top left corner
# pygame.draw.rect(screen, (0, 255, 0), (200, 200, 50, 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            print("Thanks for playing")
            sys.exit()

        pygame.display.flip()
