import pygame

class Fish(pygame.sprite.Sprite):
    def __init__(self, x=200, y=200):
        self.image = pygame.image.load("assets/images/pufferfish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.x = x
        self.y = y

    def move_left(self):
        self.x -= 10
        print("swimming to the left")

    def move_right(self):
        self.x += 10
        print("swimming to the right")

    def move_down(self):
        self.y += 10
        print("swimming down")

    def move_up(self):
        self.y -= 10
        print("swimming up")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
