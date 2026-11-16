
import pygame 
from settings import *
from sprites import carregar_sprite, desenhar_sprite

class Player:
    def __init__(self,x,y, personagem="lionel"):
        self.rect = pygame.Rect(x,y,70,70)
        self.vel_y = 0
        self.pulo_pressionado = False
        self.on_ground = False
        self.image = carregar_sprite(f"sprites/{personagem}.png", (70, 70))

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
        if keys[pygame.K_w]:
            if self.on_ground and not self.pulo_pressionado:
                self.vel_y = PLAYER_JUMP
                self.on_ground = False
            self.pulo_pressionado = True
        else:
            self.pulo_pressionado = False

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.y >= 415:
            self.rect.y = 415
            self.vel_y = 0
            self.on_ground = True

        if self.rect.y <= 0:
            self.rect.y = 0
            self.vel_y = 0

    def desenhar(self,screen):
        desenhar_sprite(screen, self.image, self.rect)
