import pygame
from game import Game
from menu import Menu
from settings import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("asserts/music/fell.mp3")
pygame.mixer.music.set_volume(0.1)

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("IFutHeads")

menu = Menu()
game = Game()

estado = "menu"
pygame.mixer.music.play(-1)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if estado == "menu":
            

            resultado = menu.handle_events(event)

            if resultado == "jogar":
                estado = "jogo"
                pygame.mixer.music.stop()
                pygame.mixer.music.load("asserts/music/torcida.mp3")
                pygame.mixer.music.play(-1)

            elif resultado == "creditos":
                estado = "creditos"

            elif resultado == "voltar":
                estado = "menu"

        elif estado == "creditos":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if menu.botao_voltar.collidepoint(mouse_pos):
                    estado = "menu"

    if estado == "menu":
        menu.draw(screen)

    elif estado == "jogo":
        game.events(screen)

    elif estado == "creditos":
        menu.creditos(screen)

    pygame.display.flip()

pygame.quit()