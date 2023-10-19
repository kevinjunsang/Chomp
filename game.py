import pygame
import sys
import time
import random

TILE_SIZE = 64  # tiles are squares height == width
SCREEN_WIDTH = 8 * TILE_SIZE
SCREEN_HEIGHT = 8 * TILE_SIZE

# COLORS
WATER_COLOR = (114, 159, 232)
SAND_COLOR = (100, 25, 0)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CHOMP!")
screen.fill(WATER_COLOR)

nemo_fish = pygame.image.load("assets/images/nemo_fish.png.png").convert()
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
nemo_fish.set_colorkey(BLACK)
sand_top.set_colorkey(BLACK)
seagrass.set_colorkey(BLACK)
# blit sand tiles across the bottom of the screen
for i in range(SCREEN_WIDTH // TILE_SIZE):
    screen.blit(sand,
                (TILE_SIZE * i,
                 SCREEN_HEIGHT - TILE_SIZE))
    screen.blit(sand_top,
                (TILE_SIZE * i,
                 SCREEN_HEIGHT - 2 * TILE_SIZE))
# blit four different seagrass along the bottom of the seabed
for i in range(4):
    # make sure that the top left corner is in the screen
    x_val = random.randint(0, SCREEN_WIDTH - TILE_SIZE)
    y_val = random.randint(SCREEN_HEIGHT - 2 * TILE_SIZE, SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
    screen.blit(seagrass,
                (x_val,
                y_val))
pygame.display.flip()
# move fish across screen
for i in range(SCREEN_WIDTH):
    screen.blit(nemo_fish,(i,SCREEN_HEIGHT // 2 - TILE_SIZE // 2))
    time.sleep(0.01)
    pygame.display.flip()
    pygame.draw.rect(screen, WATER_COLOR, (i, SCREEN_HEIGHT // 2 - TILE_SIZE // 2,
                                           TILE_SIZE, TILE_SIZE))
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
