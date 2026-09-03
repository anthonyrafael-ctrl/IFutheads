import pygame
from settings import *

#classe bola, com as posições, e dimensões(30,30). Gravidade já aplicada, ta faltando a colisão.
class Bola:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,48,48)
        self.vel_x = 0
        self.vel_y = 0
        self.bola = pygame.image.load("asserts/imagens/bola.png").convert_alpha()
        self.bola = pygame.transform.scale(self.bola, (48, 48))

    def apply_gravity(self):
        self.vel_y += GRAVITY

    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.x < 0:
            self.rect.x = 0
        
        if self.rect.x > SCREEN_W - self.rect.width:
            self.rect.x = SCREEN_W - self.rect.width

        if self.rect.y >= SCREEN_H - 30:
            self.rect.y = SCREEN_H -30
            self.vel_y *= -0.7 

    def desenhar(self,screen):
        screen.blit(self.bola, self.rect)


    