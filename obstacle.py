import random

import pygame

class etg(pygame.sprite.Sprite):

    def __init__(self,game,y):
        super().__init__()
        self.game=game
        self.image = pygame.image.load("pictures_secondemain/etagere.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = y
        self.velocity = 1

    def forward(self):
        self.rect.x -= self.velocity
        if self.game.check_collision(self, self.game.all_gamer):
            self.game.gamer.rect.x -= 5
            if not(self.game.gamer.rect.y <= self.rect.y <= self.game.gamer.rect.y + 120):
                self.game.gamer.rect.x +=5
            elif self.rect.x<self.game.gamer.rect.x:
                self.game.gamer.rect.x += 10
            if self.game.gamer.rect.x <=0 - self.game.gamer.image.get_width():
                self.game.gamer.health -= 20
                self.game.gamer.rect.x = 10
        if self.rect.x <=0 - self.image.get_width():
            self.rect.x = 1000 + random.randint(0,1000)