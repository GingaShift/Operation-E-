import pygame
import player_niveau_poubelle
import dechet
import dechetj
import dechetv
class Game:

    def __init__(self):
        self.all_player = pygame.sprite.Group()
        self.gamer = player.Player(self)
        self.all_player.add(self.gamer)
        self.all_dechet = pygame.sprite.Group()
        self.all_dechet1 = pygame.sprite.Group()
        self.all_dechet2 = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster1()
        self.spawn_monster2()
    def check_collision(self, sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        Dechet = dechet.Monster(self)
        self.all_dechet.add(Dechet)

    def spawn_monster1(self):
        Dechet1 = dechetv.Monster1(self)
        self.all_dechet1.add(Dechet1)

    def spawn_monster2(self):
        Dechet2 = dechetj.Monster2(self)
        self.all_dechet2.add(Dechet2)