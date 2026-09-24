import pygame
from settings import *
from enemy import Enemy
from ball import Bola
from player import Player

#modifiquei classe game. 
class Game:
    def __init__(self):
        self.player = Player(150,SCREEN_H - 50)
        self.enemy = Enemy(800, SCREEN_H - 50)
        self.ball = Bola(SCREEN_W // 2, SCREEN_H // 2)
        self.background = pygame.image.load("asserts/imagens/fundo.jpeg")
        self.background = pygame.transform.scale(self.background, (SCREEN_W, SCREEN_H))
    

    def events(self, screen):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            #movimentações 

            self.player.mover(keys)
            self.player.pular(keys)
            self.player.apply_gravity()

            self.enemy.seguir_bola(self.ball)
            self.enemy.apply_gravity()

            self.ball.apply_gravity()
            self.ball.mover()
            self.colisao(keys)

            screen.blit(self.background, (0,0))
            self.player.desenhar(screen)
            self.enemy.desenhar(screen)
            self.ball.desenhar(screen)


            pygame.display.update()

    def update(self):
        # movimentos, colisões e a fisica vai ficar aqui
        pass

    def show(self):
        #limpar a tela pintando tudo de preto
        self.screen.fill(BLACK)
        pygame.display.flip()

    def colisao(self, keys):

        if self.player.rect.colliderect(self.ball.rect):
            
            if self.ball.rect.centerx > self.player.rect.centerx:
                
                if keys[pygame.K_SPACE]:
                    self.ball.vel_x = 10
                    self.ball.vel_y = -7
                    
                else:
                    self.ball.vel_x = 0
                    self.ball.vel_y = 0
                    self.ball.rect.left = self.player.rect.right



        if self.enemy.rect.colliderect(self.ball.rect):
            if self.enemy.rect.centerx < self.ball.rect.centerx:
                self.ball.vel_x = 7

            else:
                self.ball.vel_x = -7

            self.ball.vel_y = -5 
            
        if self.player.rect.colliderect(self.enemy.rect):
            
            if self.player.rect.centerx < self.enemy.rect.centerx:
                self.player.rect.x -= 5
                self.enemy.rect.x += 5
            
            else:
                self.player.rect.x += 5
                self.enemy.rect.x -= 5