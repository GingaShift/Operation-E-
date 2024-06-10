import pygame
import player_elec
import eclair
import boss_elec

class Game:

    def __init__(self):
        self.all_gamer = pygame.sprite.Group()
        self.gamer = player_elec.Gamer(self)
        self.all_gamer.add(self.gamer)
        self.all_vetold = pygame.sprite.Group()  # Groupe pour les éclairs
        self.pressed = {}
        self.screen = None  # Pour la référence de l'écran
        self.boss = boss_elec.Boss(self)  # Initialiser le boss

        # Initialiser un timer pour l'apparition des éclairs
        self.eclair_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.eclair_timer, 750)  # 1000 ms = 1 seconde

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_vetold(self):
        f = eclair.Eclair(self)
        self.all_vetold.add(f)
