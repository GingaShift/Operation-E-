import pygame
import projectile
class Gamer(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('pictures_secondmain/player.png')
        self.image = pygame.transform.scale(self.image,(128,128))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.score = 0

    def degat(self,amount):
        self.health -= amount


    def update_health_bar(self,surface):
        pygame.draw.rect(surface, (60,63,60),[self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46),[self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def launch_projectile(self):
        self.all_projectiles.add(projectile.Projectile(self))

    def move_right(self):
        if not (self.game.check_collision(self, self.game.all_vetneufs)) and not (self.game.check_collision(self, self.game.all_vetold)):
            self.rect.x += self.velocity

    def move_left(self):
        if not (self.game.check_collision(self, self.game.all_vetneufs)) and not (self.game.check_collision(self, self.game.all_vetold)):
            self.rect.x -= self.velocity

    def move_down(self):
        if not (self.game.check_collision(self, self.game.all_vetneufs)) and not (self.game.check_collision(self, self.game.all_vetold)):
            self.rect.y += self.velocity

    def move_up(self):
        if not (self.game.check_collision(self, self.game.all_vetneufs)) and not (self.game.check_collision(self, self.game.all_vetold)):
            self.rect.y -= self.velocity