
import pygame
from settings import *
from sprites import carregar_sprite, desenhar_sprite

#classe da cpu mas quem decide decide o que fazer é a enemyAI (enemy_ai.py) aqui fica so a estrutura do jogador rivalzinho
class Enemy:
    def __init__(self, x, y, nivel=0, personagem="cristiano"):
        config = CPU_NIVEIS[min(nivel, len(CPU_NIVEIS) - 1)]

        self.speed = config["velocidade"]
        self.forca_chute = config["chute"]

        self.rect = pygame.Rect(x, y, 70, 70)
        self.x = float(x)                  # o rect só guarda inteiros o float permite velocidades como 4.5 ou seja numeros igual o peso argentino todo quebrado
        self._x_no_rect = self.rect.x
        self.vel_y = 0
        self.on_ground = True
        self.cooldown_chute = 0
        # a cpu joga do lado direito, então o sprite é espelhado para as chuteiras apontarem para o jogador
        self.image = carregar_sprite(f"sprites/{personagem}.png", (70, 70), espelhar=True)

    def executar_acoes(self, acoes):
        if self.rect.x != self._x_no_rect:
            self.x = float(self.rect.x)

        if "esquerda" in acoes:
            self.x -= self.speed
        if "direita" in acoes:
            self.x += self.speed
        if "pular" in acoes and self.on_ground:
            self.vel_y = PLAYER_JUMP
            self.on_ground = False

        self.x = max(0, min(self.x, SCREEN_W - self.rect.width))

        self.rect.x = round(self.x)
        self._x_no_rect = self.rect.x

        if self.cooldown_chute > 0:
            self.cooldown_chute -= 1

    def chutar(self, ball):
        if self.cooldown_chute > 0:
            return False

        self.cooldown_chute = 15

        if ball.rect.centerx <= self.rect.centerx:
            ball.vel_x = -self.forca_chute
            ball.vel_y = -11
        else:
            ball.vel_x = -int(self.forca_chute * 0.6)
            ball.vel_y = -12

        return True

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.y >= 415:
            self.rect.y = 415
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def desenhar(self,screen):
        desenhar_sprite(screen, self.image, self.rect)
