import pygame
import sys
import time
import random

from settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 128)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CHOMP!")
screen.fill(WATER_COLOR)

nemo_fish = pygame.image.load("assets/images/nemo_fish.png").convert()
eal_head = pygame.image.load("assets/images/eal_head.png").convert()
eal_tail = pygame.image.load("assets/images/eal_tail.png").convert()
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
nemo_fish.set_colorkey(BLACK)
eal_head.set_colorkey(BLACK)
eal_tail.set_colorkey(BLACK)
sand_top.set_colorkey(BLACK)
seagrass.set_colorkey(BLACK)
# flip the eal
eal_head = pygame.transform.flip(eal_head, True, False)
eal_tail = pygame.transform.flip(eal_tail, True, False)
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
# draw the CHOMP! title
text = game_font.render("Chomp!", True, BLACK)
screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
                   SCREEN_HEIGHT // 2 - text.get_height() // 2))

pygame.display.flip()
# move fish across screen
for i in range(SCREEN_WIDTH):
    # move the nemo fish across the screen
    screen.blit(nemo_fish, (i,
                            TILE_SIZE * 2))
    # move the eal across the screen
    screen.blit(eal_tail, (SCREEN_WIDTH - TILE_SIZE - i,
                           SCREEN_HEIGHT - 4 * TILE_SIZE))
    screen.blit(eal_head, (SCREEN_WIDTH - 2 * TILE_SIZE - i,
                           SCREEN_HEIGHT - 4 * TILE_SIZE))
    time.sleep(0.01)
    pygame.display.flip()
    # color back the eal and nemo fish areas
    pygame.draw.rect(screen, WATER_COLOR, (i, TILE_SIZE * 2,
                                           TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(screen, WATER_COLOR, (SCREEN_WIDTH - 2 * TILE_SIZE - i, SCREEN_HEIGHT - 4 * TILE_SIZE,
                                           2 * TILE_SIZE, TILE_SIZE))
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
