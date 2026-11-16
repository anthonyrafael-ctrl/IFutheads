import os
import pygame

PASTA_IMAGENS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "asserts", "imagens")

_cache = {}


def carregar_sprite(arquivo, tamanho, espelhar=False):
    chave = (arquivo, tamanho, espelhar)

    if chave not in _cache:
        imagem = pygame.image.load(os.path.join(PASTA_IMAGENS, arquivo)).convert_alpha()

        largura, altura = imagem.get_size()
        escala = min(tamanho[0] / largura, tamanho[1] / altura)
        novo_tamanho = (max(1, round(largura * escala)), max(1, round(altura * escala)))

        imagem = pygame.transform.smoothscale(imagem, novo_tamanho)

        if espelhar:
            imagem = pygame.transform.flip(imagem, True, False)

        _cache[chave] = imagem

    return _cache[chave]


def desenhar_sprite(tela, imagem, rect):
    tela.blit(imagem, (rect.centerx - imagem.get_width() // 2,
                       rect.bottom - imagem.get_height()))
