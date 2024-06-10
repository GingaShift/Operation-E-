import pygame

class Gamer(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.velocity = 3
        self.image = pygame.image.load('Boss_elec/player.png')
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def degat(self, amount):
        self.health -= amount

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def move_up(self):
        self.rect.y -= self.velocity
