import random

import pygame

class vet_neuf(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game=game
        self.health = 20
        self.max_health = 20
        self.attack = 1
        self.image = pygame.image.load("pictures_secondmain/vetement_neuf.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,1000)
        self.rect.y = random.choice([40,270,540])
        self.velocity = 1

    def degat(self,amount):
        self.health -= amount
        if self.health <=0:
            self.rect.x = 1000 + random.randint(0,1000)
            self.rect.y = random.choice([40, 270, 540])
            self.health=self.max_health
            self.game.gamer.score += 10

    def update_health_bar(self,surface):
        pygame.draw.rect(surface, (60,63,60),[self.rect.x + 10, self.rect.y - 20, self.max_health*5, 5])
        pygame.draw.rect(surface, (111,210,46),[self.rect.x + 10, self.rect.y - 20, self.health*5, 5])

    def forward(self):
        self.rect.x -= self.velocity
        if self.game.check_collision(self, self.game.all_gamer):
            self.game.gamer.rect.x -= 5
            self.game.gamer.degat(self.attack)
            if self.game.gamer.rect.x <=0:
                self.game.gamer.health -= 20
                self.game.gamer.rect.x = 500
        if self.rect.x <=0:
            self.degat(self.health)
            self.game.gamer.score-=10
