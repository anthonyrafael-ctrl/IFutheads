import pygame
from settings import *

#classe da ia. Tem que rever as movimentações e adicionar colisão.
class Enemy:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,70,70)
        self.vel_y = 0

    def seguir_bola(self,ball):
        if ball.rect.centerx < SCREEN_W // 2:

            if self.rect.centerx < 800:
                self.rect.x += PLAYER_SPEED

            elif self.rect.centerx > 800:
                self.rect.x -= PLAYER_SPEED

        else:

            if ball.rect.centerx < self.rect.centerx:
                self.rect.x -= PLAYER_SPEED

            elif ball.rect.centerx < self.rect.centerx:
                self.rect.x += PLAYER_SPEED

        if self.rect.left < SCREEN_W // 2:
            self.rect.left = SCREEN_W // 2

        if self.rect.right > SCREEN_W:
            self.rect.right = SCREEN_W
    
    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.y >= SCREEN_H - 70:
            self.rect.y = SCREEN_H - 70

    def desenhar(self,screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)