import pygame
import joueur

class boss():
    def __init__(self,nom,vie,image):
        self.nom=nom
        self.vie=vie
        self.image=pygame.image.load(image)
        self.rect=self.get_rect()
        self.rect.x=20
        self.rect.y=20

    def __del__(self):
        pass
    def move_right(self):
        self.rect.x+=self.velocity
    def move_left(self):
        self.rect.x-=self.velocity
    def move_up(self):
        self.rect.y+=self.velocity
    def move_down(self):
        self.rect.y-=self.velocity

class boss_enigme(boss):
    def __init__(self,question,reponse):
        boss.__init__(self)
        self.question=question
        self.reponse=reponse

    def __del__(self):
        pass

    def ask_question(self):
        return self.question

    def check_answer(self,reponse):
        if reponse==self.reponse:
            return True
        else:
            return False
