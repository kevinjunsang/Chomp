import pygame
from settings import *

class Fish(pygame.sprite.Sprite):
    def __init__(self, name, x=200, y=200):
        self.right_image = pygame.image.load(f"assets/images/{name}.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        self.x = x
        self.y = y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_left:
            self.image = self.left_image
            if self.x > 0:
                self.x -= 2
        elif self.moving_right:
            self.image = self.right_image
            if self.x < SCREEN_WIDTH - TILE_SIZE:
                self.x += 2
        if self.moving_up:
            if self.y > 0:
                self.y -= 2
        elif self.moving_down:
            if self.y < SCREEN_HEIGHT - 3 * TILE_SIZE:
                self.y += 2


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
