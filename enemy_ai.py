import random
from settings import *

#ia da cpu baseada em regras. A cada "reacao" frames ela repensa a jogada:
# acha o ponto de encontro: o primeiro instante em que ela consegue chegar na bola
#a bola é prevista andando em linha reta, com quique na parede)
#se não dá para alcançar a bola, ou ela está fora da ona" do nível, volta para a posição de casa
#senão, vai até a bola pelo lad direito (de frente pro gol do jogador) e chuta
#pula quando a bola vem alta na direção dela
#entre uma "pensada" e outra ela só segue o alvo, e é isso que dá o tempo de reação.
#adificuldade vem de CPU_NIVEIS (settings.py): um nível por fase do campeonato.
class EnemyAI:

    def __init__(self, nivel=0):
        config = CPU_NIVEIS[min(nivel, len(CPU_NIVEIS) - 1)]

        self.reacao = config["reacao"]
        self.erro = config["erro"]
        self.zona = config["zona"]

        self.casa_x = int(SCREEN_W * 0.8)   
        self.horizonte = 240                

        self.resetar()

    def resetar(self):
        self.timer = 0
        self.alvo_x = self.casa_x
        self.quer_pular = False

    def decidir(self, enemy, ball):
        self.timer -= 1

        if self.timer <= 0:
            self.timer = self.reacao
            self._pensar(enemy, ball)

        acoes = []

        distancia = self.alvo_x - enemy.rect.centerx

        if distancia < -enemy.speed:
            acoes.append("esquerda")
        elif distancia > enemy.speed:
            acoes.append("direita")

        if self.quer_pular and enemy.on_ground:
            acoes.append("pular")
            self.quer_pular = False

        return acoes

    def _pensar(self, enemy, ball):
        self.quer_pular = self._deve_pular(enemy, ball)

        meu_x = enemy.rect.centerx

        ponto = None

        for frames in range(self.horizonte):
            bola_x = self._prever_x(ball, frames)

            if abs(bola_x - meu_x) <= enemy.speed * frames + 30:
                ponto = bola_x
                break

        if ponto is None or ponto < self.zona:
            self.alvo_x = self.casa_x
            return

        self.alvo_x = ponto + 35 + random.randint(-self.erro, self.erro)

    def _deve_pular(self, enemy, ball):
        dx = ball.rect.centerx - enemy.rect.centerx

        bola_alta = ball.rect.bottom < enemy.rect.top + 25
        vindo_pra_mim = ball.vel_x * dx <= 0

        return bola_alta and vindo_pra_mim and abs(dx) < 140

    def _prever_x(self, ball, frames):
        meia_bola = ball.rect.width / 2
        minimo = meia_bola
        maximo = SCREEN_W - meia_bola
        faixa = maximo - minimo

        x = ball.rect.centerx + ball.vel_x * frames

        x = (x - minimo) % (2 * faixa)

        if x > faixa:
            x = 2 * faixa - x

        return x + minimo
