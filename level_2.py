import pygame
import sys

# Initialisation de pygame
pygame.init()

# Configuration de la fenêtre
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Quiz Environnemental')

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
HIGHLIGHT_COLOR = (170, 170, 170)

# Police
font = pygame.font.Font(None, 36)

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
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)


# Fonction principale du quiz
def quiz():
    global score, current_question
    running = True
    while running:
        screen.fill(WHITE)

        # Récupération de la question et des réponses actuelles
        question, answers = questions[current_question]

        # Affichage de la question
        draw_text(question, font, BLACK, screen, screen_width // 2, 100)

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
        for i, (answer, is_correct) in enumerate(answers):
            button_rect = pygame.Rect(screen_width // 4, 200 + i * 60, screen_width // 2, 50)
            button_rects.append(button_rect)
            if button_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, button_rect)
            else:
                pygame.draw.rect(screen, LIGHT_GRAY, button_rect)
            draw_text(answer, font, BLACK, screen, screen_width // 2, 225 + i * 60)

        pygame.display.flip()


# Fonction pour afficher le score final
def show_score():
    running = True
    while running:
        screen.fill(WHITE)

        draw_text(f'Votre score : {score} / {len(questions)}', font, BLACK, screen, screen_width // 2,
                  screen_height // 2)
        draw_text('Cliquez pour recommencer', font, DARK_GRAY, screen, screen_width // 2, screen_height // 2 + 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        pygame.display.flip()


# Boucle principale
while True:
    quiz()
    show_score()
    score = 0
    current_question = 0
