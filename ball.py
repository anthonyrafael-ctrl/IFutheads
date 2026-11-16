
import pygame
from settings import *
from sprites import carregar_sprite

class Bola:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,48,48)
        self.vel_x = 0
        self.vel_y = 0
        self.bola = carregar_sprite("bola.png", (48, 48))

    def apply_gravity(self):
        self.vel_y += GRAVITY

    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.x < 0:
            self.rect.x = 0
            self.vel_x = abs(self.vel_x)

        if self.rect.x > SCREEN_W - self.rect.width:
            self.rect.x = SCREEN_W - self.rect.width
            self.vel_x = -abs(self.vel_x)

        if self.rect.y >= 452:
            self.rect.y = 452
            self.vel_y *= -0.7 

    def desenhar(self,screen):
        screen.blit(self.bola, self.rect)
