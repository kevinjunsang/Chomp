import pygame
import sys
import time

TILE_SIZE = 64  # tiles are squares height == width
SCREEN_WIDTH = 8 * TILE_SIZE
SCREEN_HEIGHT = 8 * TILE_SIZE
SAND_HEIGHT = 20

# COLORS
WATER_COLOR = (114, 159, 232)
SAND_COLOR = (100, 25, 0)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CHOMP!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR,
                 (0, SCREEN_HEIGHT - SAND_HEIGHT,
                  SCREEN_WIDTH, SAND_HEIGHT))
fish = pygame.image.load("assets/images/fishTile_081.png").convert()
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
fish.set_colorkey(BLACK)
sand_top.set_colorkey(BLACK)
# blit sand tiles across the bottom of the screen
for i in range(SCREEN_WIDTH // TILE_SIZE):
    screen.blit(sand,
                (TILE_SIZE * i,
                 SCREEN_HEIGHT - TILE_SIZE))
    screen.blit(sand_top,
                (TILE_SIZE * i,
                 SCREEN_HEIGHT - 2 * TILE_SIZE))
pygame.display.flip()
# move fish across screen
# for i in range(SCREEN_WIDTH):
#    screen.blit(fish,(i,SCREEN_HEIGHT // 2 - TILE_SIZE // 2))
# time.sleep(0.01)
# pygame.display.flip()
# screen.blit(fish,(SCREEN_WIDTH // 2 - TILE_SIZE // 2,SCREEN_HEIGHT // 2 - TILE_SIZE // 2))
# can designate by just identifying the top left corner
# pygame.draw.rect(screen, (0, 255, 0), (200, 200, 50, 50))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            print("Thanks for playing")
            sys.exit()

        pygame.display.flip()
