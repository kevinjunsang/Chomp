import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("CHOMP!")
screen.fill((114, 159, 232))

pygame.draw.rect(screen, (100, 25, 0), (0, 380, 400, 400))
fish = pygame.image.load("assets/images/fishTile_081.png").convert()
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(fish, (200,200,64,64))
pygame.display.flip()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            print("Thanks for playing")
            sys.exit()