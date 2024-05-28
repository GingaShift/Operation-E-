import pygame
import random
class Monster2(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 1
        self.maxhealth = 1
        self.degat = 1
        self.image = pygame.image.load('picture/dj.png')
        self.type = 'jaune'
        self.rect = self.image.get_rect()
        self.rect.x=random.randint(50,680)
        self.rect.y=-5000
        self.velocity = 1

    def damage(self,amount):
        self.health-=amount
        if self.health <=0:
            self.rect.y = 0 - random.randint(1000,5000)
            self.rect.x = random.randint(50,680)
            self.health=self.maxhealth

    def falling(self):
        if not self.game.check_collision(self,self.game.all_player):
            self.rect.y += self.velocity
        if self.rect.y == 720:
            self.game.gamer.dammage(self.degat)
            self.health-=1
            if self.health <= 0:
                self.rect.y = 0 - random.randint(1000,5000)
                self.rect.x = random.randint(50, 680)
                self.health = self.maxhealth

