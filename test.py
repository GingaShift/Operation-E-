import pygame
import sys


pygame.init()
display = pygame.display.set_mode((300,300))

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SCROLLLOCK :
                print("key j has been pressed")
