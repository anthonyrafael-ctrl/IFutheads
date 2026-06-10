import pygame
from game import Game
from menu import Menu
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("IFutHeads")

menu = Menu()
game = Game()

estado = "menu"

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if estado == "menu":

            resultado = menu.handle_events(event)

            if resultado == "jogar":
                estado = "jogo"

            elif resultado == "creditos":
                estado = "creditos"

    if estado == "menu":
        menu.draw(screen)

    elif estado == "jogo":
        game.events(screen)

    elif estado == "creditos":

        screen.fill((0,0,0))

        fonte = pygame.font.Font(None, 50)

        texto = fonte.render(
            "Desenvolvido por Anthony e Rafael Araújo.",
            True,
            (255,255,255)
        )

        screen.blit(texto, (180,280))

    pygame.display.flip()

pygame.quit()