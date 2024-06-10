import pygame
import games_elec
from moviepy.editor import VideoFileClip
pygame.init()

def play_video(video_path):
    try:
        clip = VideoFileClip(video_path)
        clip.preview()
    except Exception as e:
        print(f"Error playing video {video_path}: {e}")
pygame.init()

def starting_eleco(vol):
    play_video('video/eleco.mp4')
    pygame.mixer.init()
    s = pygame.mixer.Sound("musique/niveau_secondemain.mp3")
    s.set_volume(vol)
    s.play(-1)
    pygame.display.set_caption("Boss elec")
    screen = pygame.display.set_mode((1080, 720))

    background = pygame.image.load('Boss_elec/stage.png')

    game = games_elec.Game()
    game.screen = screen  # Ajouter référence à l'écran dans le jeu

    running = True

    while running:
        screen.blit(background, (0,0))
        screen.blit(game.gamer.image, game.gamer.rect)

        game.gamer.update_health_bar(screen)
        game.boss.update_health_bar(screen)

        # Afficher le boss
        screen.blit(game.boss.image, game.boss.rect)
        game.boss.forward()

        # Faire avancer les éclairs
        for eclair in game.all_vetold:
            eclair.forward()

        game.all_vetold.draw(screen)

        if game.pressed.get(pygame.K_RIGHT) and game.gamer.rect.x + game.gamer.rect.width < screen.get_width():
            game.gamer.move_right()
        elif game.pressed.get(pygame.K_LEFT) and game.gamer.rect.x > 0:
            game.gamer.move_left()
        elif game.pressed.get(pygame.K_UP) and game.gamer.rect.y > 0:
            game.gamer.move_up()
        elif game.pressed.get(pygame.K_DOWN) and game.gamer.rect.y + game.gamer.rect.height < screen.get_height():
            game.gamer.move_down()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

            elif event.type == game.eclair_timer:
                game.spawn_vetold()  # Faire apparaître un nouvel éclair

        # Vérification des conditions de fin de jeu
        if game.gamer.health <= 0 or game.boss.health <= 0:
            running = False

    # Afficher le résultat final
    pygame.mixer.quit()
    if game.gamer.health <= 0:
        return False
    elif game.boss.health <= 0:
        return True