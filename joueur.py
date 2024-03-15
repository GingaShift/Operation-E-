import pygame
import boss

class player(pygame.sprite.Sprite):
    def __init__(self,pseudo):
        super().__init__()
        self.pseudo=pseudo
        self.vie=60
        self.force=10
        self.image=pygame.image.load("pictures/download.jpg")
        self.rect=self.image.get_rect()
        self.rect.x=20
        self.rect.y=20
        self.velocity=20

    def __del__(self):
        pass

    def repondre(self,reponse):
        return reponse
    def move_right(self):
        self.rect.x+=self.velocity
    def move_left(self):
        self.rect.x-=self.velocity
    def move_up(self):
        self.rect.y+=self.velocity
    def move_down(self):
        self.rect.y-=self.velocity

    #commit and push 2
