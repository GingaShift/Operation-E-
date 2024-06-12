import pygame
import random

class wrong_obj(pygame.sprite.Sprite):

    def __init__(self,type,x,y,game):
        super().__init__()
        self.helth = 1
        self.max_health = 1
        self.atk = 3
        self.game=game
        if type=='badcar':
            if random.randint(1,2) == 2:
                self.image = pygame.image.load('Asset_final/car.png')
            else:
                self.image = pygame.image.load('Asset_final/moto.png')
        elif type=='waterman':
            if random.randint(1,2) == 2:
                self.image = pygame.image.load('Asset_final/closer.png')
            else:
                self.image = pygame.image.load('Asset_final/luf.png')
        elif type=='piggy':
            if random.randint(1,2)==2:
                self.image = pygame.image.load('Asset_final/meal.png')
            else:
                self.image = pygame.image.load('Asset_final/chimique.png')
        elif type=='garbage':
            self.image=pygame.image.load('Asset_final/ordxpbl.png')
        elif type=='second':
            self.image = pygame.image.load('Asset_final/newvet.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.answer = False

    def remove(self,screen):
        if pygame.Surface.get_at(screen,(1034,775)) == (111, 210, 46, 255) or self.game.check_collision(self, self.game.all_player):
            self.game.all_wobj.remove(self)
            self.game.player.health-=1




    def removerest(self):
        self.game.all_wobj.remove(self)