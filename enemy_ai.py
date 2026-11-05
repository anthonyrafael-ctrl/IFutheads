import random
import json
import os

class EnemyAI:

    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 0.2
        self.estado_anterior = None
        self.acao_anterior = None
        self.memory_file = "ai_memory.json"
        self.carregar_memoria()

    def carregar_memoria(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as arquivo:
                self.q_table = json.load(arquivo)

    def salvar_memoria(self):
        with open(self.memory_file, "w") as arquivo:
            json.dump(self.q_table, arquivo)

    def observar_jogo(self, enemy, player, ball):
        distancia_bola = ball.rect.centerx - enemy.rect.centerx
        distancia_jogador = player.rect.centerx - enemy.rect.centerx

        if distancia_bola < -100:
            posicao_bola = "esquerda"
        elif distancia_bola > 100:
            posicao_bola = "direita"
        else:
            posicao_bola = "perto"

        if distancia_jogador < -100:
            posicao_jogador = "esquerda"
        elif distancia_jogador > 100:
            posicao_jogador = "direita"
        else:
            posicao_jogador = "perto"

        bola_alta = ball.rect.bottom < enemy.rect.top

        estado = (
            posicao_bola,
            posicao_jogador,
            bola_alta
        )

        return str(estado)

    def escolher_acao(self, estado):
        if estado not in self.q_table:
            self.q_table[estado] = {
                "esquerda": 0,
                "direita": 0,
                "pular": 0,
                "ficar": 0
            }

        if random.random() < self.exploration_rate:
            return random.choice(list(self.q_table[estado].keys()))

        melhores_acoes = self.q_table[estado]
        maior_valor = max(melhores_acoes.values())

        opcoes = [
            acao for acao, valor in melhores_acoes.items()
            if valor == maior_valor
        ]

        return random.choice(opcoes)

    def aprender(self, estado, acao, recompensa, proximo_estado):

        if estado not in self.q_table:
            self.escolher_acao(estado)

        if proximo_estado not in self.q_table:
            self.escolher_acao(proximo_estado)

        valor_atual = self.q_table[estado][acao]

        melhor_proximo_valor = max(self.q_table[proximo_estado].values())

        novo_valor = valor_atual + self.learning_rate * (recompensa + self.discount_factor * melhor_proximo_valor - valor_atual)

        self.q_table[estado][acao] = novo_valor

    def registrar_decisao(self, estado, acao):
        self.estado_anterior = estado
        self.acao_anterior = acao