import pygame
import game_final
import random
pygame.init()
from moviepy.editor import VideoFileClip
def play_video(video_path):
    try:
        clip = VideoFileClip(video_path)
        clip.preview()
    except Exception as e:
        print(f"Error playing video {video_path}: {e}")
pygame.init()

def start_final(vol):


    play_video('video/final_step.mp4')
    pygame.mixer.init()
    s= pygame.mixer.Sound("musique/finalemusique.mp3")
    s.set_volume(vol)
    s.play(-1)
    pygame.display.set_caption('Finale task')
    screen = pygame.display.set_mode((1080,810))
    game= game_final.Game()
    player= game.player
    running=True
    background = pygame.image.load('Asset_final/bg.png')
    background = pygame.transform.scale(background,(1080,810))
    deb=0

    while running and player.health>0:

        screen.blit(background,(0,0))


        game.all_wobj.draw(screen)
        game.all_robj.draw(screen)

        for i in range(game.max_time):
            game.update_health_bar(screen)

        if deb==0:
            type = random.choice(['badcar','second','piggy','garbage','waterman'])
            cr =(random.choice([35,305,575,845]),random.choice([35,305,575]))
            game.spawn_robj(type,cr[0],cr[1])
            cw = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
            cw2 = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
            while cw == cr or cw == cw2 or cr == cw2:
                cw = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
                cw2 = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
            game.spawn_wobj(type, cw[0], cw[1])
            game.spawn_wobj(type, cw2[0], cw2[1])
            deb+=1
        elif (pygame.Surface.get_at(screen,(1034,775)) == (111, 210, 46, 255) or (len(game.all_robj)+ len(game.all_wobj) <3 )) and deb > 0 and deb <= 10:
            if pygame.Surface.get_at(screen,(1034,775)) == (111, 210, 46, 255):
                game.player.health-=1
            for wobj in game.all_wobj:
                wobj.removerest()
            for robj in game.all_robj:
                robj.removerest()
            type = random.choice(['badcar', 'second', 'piggy', 'garbage', 'waterman'])
            cr = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
            game.spawn_robj(type, cr[0], cr[1])
            cw = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
            cw2 = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
            while cw == cr or cw == cw2 or cr == cw2:
                cw = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
                cw2 = (random.choice([35, 305, 575, 845]), random.choice([35, 305, 575]))
            game.spawn_wobj(type, cw[0], cw[1])
            game.spawn_wobj(type, cw2[0], cw2[1])
            deb += 1
        elif deb == 11:
            running = False
        screen.blit(player.image, player.rect)
        if player.health == 3:
            screen.blit(pygame.image.load('Asset_final/vie3.png'),(0,0))
        elif player.health == 2:
            screen.blit(pygame.image.load('Asset_final/vie2.png'),(0,0))
        else:
            screen.blit(pygame.image.load('Asset_final/vie1.png'),(0,0))


        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
            game.player.move_right()
        elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
            game.player.move_left()
        elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
            game.player.move_up()
        elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
            game.player.move_down()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE and (game.check_collision(game.player, game.all_robj) or game.check_collision(game.player, game.all_wobj)):
                    for wobj in game.all_wobj:
                        wobj.remove(screen)
                        wobj.removerest()
                    for robj in game.all_robj:
                        robj.remove(screen)
                        robj.removerest()
                    game.time=game.max_time
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
    pygame.mixer.quit()
    if player.health>0 and deb >10:
        return True
    else:
        return False