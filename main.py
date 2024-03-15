import pygame
import random
from joueur import*
from boss import*
pygame.init()

pygame.display.set_caption("Opération E")
screen = pygame.display.set_mode((900,760))

running=True
Player=player('moi')
while running:
    screen.blit(Player.image, Player.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            print('Fin du Jeu')

