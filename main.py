import pygame
from settings import *
from game import Game

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("IFut Heads")

game = Game()
game.events(screen)


pygame.quit()
