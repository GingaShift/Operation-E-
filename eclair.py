import random
import pygame
import random

class Eclair(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        if random.randint(1,2)==1:
            self.image = pygame.image.load("Boss_elec/eclair.png")
        else:
            self.image = pygame.image.load("Boss_elec/eclair2.png")
        self.image = pygame.transform.scale(self.image, (180, 32))  # Largeur écran, 1/10 hauteur écran
        self.rect = self.image.get_rect()
        self.rect.x = game.screen.get_width()
        self.rect.y = random.choice([140,200, 270,330,390, 440])
        self.velocity = 7  # 3 fois plus rapide qu'avant

    def forward(self):
        self.rect.x -= self.velocity
        if self.game.check_collision(self, self.game.all_gamer):
            self.game.gamer.health -= 25  # Retire 10 pv au joueur en cas de collision
            self.kill()  # Supprime l'éclair en cas de collision
        if self.rect.x <= 0:
            self.kill()  # Supprime l'éclair s'il touche le bord gauche de l'écran

