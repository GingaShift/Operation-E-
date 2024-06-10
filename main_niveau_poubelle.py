import pygame
import game_niveau_poubelle
from moviepy.editor import VideoFileClip
def play_video(video_path):
    try:
        clip = VideoFileClip(video_path)
        clip.preview()
    except Exception as e:
        print(f"Error playing video {video_path}: {e}")
pygame.init()

def start_benwars():
    #generer la fenetre de notre jeu
    play_video("video/video_camion_poubelle.mp4")
    pygame.display.set_caption('Ordure')
    screen = pygame.display.set_mode((1080,720))

    background = pygame.image.load('picture_poubelle/bg.jpg')


    game = game_niveau_poubelle.Game()

    running = True
    pygame.mixer.init()
    pygame.mixer.music.load("musique/niveau_poubel.mp3")
    pygame.mixer.music.play(-1)
    while running:

        screen.blit(background,(-854,-324))
        screen.blit(game.gamer.image, game.gamer.rect)
        myfont = pygame.font.SysFont("monospace", 62)
        score_display = myfont.render(str(game.gamer.score)+'/20', 1, (255, 255, 255))
        screen.blit(score_display, (0, 0))

        if game.gamer.health == 5:
            screen.blit(pygame.image.load('picture_poubelle/vie5.png'),(screen.get_width()-264,0))
        elif game.gamer.health == 4:
            screen.blit(pygame.image.load('picture_poubelle/vie4.png'),(screen.get_width()-264,0))
        elif game.gamer.health == 3:
            screen.blit(pygame.image.load('picture_poubelle/vie3.png'),(screen.get_width()-264,0))
        elif game.gamer.health == 2:
            screen.blit(pygame.image.load('picture_poubelle/vie2.png'),(screen.get_width()-264,0))
        elif game.gamer.health == 1:
            screen.blit(pygame.image.load('picture_poubelle/vie1.png'),(screen.get_width()-264,0))

        game.all_dechet.draw(screen)
        game.all_dechet1.draw(screen)
        game.all_dechet2.draw(screen)

        for dechets in game.all_dechet:
            dechets.falling()

        for dechets1 in game.all_dechet1:
            dechets1.falling()

        for dechets2 in game.all_dechet2:
            dechets2.falling()

        if game.pressed.get(pygame.K_RIGHT) and game.gamer.rect.x + game.gamer.rect.width<1080:
            game.gamer.moveright()
        elif game.pressed.get(pygame.K_LEFT) and game.gamer.rect.x>0:
            game.gamer.moveleft()

        pygame.display.flip()
        if game.gamer.score==20:
            running=False
            win = True
        elif game.gamer.health<=0:
            running=False
            win = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                win=False
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_a:
                    game.gamer.type = "marron"
                    game.gamer.upimage()
                elif event.key == pygame.K_z:
                    game.gamer.type = "jaune"
                    game.gamer.upimage()
                elif event.key == pygame.K_e:
                    game.gamer.type = "vert"
                    game.gamer.upimage()
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
    return win