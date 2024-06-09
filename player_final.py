import pygame.sprite
import game_final

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 3
        self.max_health = 3
        self.velocity = 9
        self.image = pygame.image.load("Asset_final/img.png")
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect =self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
