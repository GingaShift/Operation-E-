import pygame
import random

class right_obj(pygame.sprite.Sprite):

    def __init__(self,type,x,y,game):
        super().__init__()
        self.helth = 1
        self.max_health = 1
        self.atk = 3
        self.game=game
        if type == 'badcar':
            if random.randint(1,2) == 2:
                self.image = pygame.image.load('Asset_final/pied.png')
            else:
                self.image = pygame.image.load('Asset_final/velo.png')
        elif type == 'waterman':
            if random.randint(1,2) == 2:
                self.image = pygame.image.load('Asset_final/openr.png')
            else:
                self.image = pygame.image.load('Asset_final/lumo.png')
        elif type == 'piggy':
            self.image = pygame.image.load('Asset_final/leg.png')
        elif type == 'garbage':
            self.image = pygame.image.load('Asset_final/ord.png')
        elif type == 'second':
            self.image = pygame.image.load('Asset_final/oldvet.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.aswer = True

    def remove(self,screen):
        if  self.game.check_collision(self, self.game.all_player) and pygame.Surface.get_at(screen, (1034, 775)) ==(60,63,60):
            self.game.all_robj.remove(self)
            self.game.score+=1
        elif pygame.Surface.get_at(screen, (1034, 775)) == (111, 210, 46, 255):
            self.game.all_robj.remove(self)
            self.game.player.health-=1
    def removerest(self):
        self.game.all_robj.remove(self)