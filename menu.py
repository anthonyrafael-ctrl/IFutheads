import pygame
import sys

class Menu:

    def __init__(self):

        self.fonte_titulo = pygame.font.Font(None, 90)
        self.fonte_botao = pygame.font.Font(None, 50)

        self.botao_jogar = pygame.Rect(400, 250, 200, 60)
        self.botao_creditos = pygame.Rect(400, 340, 200, 60)
        self.botao_sair = pygame.Rect(400, 430, 200, 60)

    def draw(self, screen):

        screen.fill((30, 120, 30))

        titulo = self.fonte_titulo.render(
            "IFutHeads",
            True,
            (255,255,255)
        )

        screen.blit(titulo, (320,100))

        pygame.draw.rect(screen, (255,255,255), self.botao_jogar)
        pygame.draw.rect(screen, (255,255,255), self.botao_creditos)
        pygame.draw.rect(screen, (255,255,255), self.botao_sair)

        texto_jogar = self.fonte_botao.render(
            "JOGAR",
            True,
            (0,0,0)
        )

        texto_creditos = self.fonte_botao.render(
            "CRÉDITOS",
            True,
            (0,0,0)
        )

        texto_sair = self.fonte_botao.render(
            "SAIR",
            True,
            (0,0,0)
        )

        screen.blit(texto_jogar, (445,265))
        screen.blit(texto_creditos, (415,355))
        screen.blit(texto_sair, (460,445))

    def handle_events(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            if self.botao_jogar.collidepoint(mouse_pos):
                return "jogar"

            if self.botao_creditos.collidepoint(mouse_pos):
                return "creditos"

            if self.botao_sair.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

        return None