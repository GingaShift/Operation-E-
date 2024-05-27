import pygame
import sys

# Initialisation de pygame
pygame.init()

# Configuration de la fenêtre en plein écran
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption('Quiz Environnemental')

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
HIGHLIGHT_COLOR = (170, 170, 170)

# Polices
font_name = "Comic Sans MS"
question_font_size = 30
answer_font_size = 24
message_font_size = 36
question_font = pygame.font.SysFont(font_name, question_font_size)
answer_font = pygame.font.SysFont(font_name, answer_font_size)
message_font = pygame.font.SysFont(font_name, message_font_size)

# Charger et redimensionner l'image de fond
background_image = pygame.image.load('background_v_m.jpeg').convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Questions et réponses
questions = [
    ("Quel est le moyen de transport le plus écologique pour aller à l'école si tu habites près ?",
     [("La voiture", False),
      ("Le bus", False),
      ("La marche à pied", True)]),

    ("Qu'est-ce qui est mieux pour la planète : aller en vélo ou en voiture ?",
     [("Le vélo", True),
      ("La voiture", False)]),

    ("Pourquoi est-il bon de partager une voiture avec des amis ou des voisins pour aller quelque part ?",
     [("Parce que c'est plus amusant", False),
      ("Parce que ça pollue moins", True),
      ("Parce que c'est plus rapide", False)]),

    ("Quel moyen de transport ne produit pas de pollution ?",
     [("Le train", False),
      ("L'avion", False),
      ("La trottinette", True)]),

    ("Quel animal pouvons-nous observer dans la nature si nous nous déplaçons tranquillement à pied ou à vélo ?",
     [("Des poissons", False),
      ("Des oiseaux", True),
      ("Des girafes", False)]),

    ("Quand tu es dans une voiture, quelle action peut aider à économiser du carburant ?",
     [("Laisser les fenêtres ouvertes", False),
      ("Éteindre le moteur quand on est arrêté", True),
      ("Mettre de la musique très fort", False)]),

    ("Pourquoi est-il important de marcher ou de faire du vélo au lieu de prendre toujours la voiture ?",
     [("Pour rester en bonne santé", False),
      ("Pour économiser de l'argent", False),
      ("Pour protéger la planète", True)]),

    ("Quel est un bon moyen de se déplacer en ville sans polluer ?",
     [("La moto", False),
      ("Le tramway", True),
      ("Le bus", False)]),

    ("Quel est le carburant utilisé par les voitures électriques ?",
     [("L'essence", False),
      ("Le diesel", False),
      ("L'électricité", True)]),

    ("Que peux-tu faire pour aider à protéger l'environnement lorsque tu te déplaces ?",
     [("Jeter les déchets par terre", False),
      ("Utiliser une bouteille d'eau réutilisable", True),
      ("Laisser les lumières allumées", False)])
]

score = 0
current_question = 0

# Fonction pour dessiner du texte au centre de l'écran
def draw_text(text, font, color, surface, x, y, max_width=None):
    words = text.split(' ')
    lines = []
    current_line = []

    # Définition de la largeur maximale par défaut si aucune n'est fournie
    if max_width is None:
        max_width = surface.get_width()

    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    lines.append(' '.join(current_line))

    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, y + y_offset))
        surface.blit(text_surface, text_rect)
        y_offset += font.get_linesize()

# Fonction principale du quiz
def quiz():
    global score, current_question
    running = True
    while running:
        screen.blit(background_image, (0, 0))

        # Récupération de la question et des réponses actuelles
        question, answers = questions[current_question]

        # Affichage de la question
        draw_text(question, question_font, BLACK, screen, screen_width // 2, 100, max_width=screen_width - 100)

        # Gestion des événements
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, (answer, is_correct) in enumerate(answers):
                    if button_rects[i].collidepoint(event.pos):
                        if is_correct:
                            score += 1
                        current_question += 1
                        if current_question >= len(questions):
                            running = False
                        break

        # Affichage des réponses sous forme de boutons
        button_rects = []
        button_width = screen_width // 2
        button_height = 60
        for i, (answer, is_correct) in enumerate(answers):
            button_rect = pygame.Rect(screen_width // 4, 200 + i * (button_height + 20), button_width, button_height)
            button_rects.append(button_rect)
            if button_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, button_rect)
            else:
                pygame.draw.rect(screen, LIGHT_GRAY, button_rect)
            draw_text(answer, answer_font, BLACK, screen, screen_width // 2, 200 + i * (button_height + 20) + button_height // 2)

        pygame.display.flip()

# Fonction pour afficher le score final
def show_score():
    global score, current_question
    running = True
    while running:
        screen.blit(background_image, (0, 0))

        # Message de score
        if score >= 8:
            message = f'Félicitations! Vous avez passé le niveau avec un score de {score} / {len(questions)}'
        else:
            message = f'Votre score : {score} / {len(questions)}. Vous devez refaire le niveau.'

        draw_text(message, message_font, BLACK, screen, screen_width // 2, screen_height // 2 - 50, max_width=screen_width - 100)
        draw_text('Cliquez pour retourner au menu principal', message_font, DARK_GRAY, screen, screen_width // 2, screen_height // 2 + 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        pygame.display.flip()

# Fonction pour afficher le menu principal
def main_menu():
    running = True
    while running:
        screen.blit(background_image, (0, 0))
        draw_text('Quiz Environnemental', message_font, BLACK, screen, screen_width // 2, screen_height // 2 - 100, max_width=screen_width - 100)
        draw_text('Cliquez pour commencer le quiz', message_font, DARK_GRAY, screen, screen_width // 2, screen_height // 2 + 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        pygame.display.flip()

# Boucle principale
while True:
    main_menu()
    quiz()
    show_score()
    score = 0
    current_question = 0
