import pygame
import os
import sys
import moviepy.editor
import pygame_menu as pm
user_name = ""
nom_utilisateur = ""
def reset_window_content(screen_game):
    screen_game.fill((0,0,0))
    pygame.display.flip()

def adjust_brightness(image, brightness):
    # Crée une copie de l'image
    adjusted_image = image.copy()
    # Ajuste la luminosité de l'image
    adjusted_image.fill((brightness, brightness, brightness), special_flags=pygame.BLEND_RGB_ADD)
    return adjusted_image

def display_video(video_file, title_text):
    pygame.init()
    video = moviepy.editor.VideoFileClip(video_file)
    video_size = video.size
    screen = pygame.display.set_mode(video_size)
    video.preview()
    pygame.quit()  # Ferme la fenêtre pygame lorsque la vidéo est terminée
def adjust_brightness(image, brightness):
    # Crée une copie de l'image
    adjusted_image = image.copy()
    # Ajuste la luminosité de l'image
    adjusted_image.fill((brightness, brightness, brightness), special_flags=pygame.BLEND_RGB_ADD)
    return adjusted_image

def display_name_entry(screen_game):
    # Créez une nouvelle fenêtre pour la saisie du nom
    name_window = pm.Menu("Enter Your Name (4 letters max)", 800, 600, theme=pm.themes.THEME_DEFAULT)


    # Définissez une variable pour stocker le nom saisi par l'utilisateur
    user_name = [""]  # Utilisez une liste pour stocker le nom afin qu'elle soit mutable dans la fonction

    # Fonction pour enregistrer le nom saisi et passer à la fenêtre principale du jeu
    def save_name():
        user_name[0] = name_input.get_value()  # Récupérer le nom saisi par l'utilisateur
        name_window.disable()  # Désactiver la fenêtre de saisie du nom
        return user_name[0]

    # Ajoutez une zone de texte pour que l'utilisateur saisisse son nom
    name_input = name_window.add.text_input("Name: ", default="", maxchar=10)

    # Ajoutez un bouton "Save" pour enregistrer le nom saisi
    name_window.add.button("Save", save_name)

    # Exécutez le menu de saisie du nom
    name_window.mainloop(screen_game)

    # Retournez le nom saisi par l'utilisateur
    return user_name[0]

def display_info_window(screen_game):
    # Créez une nouvelle fenêtre d'information
    info_window = pygame.Surface((700, 600))

    # Ajoutez un dégradé de couleur au fond
    for y in range(info_window.get_height()):
        color = (0, 0, 80 + y // 6)  # Dégradé allant du bleu foncé au bleu clair vers le bas
        pygame.draw.line(info_window, color, (0, y), (info_window.get_width(), y))

    # Ajoutez une ombre portée à la fenêtre d'information
    pygame.draw.rect(info_window, (0, 0, 0), info_window.get_rect(), 3)  # Bordure noire
    info_window.set_alpha(200)  # Réglez la transparence pour l'ombre portée

    font = pygame.font.SysFont("Rockwell", 24)
    text_credit_game = font.render("Crédit game", True, (255, 255, 255))  # Texte blanc
    info_window.blit(text_credit_game, (280, 20))

    # Ajoutez du texte à la fenêtre
    text = font.render("Crée et designé par Gabriel Lallier, Eden Elfassy\n Alina Frederic et Paul-Emile Bertrand\n Toute copie ou violation de la propriété intellectuelle\n fera l'objet de poursuite", True, (255, 255, 255))  # Texte blanc
    info_window.blit(text, (20, 150))

    # Calculez les coordonnées pour centrer la fenêtre d'information
    window_x = (screen_game.get_width() - info_window.get_width()) // 2
    window_y = (screen_game.get_height() - info_window.get_height()) // 2

    return info_window, window_x, window_y

# Ajout DE
def display_settings_window(screen_game):
    import pygame
    import pygame_menu as pm

    pygame.init()

    # Screen
    WIDTH, HEIGHT = 700, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Standard RGB colors
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 100, 100)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Main function of the program

    def main():
        # List that is displayed while selecting the graphics level
        graphics = [("Low", "low"),
                    ("Medium", "medium"),
                    ("High", "high"),
                    ("Ultra High", "ultra high")]

        # List that is displayed while selecting the window resolution level
        resolution = [("1920x1080", "1920x1080"),
                      ("1920x1200", "1920x1200"),
                      ("1280x720", "1280x720"),
                      ("2560x1440", "2560x1440"),
                      ("3840x2160", "3840x2160")]

        # List that is displayed while selecting the difficulty
        difficulty = [("Easy", "Easy"),
                      ("Medium", "Medium"),
                      ("Expert", "Expert")]

        # List that is displayed while selecting the player's perspective
        perspectives = [("FPP", "fpp"),
                        ("TPP", "tpp")]

        # This function displays the currently selected options

        def printSettings():
            print("\n\n")
            # getting the data using "get_input_data" method of the Menu class
            settingsData = settings.get_input_data()

            for key in settingsData.keys():
                print(f"{key}\t:\t{settingsData[key]}")

            # Creating the settings menu

        settings = pm.Menu(title="Settings",
                           width=WIDTH,
                           height=HEIGHT,
                           theme=pm.themes.THEME_DEFAULT)

        # Adjusting the default values
        settings._theme.widget_font_size = 25
        settings._theme.widget_font_color = BLACK
        settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

        # Text input that takes in the username
        settings.add.text_input(title="User Name : ", textinput_id="username")

        # 2 different Drop-downs to select the graphics level and the resolution level
        settings.add.dropselect(title="Graphics Level", items=graphics,
                                dropselect_id="graphics level", default=0)
        settings.add.dropselect_multiple(title="Window Resolution", items=resolution,
                                         dropselect_multiple_id="Resolution",
                                         open_middle=True, max_selected=1,
                                         selection_box_height=6)

        # Toggle switches to turn on/off the music and sound
        settings.add.toggle_switch(
            title="Muisc", default=True, toggleswitch_id="music")
        settings.add.toggle_switch(
            title="Sounds", default=False, toggleswitch_id="sound")

        # Selector to choose between the types of difficulties available
        settings.add.selector(title="Difficulty\t", items=difficulty,
                              selector_id="difficulty", default=0)

        # Range slider that lets to choose a value using a slider
        settings.add.range_slider(title="FOV", default=60, range_values=(
            50, 100), increment=1, value_format=lambda x: str(int(x)), rangeslider_id="fov")

        # Fancy selector (style added to the default selector) to choose between
        # first person and third person perspectives
        settings.add.selector(title="Perspective", items=perspectives,
                              default=0, style="fancy", selector_id="perspective")

        # clock that displays the current date and time
        settings.add.clock(clock_format="%d-%m-%y %H:%M:%S",
                           title_format="Local Time : {0}")

        # 3 different buttons each with a different style and purpose
        settings.add.button(title="Print Settings", action=printSettings,
                            font_color=WHITE, background_color=GREEN)
        settings.add.button(title="Restore Defaults", action=settings.reset_value,
                            font_color=WHITE, background_color=RED)
        settings.add.button(title="Return To Main Menu",
                            action=pm.events.BACK, align=pm.locals.ALIGN_CENTER)

        # Creating the main menu
        mainMenu = pm.Menu(title="Main Menu",
                           width=WIDTH,
                           height=HEIGHT,
                           theme=pm.themes.THEME_DEFAULT)

        # Adjusting the default values
        mainMenu._theme.widget_alignment = pm.locals.ALIGN_CENTER

        # Button that takes to the settings menu when clicked
        mainMenu.add.button(title="Settings", action=settings,
                            font_color=WHITE, background_color=GREEN)

        # An empty label that is used to add a seperation between the two buttons
        mainMenu.add.label(title="")

        # Exit button that is used to terminate the program
        mainMenu.add.button(title="Exit", action=pm.events.EXIT,
                            font_color=WHITE, background_color=RED)

        # Lets us loop the main menu on the screen
        mainMenu.mainloop(screen)

    if __name__ == "__main__":
        main()


def display_image(image_file, title_text,):

    import pygame
    global user_name
    pygame.init()
    screen_game = pygame.display.set_mode((1200, 800))
    image = pygame.image.load(image_file).convert_alpha()
    os.environ['SDL_VIDEO_CENTERED'] = '1'



    # Chargement de l'image pour le bouton "info"
    info_button = pygame.image.load("info.png").convert_alpha()
    info_button = pygame.transform.scale(info_button, (100, 100))
    info_button_rect = info_button.get_rect()
    info_button_rect.center = (1100, 710)

    button_info_hover = False
    button_info_clicked = False
    info_window_open = False
    info_window_surface = None

    # Ajout DE:
    window_settings_open = False
    window_settings_surface = None
    window_entry_name_close = False
    text_x = 0
    text_y = 0
    scroll_speed = 0

    # Fin Ajout DE

    # Chargement de l'image pour le bouton "settings"
    settings_button = pygame.image.load("settings.png").convert_alpha()
    settings_button = pygame.transform.scale(settings_button, (100, 100))
    settings_button_rect = settings_button.get_rect()
    settings_button_rect.center = (100, 710)

    play_font = pygame.image.load("play.png").convert_alpha()
    play_font = pygame.transform.scale(play_font,(400,130))
    play_font_rect = play_font.get_rect()
    play_font_rect.center = (600,400)

    quit_font = pygame.image.load("Quit.png").convert_alpha()
    quit_font = pygame.transform.scale(quit_font,(400,180))
    quit_font_rect = play_font.get_rect()
    quit_font_rect.center = (600,530)

    return_font = pygame.image.load("return_arrow.png").convert_alpha()
    return_font = pygame.transform.scale(return_font, (200, 200))
    return_font_rect = return_font.get_rect()
    return_font_rect.center = (200, 200)

    level_1_font = pygame.image.load("level_1.png").convert_alpha()
    level_1_font = pygame.transform.scale(level_1_font,(200,200))
    level_1_font_rect = level_1_font.get_rect()
    level_1_font_rect.center = (500,200)

    level_2_font = pygame.image.load("level_2.png").convert_alpha()
    level_2_font = pygame.transform.scale(level_2_font, (200, 200))
    level_2_font_rect = level_2_font.get_rect()
    level_2_font_rect.center = (700, 500)

    level_3_font = pygame.image.load("level_3.png").convert_alpha()
    level_3_font = pygame.transform.scale(level_3_font, (200, 200))
    level_3_font_rect = level_3_font.get_rect()
    level_3_font_rect.center = (800, 300)

    level_4_font = pygame.image.load("level_4.png").convert_alpha()
    level_4_font = pygame.transform.scale(level_4_font, (200, 200))
    level_4_font_rect = level_4_font.get_rect()
    level_4_font_rect.center = (1000, 200)

    button_hover = False
    button_clicked = False

    # Créer un objet font


    # Surface pour le contenu à afficher lorsque le bouton "info" est cliqué
    new_content_surface = pygame.Surface((800, 600))
    new_content_surface.fill((255, 255, 255))  # Remplir avec une couleur de fond blanche par défaut
    if not user_name:
        user_name = display_name_entry(screen_game)

        window_entry_name_close = True

    pygame.mixer.init()
    pygame.mixer.music.load("son_operationE.mp3")
    pygame.mixer.music.play(-1)

    button_hover_play = False
    button_hover_quit = False
    settings_menu_open = False
    game_playing = False
    button_state_return = False
    button_hover_level_1 = False
    button_hover_level_2 = False
    button_hover_level_3 = False
    button_hover_level_4 = False

    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.MOUSEMOTION:
                if level_1_font_rect.collidepoint(event.pos):
                    button_hover_level_1 = True
                else :
                    button_hover_level_1 = False

                if level_2_font_rect.collidepoint(event.pos):
                    button_hover_level_2 = True
                else :
                    button_hover_level_2 = False

                if level_3_font_rect.collidepoint(event.pos):
                    button_hover_level_3 = True
                else :
                    button_hover_level_3 = False

                if level_4_font_rect.collidepoint(event.pos):
                    button_hover_level_4 = True
                else :
                    button_hover_level_4 = False

                if return_font_rect.collidepoint(event.pos):
                    button_state_return = True
                else :
                    button_state_return = False

                if play_font_rect.collidepoint(event.pos):

                    button_hover_play = True
                else :
                    button_hover_play = False

                if quit_font_rect.collidepoint(event.pos):
                    button_hover_quit = True
                else :
                    button_hover_quit = False
                if settings_button_rect.collidepoint(event.pos):
                    button_hover = True
                else:
                    button_hover = False

                if info_button_rect.collidepoint(event.pos):
                    button_info_hover = True
                else:
                    button_info_hover = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_font_rect.collidepoint(event.pos):
                    pygame.mixer.Sound("son_play.mp3").play()
                    reset_window_content(screen_game)
                    image = pygame.image.load("galaxy.jpg").convert()
                    screen_game.blit(image, (0,0))
                    pygame.display.flip()
                    game_playing = True
                    play_font_rect.center = (-100, -100)
                    quit_font_rect.center = (-100, -100)

                    if not user_name:
                        user_name = display_name_entry(screen_game)

                if quit_font_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    play_font_rect.center = (-100, -100)
                    quit_font_rect.center = (-100, -100)

                if return_font_rect.collidepoint(event.pos):
                    game_playing = False


                if settings_button_rect.collidepoint(event.pos):
                    settings_menu_open = True
                else:
                    settings_menu_open = False


                if info_button_rect.collidepoint(event.pos):
                    if info_window_open:  # Si la fenêtre d'information est déjà ouverte
                        info_window_open = False  # Ferme la fenêtre d'information
                    else:
                        info_window_surface, window_x, window_y = display_info_window(screen_game)
                        info_window_open = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if settings_button_rect.collidepoint(event.pos):
                    if button_clicked:
                        print("Settings Button clicked !")
                        button_clicked = False
                if info_button_rect.collidepoint(event.pos):
                    if button_info_clicked:
                        print("Info Button clicked !")
                        button_info_clicked = False

        screen_game.blit(image, (0, 0))  # Dessiner l'image de fond
        if not game_playing :
            play_font_rect.center = (600, 400)
            quit_font_rect.center = (600, 530)

            if button_hover:
                screen_game.blit(adjust_brightness(settings_button, 50), settings_button_rect)  # Ajuste la luminosité du bouton pour la surbrillance
            else:
                screen_game.blit(settings_button, settings_button_rect)

            if button_info_hover:
                screen_game.blit(adjust_brightness(info_button, 50), info_button_rect)  # Ajuste la luminosité du bouton pour la surbrillance
            else:
                screen_game.blit(info_button, info_button_rect)

            if button_hover_play:
                screen_game.blit(adjust_brightness(play_font, 50), play_font_rect)  # Bouton en surbrillance
            else:
                screen_game.blit(play_font, play_font_rect)  # Bouton normal

            # Dessiner le bouton "Quit"
            if button_hover_quit:
                screen_game.blit(adjust_brightness(quit_font, 50), quit_font_rect)  # Bouton en surbrillance
            else:
                screen_game.blit(quit_font, quit_font_rect)

            if settings_menu_open:
                display_settings_window(screen_game)

            if window_entry_name_close == False and info_window_open == False:
                text_x -= scroll_speed
                if text_x < -text_surface.get_width():
                    text_x = 800
                screen_game.blit(text_surface, (text_x, text_y))  # Dessiner le titre animé

            # Ajout DE
            # des la fermeture de la fenetre permettant à user d'entrer son nom:
            if window_entry_name_close == True and info_window_open == False:

                if len(user_name) == 0:
                    nom_utilisateur = "Nom bidon"
                else:
                    nom_utilisateur = user_name[0] + user_name[1] + user_name[2] + user_name[3]
                texte_complet = "Operation E" + " - User = " + nom_utilisateur
                font = pygame.font.SysFont("Rockwell", 150)
                text_surface = font.render(texte_complet, True, (192, 192, 192))

                text_x = 800
                text_y = 100
                scroll_speed = 2

                screen_game.blit(text_surface, (text_x, text_y))  # Dessiner le titre animé

                window_entry_name_close = False

            # Fin ajout DE

            # Afficher la nouvelle surface du contenu si le bouton "info" a été cliqué
            if info_window_open:
                screen_game.blit(info_window_surface, (window_x, window_y))  # Dessiner la fenêtre d'information sur l'écran principal

        # Ajout DE
            if window_settings_open:
                screen_game.blit(window_settings_surface,(window_x, window_y))
        # Dessiner la fenêtre d'information sur l'écran principal
            # Fin ajout DE

        else :
            if game_playing:
                if button_state_return :
                    screen_game.blit(adjust_brightness(return_font,50),return_font_rect)

                else :
                    screen_game.blit(return_font,return_font_rect)

                if button_hover_level_1:
                    screen_game.blit(adjust_brightness(level_1_font,50),level_1_font_rect)
                else :
                    screen_game.blit(level_1_font, level_1_font_rect)

                if button_hover_level_2 :
                    screen_game.blit(adjust_brightness(level_2_font,50),level_2_font_rect)
                else :
                    screen_game.blit(level_2_font, level_2_font_rect)

                if button_hover_level_3 :
                    screen_game.blit(adjust_brightness(level_3_font,50),level_3_font_rect)
                else :
                    screen_game.blit(level_3_font, level_3_font_rect)

                if button_hover_level_4:
                    screen_game.blit(adjust_brightness(level_4_font,50),level_4_font_rect)
                else :
                    screen_game.blit(level_4_font,level_4_font_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

display_video("video.mp4","NeoNovaStudios")
# Afficher la seconde fenêtre avec une image


#nom_utilisateur = ""
#def chaine_qui_defile(title_text):
#    font = pygame.font.SysFont("Rockwell", 150)
#    text_surface = font.render(title_text, True, (192, 192, 192))

#    text_x = 800
#    text_y = 100
#    scroll_speed = 2

display_image("galaxy.jpg", f"Operation - E ; user:" + nom_utilisateur)


# Utiliser split pour diviser la chaîne en mots
# mots = user_name[0].split()

# Maintenant, mots est une liste contenant tous les mots dans la chaîne. On prend le premier.
# premier_mot = mots[0]


pygame.quit()
sys.exit()
