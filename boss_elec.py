import pygame

class Boss(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 10
        self.max_health = 10
        self.image = pygame.image.load('Boss_elec/elec_boss.png')  # Charger l'image correctement
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = 432
        self.rect.y = 0

    def degat(self, amount):
        self.health -= amount
        if self.health <= 0:
            return True
        return False

    def forward(self):
        if self.game.check_collision(self, self.game.all_gamer):
            self.game.gamer.rect.y = self.game.screen.get_height() - self.game.gamer.rect.height
            self.degat(1)


    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y + 138, int(self.max_health*12.8), 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y + 138, int(self.health*12.8), 5])