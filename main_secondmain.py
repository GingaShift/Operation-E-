import pygame
import games
pygame.init()
from moviepy.editor import VideoFileClip
def play_video(video_path):
    try:
        clip = VideoFileClip(video_path)
        clip.preview()
    except Exception as e:
        print(f"Error playing video {video_path}: {e}")
def starting_secondhand():
    play_video("video_secondhand.mp4")
    pygame.display.set_caption("Seconde main")
    screen = pygame.display.set_mode((1080,720))

    background = pygame.image.load('pictures/bg.jpg')

    game= games.Game()

    running=True

    pygame.mixer.init()
    pygame.mixer.music.load("niveau_secondemain.mp3")
    pygame.mixer.music.play(-1)

    while running and game.gamer.health>0 and game.gamer.score < 250:

        screen.blit(background, (-570,-140))
        screen.blit(game.gamer.image, game.gamer.rect)

        myfont = pygame.font.SysFont("monospace", 62)
        score_display = myfont.render(str(game.gamer.score), 1, (0, 0, 0))
        screen.blit(score_display, (0, 0))

        game.gamer.update_health_bar(screen)

        for projectile in game.gamer.all_projectiles:
            projectile.move()

        for vetn in game.all_vetneufs:
            vetn.forward()
            vetn.update_health_bar(screen)

        for veto in game.all_vetold:
            veto.forward()

        for obs_etg in game.all_obs:
            obs_etg.forward()

        game.gamer.all_projectiles.draw(screen)

        game.all_vetneufs.draw(screen)
        game.all_vetold.draw(screen)
        game.all_obs.draw(screen)

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

                if event.key == pygame.K_SPACE:
                    game.gamer.launch_projectile()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
    if game.gamer.health<=0:
        return False
    elif game.gamer.score >= 250:
        return True