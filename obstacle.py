import random

import pygame

class etg(pygame.sprite.Sprite):

    def __init__(self,game,y):
        super().__init__()
        self.game=game
        self.image = pygame.image.load("pictures/etagere.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = y
        self.velocity = 1

    def forward(self):
        self.rect.x -= self.velocity
        if self.game.check_collision(self, self.game.all_gamer):
            self.game.gamer.rect.x -= 5
            if self.game.gamer.rect.x <=0:
                self.game.gamer.health -= 20
                self.game.gamer.rect.x = 500
        if self.rect.x <=0:
            self.rect.x = 1000 + random.randint(0,1000)