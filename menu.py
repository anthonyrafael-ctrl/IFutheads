import pygame
import sys
import settings
from sprites import carregar_sprite

tela = pygame.display.set_mode((1600, 900))
fundo = pygame.image.load("menu.png")
fundo = pygame.transform.scale(fundo, (1600, 900))
class Menu:

    def __init__(self):

        self.fonte_titulo = pygame.font.Font(None, 90)
        self.fonte_botao = pygame.font.Font(None, 50)
        self.fonte_selecao = pygame.font.Font(None, 65)

        self.botao_jogar = pygame.Rect(400, 250, 200, 60)
        self.botao_creditos = pygame.Rect(400, 340, 200, 60)
        self.botao_sair = pygame.Rect(400, 430, 200, 60)
        self.botao_voltar = pygame.Rect(400, 500, 200, 60)


        self.personagens = [
            {"chave": "lionel", "nome": "LIONEL ROLLIM", "sprite": "sprites/lionel.png"},
            {"chave": "cristiano", "nome": "CRISTIANO ROMERITO", "sprite": "sprites/cristiano.png"},
        ]
        self.personagem_selecionado = None
        self.botoes_personagens = [
            pygame.Rect(220, 300, 260, 200),
            pygame.Rect(520, 300, 260, 200),
        ]
        self.botao_continuar = pygame.Rect(400, 520, 200, 60)

        self.previas = [carregar_sprite(p["sprite"], (130, 130)) for p in self.personagens]
        self.nomes = [self._texto_ajustado(p["nome"], 230) for p in self.personagens]
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

    def personagem_screen(self, screen):

        screen.blit(self.fundo_menu, (0,0))

        titulo = self.fonte_selecao.render(
            "ESCOLHA SEU PERSONAGEM", True, (255, 255, 255))

        screen.blit(titulo, titulo.get_rect(center=(settings.SCREEN_W // 2, 270)))

        for i, botao in enumerate(self.botoes_personagens):

            if self.personagem_selecionado == i:
                cor_fundo, cor_borda, espessura = (255, 215, 0), (0, 110, 40), 6
            else:
                cor_fundo, cor_borda, espessura = (245, 245, 245), (60, 60, 60), 2

            pygame.draw.rect(screen, cor_fundo, botao, border_radius=12)
            pygame.draw.rect(screen, cor_borda, botao, espessura, border_radius=12)

            previa = self.previas[i]
            screen.blit(previa, previa.get_rect(midbottom=(botao.centerx, botao.y + 150)))

            nome = self.nomes[i]
            screen.blit(nome, nome.get_rect(center=(botao.centerx, botao.bottom - 28)))

        # o butotão fica cinza até o jogador escolher alguém
        cor_continuar = (255, 255, 255) if self.personagem_selecionado is not None else (160, 160, 160)
        pygame.draw.rect(screen, cor_continuar, self.botao_continuar)
        texto_continuar = self.fonte_botao.render("CONTINUAR", True, (0, 0, 0))
        
        screen.blit(texto_continuar, texto_continuar.get_rect(center=self.botao_continuar.center))

    def _texto_ajustado(self, texto, largura_max):
        # renderiza o textinhoo na maior fonte que ainda cabe em largura_max
        tamanho = 36

        while True:
            imagem = pygame.font.Font(None, tamanho).render(texto, True, (0, 0, 0))

            if imagem.get_width() <= largura_max or tamanho <= 14:
                return imagem

            tamanho -= 2

    def selecionar_personagem(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            mouse_pos = pygame.mouse.get_pos()
            
            for i, botao in enumerate(self.botoes_personagens):
                
                if botao.collidepoint(mouse_pos):
                    self.personagem_selecionado = i

            if self.botao_continuar.collidepoint(mouse_pos):
                if self.personagem_selecionado is not None:
                    return "continuar"


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