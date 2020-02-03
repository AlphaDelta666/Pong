import pygame
from pygame.locals import *

class Joueur(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.pressed = {}
        self.score = 0

    def move_up(self):
        self.rect.y -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity

    def add_score(self):
        self.score += 1
