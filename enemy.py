import pygame
from settings import *

#classe da ia. Tem que rever as movimentações e adicionar colisão.
class Enemy:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,70,70)
        self.vel_y = 0

    def seguir_bola(self,ball):
        if ball.rect.x < self.rect.x:
            self.rect.x -= PLAYER_SPEED
        elif ball.rect.x > self.rect.x:
            self.rect.x += PLAYER_SPEED

        if self.rect.x < 0:
            self.rect.x = 0
        
        if self.rect.x > SCREEN_W - self.rect.width:
            self.rect.x = SCREEN_W - self.rect.width
    
    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.y >= SCREEN_H - 70:
            self.rect.y = SCREEN_H - 70

    def desenhar(self,screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)