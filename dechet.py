import pygame
import random
class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 1
        self.maxhealth = 1
        self.degat = 1
        self.image = pygame.image.load('picture_poubelle/dm.png')
        self.type = 'marron'
        self.rect = self.image.get_rect()
        self.rect.x=random.randint(50,680)
        self.rect.y=0
        self.velocity = 1

    def damage(self,amount):
        self.health-=amount
        if self.health <=0:
            self.rect.y = 0 - random.randint(100,500)
            self.rect.x = random.randint(50,680)
            self.health=self.maxhealth

    def falling(self,vol):
        if not self.game.check_collision(self,self.game.all_player,self.type,vol):
            self.rect.y += self.velocity
        else:
            self.damage(self.health)
            if self.type == self.game.gamer.type:
                self.game.gamer.score += 1
            else:
                self.game.gamer.dammage(1)
        if self.rect.y == 720:
            self.game.gamer.dammage(self.degat)
            self.health-=1
            if self.health <= 0:
                self.rect.y = 0 - random.randint(100,500)
                self.rect.x = random.randint(50, 680)
                self.health = self.maxhealth

