import sys
import time

import pygame

from world_elements.level import Level
from level_loader import LevelLoader
from world_elements.hero import Hero
from world_elements.platform import Platform
from world_elements.foe import Foe
from world_elements.flag import Flag

TMP_JUMP_HEIGHT = 10
TMP_HERO_HORIZONTAL_STEP = 1

def is_over_start_button(pos):
    if(pos[0] > 290 and pos[0]< 390):
        if(pos[1] >300 and pos[1] <340):
            return True
    return False

def is_over_quit_button(pos):
    if(pos[0] > 510 and pos[0]< 610):
        if(pos[1] >300 and pos[1] <340):
            return True
    return False

def game_intro(screen):
    intro = True
    title = pygame.image.load(r"C:\Users\Svatopluk\PycharmProjects\Python-project--master\src\img\basic\title.png")
    while (intro):

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (is_over_start_button(pos)):
                    intro = False
                if(is_over_quit_button(pos)):
                    pygame.quit()
                    quit()

        screen.blit(title, (250, 0))

        font = pygame.font.SysFont('comicsans', 60)
        text1 = font.render("Start", 1, (0, 0, 0))
        text2 = font.render("Quit", 1, (0, 0, 0))

        pygame.draw.rect(screen, (120, 230, 120), (290, 300, 100, 40))
        screen.blit(text1, (290, 300))

        pygame.draw.rect(screen, (230, 0, 50), (510, 300, 100, 40))
        screen.blit(text2, (510, 300))
        pygame.display.update()

def main():
    pygame.init()

    screen_size = (920, 520)
    screen = pygame.display.set_mode(screen_size)

    game_intro(screen)

    object_list = LevelLoader("../Resources/test").load_level()

    first_level = Level(object_list)

    manfred = Hero(first_level)

    baron_r_img = pygame.image.load(r"C:\Users\Svatopluk\PycharmProjects\Python-project--master\img\basic\baron_r.png")
    baron_l_img = pygame.image.load(r"C:\Users\Svatopluk\PycharmProjects\Python-project--master\img\basic\baron_l.png")


    platform_img = pygame.image.load(r"C:\Users\Svatopluk\PycharmProjects\Python-project--master\img\basic\platforma.png")

    foe_flag_img = pygame.image.load(r"C:\Users\Svatopluk\PycharmProjects\Python-project--master\img\basic\foe_flag.png")
    baron_flag_img = pygame.image.load(r"C:\Users\Svatopluk\PycharmProjects\Python-project--master\img\basic\baron_flag.png")
    bullet_img = pygame.image.load(r"C:\Users\Svatopluk\PycharmProjects\Python-project--master\img\basic\patron.png")

    foe_img = pygame.image.load(r"C:\Users\Svatopluk\PycharmProjects\Python-project--master\img\basic\foe.png")

    ax = 0
    while (True):
        ay = 0
        for event in pygame.event.get():
            if (event.type == pygame.KEYUP):
                ax = 0
            if (event.type == pygame.QUIT):
                sys.exit(0)
            elif (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_RIGHT):
                    ax = TMP_HERO_HORIZONTAL_STEP
                    manfred.right_direction()

                if (event.key == pygame.K_LEFT):
                    ax = -TMP_HERO_HORIZONTAL_STEP
                    manfred.left_direction()

                if (event.key == pygame.K_UP):
                    ay = -TMP_JUMP_HEIGHT
                    manfred.is_jumping = True
                if(event.key == pygame.K_SPACE):
                    manfred.shoot()


        screen.fill((0, 0, 0))

        for object in first_level.objects:
            if(isinstance(object, Platform)):
                img = platform_img
            elif(isinstance(object, Flag)):
                if(not object.captured):
                    img = foe_flag_img
                else:
                    img = baron_flag_img
            elif(isinstance(object, Foe)):
                img = foe_img
            screen.blit(img, (object.position_on_screen(int(manfred.position.x))*4+40, int(object.position.y)*4-20))

        for bullet in first_level.bullets_list:
            screen.blit(bullet_img, (int(bullet.position_on_screen(manfred.position.x)*4+40), int(bullet.position.y)*4-20))

        first_level.move_bullets()

        manfred.accelerate(ax, ay)
        manfred.update()

        baron_pos = (160, int(manfred.position.y)*4 - 20)

        if (manfred.is_in_right_direction()):
            screen.blit(baron_r_img, baron_pos)
        else:
            screen.blit(baron_l_img, baron_pos)


        #print(first_level.hero.spawn.position)

        pygame.display.flip()
        time.sleep(0.08)


if (__name__ == "__main__"):
    main()
