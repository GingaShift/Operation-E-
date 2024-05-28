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
        self.image = pygame.image.load("picture/pm.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.score = 0

    def upimage(self):
        if self.type == "marron":
            self.image = pygame.image.load("picture/pm.png")
        elif self.type == "jaune":
            self.image = pygame.image.load("picture/pj.png")
        elif self.type == "vert":
            self.image = pygame.image.load("picture/pv.png")
    def dammage(self, amount):
        self.health -= amount
        if self.health <=0:
            pygame.quit()
    def update_health_bar(self,surface):
        pygame.draw.rect(surface,(60,63,60),[self.rect.x + 10, self.rect.y -20, self.max_health*30,5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health*30, 5])

    def moveright(self):
        self.rect.x += self.velocity
        for monster in self.game.check_collision(self, self.game.all_dechet):
            monster.damage(self.degat)
            if not monster.type == self.game.gamer.type:
                self.dammage(monster.degat)
            else:
                self.score+=1
        for monster1 in self.game.check_collision(self, self.game.all_dechet1):
            monster1.damage(self.degat)
            if not monster1.type == self.game.gamer.type:
                self.dammage(monster1.degat)
            else:
                self.score+=1
        for monster2 in self.game.check_collision(self, self.game.all_dechet2):
            monster2.damage(self.degat)
            if not monster2.type == self.game.gamer.type:
                self.dammage(monster2.degat)
            else:
                self.score+=1

    def moveleft(self):
        self.rect.x -= self.velocity
        for monster in self.game.check_collision(self, self.game.all_dechet):
            monster.damage(self.degat)
            if not monster.type == self.game.gamer.type:
                self.dammage(monster.degat)
            else:
                self.score+=1
        for monster1 in self.game.check_collision(self, self.game.all_dechet1):
            monster1.damage(self.degat)
            if not monster1.type == self.game.gamer.type:
                self.dammage(monster1.degat)
            else:
                self.score += 1
        for monster2 in self.game.check_collision(self, self.game.all_dechet2):
            monster2.damage(self.degat)
            if not monster2.type == self.game.gamer.type:
                self.dammage(monster2.degat)
            else:
                self.score+=1