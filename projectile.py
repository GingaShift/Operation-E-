import pygame
import game
class Projectile(pygame.sprite.Sprite):

    def __init__(self, gamer):
        super().__init__()
        self.velocity = 5
        self.gamer = gamer
        self.image = pygame.image.load("pictures/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = gamer.rect.x + 120
        self.rect.y = gamer.rect.y + 80
        self.origin_image = self.image
        self.angle=0

    def rotate(self):
        self.angle += 24
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.gamer.all_projectiles.remove(self)
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        for vetn in self.gamer.game.check_collision(self, self.gamer.game.all_vetneufs):
            self.remove()
            vetn.degat(self.gamer.attack)
        for veto in self.gamer.game.check_collision(self, self.gamer.game.all_vetold):
            self.remove()
            veto.degat(self.gamer.attack)
        if self.rect.x >1080:
            self.remove()
