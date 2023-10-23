import pygame
from settings import *
import math

class Minnow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.right_image = pygame.image.load("assets/images/minnow.png").convert()
        self.right_image.set_colorkey(BLACK)
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        # creating a rectangle that defines where to paint the fish
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = True
        self.moving_right = False
        self.moving_up = False
        self.moving_down = True
        self.life = True

    def update(self):
        if self.moving_left:
            self.image = self.left_image
            self.rect.x -= 2
        elif self.moving_right:
            self.image = self.right_image
            self.rect.x += 2
        if self.moving_up:
            self.rect.y -= 2
        elif self.moving_down:
            self.rect.y += 2
        if self.rect.left < 0:
            self.rect.left = 0
            self.moving_left = False
            self.moving_right = True
        if self.rect.top < 0:
            self.rect.top = 0
            self.moving_up = False
            self.moving_down = True
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.moving_right = False
            self.moving_left = True
        if self.rect.bottom > WATER_BOTTOM:
            self.rect.bottom = WATER_BOTTOM
            self.moving_down = False
            self.moving_up = True

    def dead(self):
        self.image = pygame.image.load("assets/images/fish_bones.png.").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.flip(self.image, False, True)
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.rect.y -= 2
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))