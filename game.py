import pygame
import sys
import time
import random
import fish
import minnow
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

my_fish = fish.Fish("nemo_fish", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
my_minnows = []
for i in range(NUM_MINNOWS):
    my_minnows.append(minnow.Minnow(random.randint(0, SCREEN_WIDTH - TILE_SIZE),
                                    random.randint(0, WATER_BOTTOM - TILE_SIZE)))
background = screen.copy()
clock = pygame.time.Clock()
def draw_background():
    for i in range(SCREEN_WIDTH // TILE_SIZE):
        background.blit(sand,
                    (TILE_SIZE * i,
                     SCREEN_HEIGHT - TILE_SIZE))
        background.blit(sand_top,
                    (TILE_SIZE * i,
                     SCREEN_HEIGHT - 2 * TILE_SIZE))
    # blit four different seagrass along the bottom of the seabed
    for i in range(4):
        # make sure that the top left corner is in the screen
        x_val = random.randint(0, SCREEN_WIDTH - TILE_SIZE)
        y_val = random.randint(SCREEN_HEIGHT - 2 * TILE_SIZE, SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
        background.blit(seagrass,
                    (x_val,
                     y_val))
    # draw the CHOMP! title
    text = game_font.render("Chomp!", True, BLACK)
    # background.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
    #                   SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
# screen.blit(fish,(SCREEN_WIDTH // 2 - TILE_SIZE // 2,SCREEN_HEIGHT // 2 - TILE_SIZE // 2))
# can designate by just identifying the top left corner
# pygame.draw.rect(screen, (0, 255, 0), (200, 200, 50, 50))

draw_background()

while True:
    # listen for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Thanks for playing")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = True
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = True
            if event.key == pygame.K_UP:
                my_fish.moving_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = False
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = False
            if event.key == pygame.K_UP:
                my_fish.moving_up = False
        for minnow in my_minnows:
            if minnow.rect.colliderect(my_fish.rect):
                minnow.life = False
    # update game objects

    # draw the game screen
    my_fish.update()
    for minnow in my_minnows:
        if minnow.life:
            minnow.update()
        else:
            minnow.dead()
    screen.blit(background, (0, 0))
    my_fish.draw(screen)
    for minnow in my_minnows:
        minnow.draw(screen)
    pygame.display.flip()
    clock.tick(60)
