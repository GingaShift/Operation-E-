import pygame
import random
class Monster2(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 1
        self.maxhealth = 1
        self.degat = 1
        self.image = pygame.image.load('picture_poubelle/dj.png')
        self.type = 'jaune'
        self.rect = self.image.get_rect()
        self.rect.x=random.randint(50,680)
        self.rect.y=-500
        self.velocity = 1

    def damage(self,amount):
        self.health-=amount
        if self.health <=0:
            self.rect.y = 0 - random.randint(175,575)
            self.rect.x = random.randint(50,680)
            self.health=self.maxhealth

    def falling(self):
        if not self.game.check_collision(self,self.game.all_player,self.type):
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
                self.rect.y = 0 - random.randint(175,575)
                self.rect.x = random.randint(50, 680)
                self.health = self.maxhealth

