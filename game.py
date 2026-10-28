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
        self.fase = 0
        self.fases = ["QUARTAS DE FINAL","SEMIFINAL","FINAL"]

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
                resultado = self.tela_resultado(screen)

                if resultado == "menu":
                    return "menu"

                if resultado == "proxima":
                    self.fase += 1

                self.reiniciar_partida()
                continue




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

    
    def tela_resultado(self, screen):
        clock = pygame.time.Clock()

        venceu = self.placar_player > self.placar_cpu
        perdeu = self.placar_player < self.placar_cpu
        empatou = self.placar_player == self.placar_cpu

        if venceu:
            if self.fase == 2:
                mensagem = "VOCE E CAMPEAO!"
                botao_texto = "VOLTAR AO MENU"
                acao = "menu"
            else:
                mensagem = "VOCE AVANCOU!"
                botao_texto = "PROXIMA FASE"
                acao = "proxima"

        elif perdeu:
            mensagem = "ELIMINADO!"
            botao_texto = "VOLTAR AO MENU"
            acao = "menu"

        else:
            mensagem = "EMPATE!"
            botao_texto = "JOGAR NOVAMENTE"
            acao = "repetir"

        fonte_titulo = pygame.font.Font(None, 65)
        fonte_placar = pygame.font.Font(None, 45)
        fonte_botao = pygame.font.Font(None, 32)
        fonte_fase = pygame.font.Font(None, 35)

        botao = pygame.Rect(
            SCREEN_W // 2 - 150, 390, 300, 60
        )

        while True:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "menu"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao.collidepoint(event.pos):
                        return acao

            screen.blit(self.background, (0, 0))

            fase_texto = fonte_fase.render(
                self.fases[self.fase], True, WHITE
            )
            screen.blit(
                fase_texto,
                fase_texto.get_rect(
                    center=(SCREEN_W // 2, 140)
                )
            )

            titulo = fonte_titulo.render(
                mensagem, True, WHITE
            )
            screen.blit(
                titulo,
                titulo.get_rect(
                    center=(SCREEN_W // 2, 220)
                )
            )

            placar = fonte_placar.render(
                f"PLAYER {self.placar_player} X "
                f"{self.placar_cpu} CPU",
                True, WHITE
            )
            screen.blit(
                placar,
                placar.get_rect(
                    center=(SCREEN_W // 2, 300)
                )
            )

            pygame.draw.rect(screen, (40, 140, 60), botao)

            texto = fonte_botao.render(
                botao_texto, True, WHITE
            )
            screen.blit(
                texto,
                texto.get_rect(center=botao.center)
            )

            pygame.display.update()

    def update(self):
        # movimentos, colisões e a fisica vai ficar aqui
        pass

    
    def reiniciar_partida(self):
        self.player = Player(150, SCREEN_H - 70)
        self.enemy = Enemy(800, SCREEN_H - 70)

        self.ball = Bola(SCREEN_W // 2, SCREEN_H // 2)
        self.ball.rect.center = (SCREEN_W // 2, SCREEN_H // 2)

        self.placar_player = 0
        self.placar_cpu = 0

        self.time = TIME_MATCH
        self.time_last = pygame.time.get_ticks()


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

            # Volta o jogador para a posição inicial
            self.player.rect.x = 150
            self.player.rect.y = SCREEN_H - 70
            self.player.vel_y = 0
            self.player.on_ground = True

            # Volta a CPU para a posição inicial
            self.enemy.rect.x = 800
            self.enemy.rect.y = SCREEN_H - 70
            self.enemy.vel_y = 0

            # Volta a bola para o centro
            self.ball.rect.center = (SCREEN_W // 2, SCREEN_H // 2)
            self.ball.vel_x = 0
            self.ball.vel_y = 0

        elif self.ball.rect.colliderect(self.gol_direito):
            print("GOL DO JOGADOR!")

            self.placar_player += 1

            # Volta o jogador para a posição inicial
            self.player.rect.x = 150
            self.player.rect.y = SCREEN_H - 70
            self.player.vel_y = 0
            self.player.on_ground = True

            # Volta a CPU para a posição inicial
            self.enemy.rect.x = 800
            self.enemy.rect.y = SCREEN_H - 70
            self.enemy.vel_y = 0

            # Volta a bola para o centro
            self.ball.rect.center = (SCREEN_W // 2, SCREEN_H // 2)
            self.ball.vel_x = 0
            self.ball.vel_y = 0
