import pygame
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Futebol de Cabeção")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()