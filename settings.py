# LARGURA DA TELA E OS FRAMES POR SEGUNDO:
SCREEN_W= 1000
SCREEN_H= 600
FPS= 60 
TIME_MATCH= 10


# FISICA DO JOGNO
GRAVITY = 0.4
PLAYER_SPEED = 5
PLAYER_JUMP = -11.5
BALL_RESTITUTION = 0.7

# DIFICULDADE DOCPU
CPU_NIVEIS = [
    {"velocidade": 3.5, "reacao": 9, "erro": 30, "chute": 8,  "zona": 250},
    {"velocidade": 4, "reacao": 8,  "erro": 20, "chute": 9,  "zona": 150},
    {"velocidade": 4.75, "reacao": 6,  "erro": 14, "chute": 10, "zona": 0},
]

# CORES
WHITE  = (255, 255, 255)  # dermacação do campo e as do gol
GREEN  = ( 34, 139,  34)  # gramado
BLACK  = (  0,   0,   0)  # boorda