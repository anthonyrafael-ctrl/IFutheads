import pygame
from settings import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # movimentos, colisões e a fisica vai ficar aqui
        pass

    def show(self):
        #limpar a tela pintando tudo de preto
        self.screen.fill(BLACK)
        pygame.display.flip()