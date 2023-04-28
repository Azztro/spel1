import pygame
import sys
import os
import pickle
import math


def collides(obect_1_x_pos, obect_1_y_pos, obect_2_x_pos, obect_2_y_pos):
    if (obect_1_x_pos + 96 >= obect_2_x_pos and (obect_1_x_pos - 96 <= obect_2_x_pos)\
        and (obect_1_y_pos + 96 >= obect_2_y_pos) and (obect_1_y_pos - 96 <= obect_2_y_pos)\
        or obect_1_x_pos - 96 <= obect_2_x_pos and (obect_1_x_pos + 96 >= obect_2_x_pos)\
        and (obect_1_y_pos + 96 >= obect_2_y_pos) and (obect_1_y_pos - 96 <= obect_2_y_pos)\
        and obect_1_y_pos + 96 >= obect_2_y_pos and (obect_1_y_pos - 96 <= obect_2_y_pos)\
        and (obect_1_x_pos + 96 >= obect_2_x_pos) and (obect_1_x_pos - 96 <= obect_2_x_pos)\
        or obect_1_y_pos - 96 <= obect_2_y_pos and (obect_1_y_pos + 96 >= obect_2_y_pos)\
        and (obect_1_x_pos - 96 <= obect_2_x_pos) and (obect_1_x_pos + 96 >= obect_2_x_pos)) and tid > 60:
        return True
    else:
        return False
PATH = __file__[:-7]

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 480))
Gameover = pygame.image.load(os.path.join(PATH+"\\grafik", "Game over.png"))

bg = pygame.image.load(os.path.join(PATH+"\\grafik", "Namnlös.png"))
player_right = pygame.image.load(os.path.join(PATH+"\\grafik", "gubbe_right.png"))
player_left = pygame.image.load(os.path.join(PATH+"\\grafik", "gubbe_left.png"))
player_upp = pygame.image.load(os.path.join(PATH+"\\grafik", "gubbe_upp.png"))
player_down = pygame.image.load(os.path.join(PATH+"\\grafik", "gubbe_down.png"))
hp = pygame.image.load(os.path.join(PATH+"\\grafik", "hp.png"))


fiende = pygame.image.load(os.path.join(PATH+"\\grafik", "fiende.png"))

sword_slash_upp = pygame.image.load(os.path.join(PATH+"\\grafik", "sword_slash_upp.png"))
sword_slash_right = pygame.image.load(os.path.join(PATH+"\\grafik", "sword_slash_right.png"))
sword_slash_down = pygame.image.load(os.path.join(PATH+"\\grafik", "sword_slash_down.png"))
sword_slash_left = pygame.image.load(os.path.join(PATH+"\\grafik", "sword_slash_left.png"))
sword_x_pos = 0
sword_y_pos = 0

stone = pygame.image.load(os.path.join(PATH+"\\grafik", "stone.png"))

player_last = 0
player_hp = 3

fiende_hp = 3

player_y_pos = 0
player_x_pos = 0

fiende_y_pos = 300
fiende_x_pos = 300

with open(f'{PATH}Map.dat', 'rb') as file:
    MapData = pickle.load(file)

pygame.mouse.set_visible(1)
pygame.display.set_caption('My game')

tid = 0

movment = [False, False, False, False] # w, d, s, a
ability = [False]
attack = [False]
images = [stone]
while True:
    #print(fiende_x_pos, player_x_pos)
    #print('sword',sword_x_pos, sword_y_pos)
    #print('fiende', fiende_x_pos, fiende_y_pos)

    clock.tick(60)
    tid = tid + 1

    screen.blit(bg, (0, 0))

    #print(player_y_pos, player_x_pos)
    #print(pygame.key.get_mods())

    x, y = pygame.mouse.get_pos()


    for entity in MapData:
        screen.blit(images[entity[0]], (entity[1][0] - player_x_pos + 252, entity[1][1] - player_y_pos + 192))

        if player_x_pos + 100 >= entity[1][0] and (player_x_pos - 96 <= entity[1][0]) and (player_y_pos + 96 >= entity[1][1]) and (player_y_pos - 96 <= entity[1][1]):
            movment[1] = False
        if player_x_pos - 100 <= entity[1][0] and (player_x_pos + 95 >= entity[1][0]) and (player_y_pos + 96 >= entity[1][1]) and (player_y_pos - 96 <= entity[1][1]):
            movment[3] = False
        if player_y_pos + 96 >= entity[1][1] and (player_y_pos - 100 <= entity[1][1]) and (player_x_pos + 96 >= entity[1][0]) and (player_x_pos - 96 <= entity[1][0]):
            movment[0] = False
        if player_y_pos - 96 <= entity[1][1] and (player_y_pos + 100 >= entity[1][1]) and (player_x_pos - 96 <= entity[1][0]) and (player_x_pos + 96 >= entity[1][0]):
            movment[2] = False

    # fiende
    if fiende_hp > 0:
        screen.blit(fiende, (fiende_x_pos - player_x_pos + 252, fiende_y_pos - player_y_pos + 192))
        if (math.fabs(player_x_pos - fiende_x_pos) < 300 and math.fabs(player_y_pos - fiende_y_pos) < 300) and fiende_hp > 0:
            if fiende_x_pos > player_x_pos:
                fiende_x_pos = fiende_x_pos - 2
            if fiende_x_pos < player_x_pos:
                fiende_x_pos = fiende_x_pos + 2

            if fiende_y_pos > player_y_pos:
                fiende_y_pos = fiende_y_pos - 2
            if fiende_y_pos < player_y_pos:
                fiende_y_pos = fiende_y_pos + 2

    # hp
    if player_hp >= 1:
        screen.blit(hp, (10, 10))
    if player_hp >= 2:
        screen.blit(hp, (40, 10))
    if player_hp >= 3:
        screen.blit(hp, (70, 10))

    if (collides(player_x_pos, player_y_pos, fiende_x_pos, fiende_y_pos)) and fiende_hp > 0:
        player_hp = player_hp - 1
        #print(player_hp)
        print(player_x_pos,player_y_pos,fiende_x_pos,fiende_y_pos)
        tid = 0

    if (collides(sword_x_pos, sword_y_pos, fiende_x_pos, fiende_y_pos)) and tid > 100:
        fiende_hp = fiende_hp - 1
        print('hp',fiende_hp)
        print(sword_x_pos, sword_y_pos, fiende_x_pos, fiende_y_pos)
        tid = 0


    # player
    if movment[0] == True:
        player_y_pos = player_y_pos - 5
        screen.blit(player_upp, (252, 192))
        player_last = 0
    if movment[1] == True:
        player_x_pos = player_x_pos + 5
        screen.blit(player_right, (252, 192))
        player_last = 1
    if movment[2] == True:
        player_y_pos = player_y_pos + 5
        screen.blit(player_down, (252, 192))
        player_last = 2
    if movment[3] == True:
        player_x_pos = player_x_pos - 5
        screen.blit(player_left, (252, 192))
        player_last = 3

    if attack[0] == True:
        if player_last == 0:
            screen.blit(sword_slash_upp, (252, 96))
            sword_x_pos = player_x_pos
            sword_y_pos = player_y_pos + 96
        if player_last == 1:
            screen.blit(sword_slash_right, (348, 192))
            sword_x_pos = player_x_pos + 96
            sword_y_pos = player_y_pos
        if player_last == 2:
            screen.blit(sword_slash_down, (252, 288))
            sword_x_pos = player_x_pos
            sword_y_pos = player_y_pos - 96
        if player_last == 3:
            screen.blit(sword_slash_left, (156, 192))
            sword_x_pos = player_x_pos - 96
            sword_y_pos = player_y_pos


#ability
    if (movment[0] == True) and (ability[0] == True):
        player_y_pos = player_y_pos + 15
    if (movment[1] == True) and (ability[0] == True):
        player_x_pos = player_x_pos - 15
    if (movment[2] == True) and (ability[0] == True):
        player_y_pos = player_y_pos - 15
    if (movment[3] == True) and (ability[0] == True):
        player_x_pos = player_x_pos + 15



    if (not movment[0]) and not (movment[1]) and (not movment[2]) and (not movment[3]):
        if player_last == 0:
            screen.blit(player_upp, (252, 192))
        if player_last == 1:
            screen.blit(player_right, (252, 192))
        if player_last == 2:
            screen.blit(player_down, (252, 192))
        if player_last == 3:
            screen.blit(player_left, (252, 192))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()
#movment
        if event.type == 768:
            if event.unicode == 'w':
                movment[0] = True
            elif event.unicode == 'd':
                movment[1] = True
            elif event.unicode == 's':
                movment[2] = True
            elif event.unicode == 'a':
                movment[3] = True
#movment
        elif event.type == 769:
            if event.unicode == 'w':
                movment[0] = False
            elif event.unicode == 'd':
                movment[1] = False
            elif event.unicode == 's':
                movment[2] = False
            elif event.unicode == 'a':
                movment[3] = False

        if event.type == 768:
            if event.unicode == 'e':
                attack[0] = True

        elif event.type == 769:
            if event.unicode == 'e':
                attack[0] = False

#ability
        if event.type == 768:
            if event.key == 1073742049:  # SHIFT = 1073742049
                ability[0] = True

        elif event.type == 769:
            if event.key == 1073742049:
                ability[0] = False

    if player_hp <= 0:
        screen.blit(Gameover,(0,0))
        movment[0], movment[1], movment[2], movment[3] = False, False, False, False



    pygame.display.update()