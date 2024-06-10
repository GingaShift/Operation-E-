import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 5
        self.max_health = 5
        self.type = "marron"
        self.degat = 1
        self.velocity = 9
        self.image = pygame.image.load("picture_poubelle/pm.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.score = 0

    def upimage(self):
        if self.type == "marron":
            self.image = pygame.image.load("picture_poubelle/pm.png")
        elif self.type == "jaune":
            self.image = pygame.image.load("picture_poubelle/pj.png")
        elif self.type == "vert":
            self.image = pygame.image.load("picture_poubelle/pv.png")
    def dammage(self, amount):
        self.health -= amount


    def moveright(self):
        self.rect.x += self.velocity
        for monster in self.game.check_collision(self, self.game.all_dechet,self.type):
            monster.damage(self.degat)
            if not monster.type == self.game.gamer.type:
                self.dammage(monster.degat)
            else:
                self.score+=1
        for monster1 in self.game.check_collision(self, self.game.all_dechet1,self.type):
            monster1.damage(self.degat)
            if not monster1.type == self.game.gamer.type:
                self.dammage(monster1.degat)
            else:
                self.score+=1
        for monster2 in self.game.check_collision(self, self.game.all_dechet2,self.type):
            monster2.damage(self.degat)
            if not monster2.type == self.game.gamer.type:
                self.dammage(monster2.degat)
            else:
                self.score+=1

    def moveleft(self):
        self.rect.x -= self.velocity
        for monster in self.game.check_collision(self, self.game.all_dechet,self.type):
            monster.damage(self.degat)
            if not monster.type == self.game.gamer.type:
                self.dammage(monster.degat)
            else:
                self.score+=1
        for monster1 in self.game.check_collision(self, self.game.all_dechet1,self.type):
            monster1.damage(self.degat)
            if not monster1.type == self.game.gamer.type:
                self.dammage(monster1.degat)
            else:
                self.score += 1
        for monster2 in self.game.check_collision(self, self.game.all_dechet2,self.type):
            monster2.damage(self.degat)
            if not monster2.type == self.game.gamer.type:
                self.dammage(monster2.degat)
            else:
                self.score+=1