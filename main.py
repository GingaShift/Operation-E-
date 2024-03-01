import pygame
import random
from joueur import*
from boss import*
pygame.init()

pygame.display.set_caption("Opération E")
pygame.display.set_mode((500,450))

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            print('Fin du Jeu')

