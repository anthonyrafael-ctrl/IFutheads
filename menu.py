import pygame
import sys
import settings

tela = pygame.display.set_mode((1600, 900))
fundo = pygame.image.load("menu.png")
fundo = pygame.transform.scale(fundo, (1600, 900))
class Menu:

    def __init__(self):

        self.fonte_titulo = pygame.font.Font(None, 90)
        self.fonte_botao = pygame.font.Font(None, 50)

        self.botao_jogar = pygame.Rect(400, 250, 200, 60)
        self.botao_creditos = pygame.Rect(400, 340, 200, 60)
        self.botao_sair = pygame.Rect(400, 430, 200, 60)
        self.botao_voltar = pygame.Rect(400, 500, 200, 60)

        self.fundo_menu = pygame.image.load("asserts/imagens/image.png").convert()
        self.fundo_menu = pygame.transform.scale(self.fundo_menu,(settings.SCREEN_W, settings.SCREEN_H))

    def draw(self, screen):

        screen.blit(self.fundo_menu, (0, 0))

        pygame.draw.rect(screen, (255,255,255), self.botao_jogar)
        pygame.draw.rect(screen, (255,255,255), self.botao_creditos)
        pygame.draw.rect(screen, (255,255,255), self.botao_sair)

        texto_jogar = self.fonte_botao.render("JOGAR",True,(0,0,0))

        texto_creditos = self.fonte_botao.render("CRÉDITOS",True,(0,0,0))

        texto_sair = self.fonte_botao.render("SAIR",True,(0,0,0))

        screen.blit(texto_jogar, (445,265))
        screen.blit(texto_creditos, (415,355))
        screen.blit(texto_sair, (460,445))


    def creditos(self, screen):
        screen.fill((0, 0, 0))

        titulo = self.fonte_titulo.render(
            "CRÉDITOS",
            True,
            (255,255,255)
        )

        subtitulo = self.fonte_botao.render(
            "IFutHeads",
            True,
            (255,255,255)
        )

        texto1 = self.fonte_botao.render(
            "Desenvolvido por",
            True,
            (255,255,255)
        )

        texto2 = self.fonte_botao.render(
            "Anthony Rafael & Rafael Araújo",
            True,
            (255,255,255)
        )

        texto3 = self.fonte_botao.render(
            "Projeto desenvolvido para o IFRN-ca",
            True,
            (200,200,200)
        )

        screen.blit(titulo, (390, 80))
        screen.blit(subtitulo, (440, 200))
        screen.blit(texto1, (385, 270))
        screen.blit(texto2, (330, 320))
        screen.blit(texto3, (350, 370))

        pygame.draw.rect( screen, (255,255,255), self.botao_voltar)


        voltar = self.fonte_botao.render("VOLTAR", True, (0,0,0))
        screen.blit(voltar, (440,515))


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

            if self.botao_voltar.collidepoint(mouse_pos):
                return "voltar"

        return None