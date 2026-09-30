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
        self.placar_player = 0
        self.placar_cpu = 0
        self.gol_esquerdo = pygame.Rect(0,400,100,200)
        self.gol_direito = pygame.Rect(920,430,80,100)
        self.time = TIME_MATCH
        self.time_last = pygame.time.get_ticks()
        self.background = pygame.image.load("asserts/imagens/fundo.jpeg")
        self.background = pygame.transform.scale(self.background, (SCREEN_W, SCREEN_H))
    

    def events(self, screen):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(FPS)

            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.time_last >= 1000:
                if self.time > 0:
                    self.time -= 1

                self.time_last = tempo_atual

            if self.time <= 0:
                return "menu"



            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.time_last >= 1000:
                if self.time > 0:
                    self.time -= 1

                self.time_last = tempo_atual
            
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
            self.var()

            screen.blit(self.background, (0,0))
            self.player.desenhar(screen)
            self.enemy.desenhar(screen)
            self.ball.desenhar(screen)

            fonte_tempo = pygame.font.Font(None, 50)
            text_tempo = fonte_tempo.render(str(self.time), True, WHITE)
            screen.blit(text_tempo, (SCREEN_W // 2 - 15, 20))

            fonte_placar = pygame.font.Font(None, 50)
            texto_placar = fonte_placar.render(f"PLAYER {self.placar_player} X {self.placar_cpu} CPU", True, WHITE)
            screen.blit(texto_placar, (SCREEN_W // 2 - 150, 70))



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


    def var(self):

        if self.ball.rect.colliderect(self.gol_esquerdo):
            print("GOL da CPU")

            self.placar_cpu += 1

            self.ball.rect.x = SCREEN_W // 2
            self.ball.rect.y = SCREEN_H // 2
            self.ball.vel_x = 0
            self.ball.vel_y = 0

        if self.ball.rect.colliderect(self.gol_direito):
            print("GOLLLLL DO JOGADORR!")

            self.placar_player += 1

            self.ball.rect.x = SCREEN_W // 2
            self.ball.rect.y = SCREEN_H // 2
            self.ball.vel_x = 0
            self.ball.vel_y = 0