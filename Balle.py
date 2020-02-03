import pygame

class Balle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ressource/ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 250
        self.dirx = 1
        self.diry = 1
        self.velocity = 5



    def move(self):
        self.rect.x += self.dirx * self.velocity
        self.rect.y += self.diry * self.velocity
