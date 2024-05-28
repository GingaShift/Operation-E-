import pygame
import player
import neuf
import old
import obstacle
class Game:

    def __init__(self):
        self.all_gamer= pygame.sprite.Group()
        self.gamer=player.Gamer(self)
        self.all_gamer.add(self.gamer)
        self.all_vetneufs = pygame.sprite.Group()
        self.all_vetold = pygame.sprite.Group()
        self.all_obs = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_vetneuf()
        self.spawn_vetold()
        self.spawn_obs(168)
        self.spawn_obs(168)
        self.spawn_obs(405)
        self.spawn_obs(405)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_vetneuf(self):
        vetsold = old.vet_old(self)
        self.all_vetold.add(vetsold)

    def spawn_vetold(self):
        vetsneufs = neuf.vet_neuf(self)
        self.all_vetneufs.add(vetsneufs)

    def spawn_obs(self,y):
        obs=obstacle.etg(self,y)
        self.all_obs.add(obs)