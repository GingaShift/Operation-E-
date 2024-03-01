import pygame
import joueur

class boss():
    def __init__(self):
        pass

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
