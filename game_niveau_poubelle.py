import pygame
import player_niveau_poubelle as player
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

    def check_collision(self, sprite,group,type,vol):
        if pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask):
            if type=='vert':
                s = pygame.mixer.Sound("bruitage/bouteil en verre.mp3")
                s.set_volume(vol-0.2)
                s.play()
            elif type=='jaune':
                s = pygame.mixer.Sound("bruitage/jaune.mp3")
                s.set_volume(vol-0.3)
                s.play()
            elif type == 'marron':
                s = pygame.mixer.Sound("bruitage/marron.mp3")
                s.set_volume(vol-0.2)
                s.play()
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