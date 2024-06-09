import pygame
import player_final
import objet1
import objet2


class Game():

    def __init__(self):
        self.all_player = pygame.sprite.Group()
        self.player = player_final.Player()
        self.all_player.add(self.player)
        self.all_wobj = pygame.sprite.Group()
        self.all_robj = pygame.sprite.Group()
        self.pressed = {}
        self.max_time = 1000
        self.time = 1000
        self.score=0
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    def spawn_wobj(self,type,x,y):
        self.all_wobj.add(objet1.wrong_obj(type,x,y,self))
    def spawn_robj(self,type,x,y):
        self.all_robj.add(objet2.right_obj(type,x,y,self))

    def update_health_bar(self,surface):
        if self.time!=0:
            pygame.draw.rect(surface, (60,63,60),[35, 775, self.max_time, 35])
            pygame.draw.rect(surface, (111,210,46),[35, 775, self.time, 35])
            self.time-=2
        else:
            pygame.draw.rect(surface, (60, 63, 60), [35, 775, self.max_time, 35])
            pygame.draw.rect(surface, (111, 210, 46), [35, 775, self.time, 35])
            self.time = self.max_time