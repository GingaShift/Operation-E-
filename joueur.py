import pygame
import boss

class player:
    def __init__(self,vie,force,velocity):
        self.vie=vie
        self.force=force
        self.image=pygame.image.load('faux trouver le esign')
        self.rect=self.image.get_rect()
        self.rect.x=20
        self.rect.y=20
        self.velocity=velocity

    def __del__(self):
        pass

    def move_right(self):
        self.rect.x+=self.velocity
    def move_left(self):
        self.rect.x-=self.velocity
    def move_up(self):
        self.rect.y+=self.velocity
    def move_down(self):
        self.rect.y-=self.velocity
