import pygame 
from settings import *

#classe player, tem que rever como vai colocar os dois personagens e escolher só um. Tem que adicionar colisão
class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,70,70)
        self.vel_y = 0
        self.on_ground = False
        self.image = pygame.image.load("asserts/imagens/lionel_rollim.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect(topleft=(x,y))
    
    def mover(self,keys):
        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED

        if self.rect.x < 0:
            self.rect.x = 0
        
        if self.rect.x > SCREEN_W - self.rect.width:
            self.rect.x = SCREEN_W - self.rect.width

    def pular(self,keys):
        if keys[pygame.K_w] and self.on_ground:
            self.vel_y = PLAYER_JUMP

        if self.rect.y > 600:
            self.rect.y = 600

        
    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.y >= SCREEN_H - 70:
            self.rect.y = SCREEN_H - 70
            self.on_ground = True
        
        if self.rect.y <= 0:
            self.rect.y = 0
            self.vel_y = 0

        

    def desenhar(self,screen):
        screen.blit(self.image, self.rect)

