import pygame
from settings import *

#classe bola, com as posições, e dimensões(30,30). Gravidade já aplicada, ta faltando a colisão.
class Bola:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,30,30)
        self.vel_x = 0
        self.vel_y = 0

    def apply_gravity(self):
        self.vel_y += GRAVITY

    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.y >= SCREEN_H - 30:
            self.rect.y = SCREEN_H -30
            self.vel_y *= -0.7 

    def desenhar(self,screen):
        pygame.draw.ellipse(screen, (0,0,0), self.rect)