import pygame
from moviepy.editor import VideoFileClip


def play_video(video_path):
    try:
        clip = VideoFileClip(video_path)
        clip.preview()
    except Exception as e:
        print(f"Error playing video {video_path}: {e}")

pygame.init()

class Button:
    def __init__(self, text, x_pos, y_pos, width, height, enabled,screen,font):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 295
        self.height = 60
        self.enabled = enabled
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.draw(screen,font)

    def draw(self,screen,font):
        button_color = 'gray'
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            button_color = 'lightgray'  # Change la couleur lors du survol
        pygame.draw.rect(screen, button_color, self.rect, 0, 5)
        pygame.draw.rect(screen, 'black', self.rect, 2, 5)
        button_text = font.render(self.text, True, 'black')
        text_rect = button_text.get_rect(center=self.rect.center)
        screen.blit(button_text, text_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if left_click and self.rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class Quiz:
    def __init__(self):
        self.questions = ["Le quart des émissions de gaz à effet de serre en France provient de nos assiettes?",
                          "Quel aliment est en tête du classement des aliments les plus polluants en\ngaz à effet de serre?",
                          "Quel aliment ne favorise pas la réduction de son empreinte carbone ?",
                          "Les aliments suivants : \"le tabac, l’huile de palme, le sucre de canne, le cacao, le café\"\ncontribuent-ils à la déforestation?",
                          "À quoi ne contribuent pas les produits suremballés?"]
        self.answers = [
            ["Vrai", "Faux"],
            ["La viande", "La tomate", "Le champignon", "Les graines"],
            ["Les algues", "Fruits locaux", "Légumes locaux", "Produits laitiers"],  # Ajouter une virgule ici
            ["Vrai", "Faux"],
            ["Pollution plastique","Au bien de la planète","Destruction des espèces","Favorise l'acte d'acheter"]
        ]
        self.correct_answers = [0, 0, 3,0,1]
        self.current_question = 0
        self.score = 0
        self.answered = False
        self.feedback_time = 0
        self.feedback_text = ""

    def display_question(self,WIDTH,HEIGHT,screen,new_image,final_score_position,font):
        if self.current_question < len(self.questions):
            if not self.answered:
                text_x = (WIDTH - new_image.get_width()) // 2 + 200
                text_y = (HEIGHT - new_image.get_height()) // 2 + 650
                button_x = (WIDTH - new_image.get_width()) // 2 + 200
                button_y = (HEIGHT - new_image.get_height()) // 2 + 723

                question_parts = self.questions[self.current_question].split('\n')

                for i, part in enumerate(question_parts):
                    question_text = font.render(part, True, 'black')
                    screen.blit(question_text, (text_x, text_y + i * 30))

                horizontal_margin = 320
                vertical_margin = 80

                for i, answer in enumerate(self.answers[self.current_question]):
                    col = i % 2
                    row = i // 2
                    button = Button(answer, button_x + col * horizontal_margin, button_y + row * vertical_margin, 200, 60, True,screen,font)
                    if button.check_click():
                        self.answered = True
                        if i == self.correct_answers[self.current_question]:
                            self.feedback_text = "Gagné!"
                            self.score += 1
                        else:
                            self.feedback_text = "Perdu!"
                        self.feedback_time = pygame.time.get_ticks()
            return True
        else:
            score_text = font.render("Score final : " + str(self.score), True, 'black')
            screen.blit(score_text, final_score_position)
            return False

    def next_question(self):
        if self.answered:
            if pygame.time.get_ticks() - self.feedback_time >= 1200:
                self.current_question += 1
                self.answered = False
                self.feedback_text = ""
def start_piggy():
    play_video("boss.mp4")
    WIDTH = 1920
    HEIGHT = 1080
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    fps = 60
    timer = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 24)
    pygame.display.set_caption('Quiz')
    background_image = pygame.image.load("Untitled.jpeg").convert()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # Charger et redimensionner la nouvelle image
    new_image = pygame.image.load("rectangle.png").convert_alpha()
    new_image = pygame.transform.scale(new_image, (1500, 1000))

    boss_image = pygame.image.load("cochon boss.png").convert_alpha()
    boss_image = pygame.transform.scale(boss_image, (420, 420))

    hero_image = pygame.image.load("hero.png").convert_alpha()
    hero_image = pygame.transform.scale(hero_image, (400, 300))

    # Agrandir l'image du héros tout en conservant les proportions
    hero_scale_factor = 1.3
    hero_width = int(hero_image.get_width() * hero_scale_factor)
    hero_height = int(hero_image.get_height() * hero_scale_factor)
    hero_image = pygame.transform.scale(hero_image, (hero_width, hero_height))

    # Positions des textes
    feedback_text_position = ((WIDTH - 350) // 2 + 100, 780)
    final_score_position = ((WIDTH - 350) // 2 + 40, 780)

    quiz = Quiz()

    # Jouer la vidéo avant de commencer le jeu


    run = True
    while run:
        screen.fill('white')
        timer.tick(fps)
        screen.blit(background_image, (0, 0))
        screen.blit(new_image, ((WIDTH - new_image.get_width()) // 2 - 30, (HEIGHT - new_image.get_height()) // 2 + 400))
        screen.blit(boss_image, ((WIDTH - boss_image.get_width()) // 2 + 320, (HEIGHT - boss_image.get_height()) // 2 - 75))
        screen.blit(hero_image, ((WIDTH - boss_image.get_width()) // 2 - 350, (HEIGHT - hero_image.get_height()) // 2 - 90))
        fin = quiz.display_question(WIDTH,HEIGHT,screen,new_image,final_score_position,font)
        if not fin:
            run=False
        if quiz.feedback_text:
            feedback_display_time = pygame.time.get_ticks() - quiz.feedback_time
            if feedback_display_time < 1000:
                feedback_surface = font.render(quiz.feedback_text, True, 'black')
                screen.blit(feedback_surface, feedback_text_position)
            else:
                quiz.next_question()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.QUIT()
        pygame.display.flip()
    if quiz.score >=4:
        return True
    else:
        return False

