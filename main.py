import pygame
import sys
import os
import pickle
import math

PATH = __file__[:-7]

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 480))

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

stone = pygame.image.load(os.path.join(PATH+"\\grafik", "stone.png"))

player_last = 0
player_hp = 3

player_y_pos = 0
player_x_pos = 0

fiende_y_pos = 300
fiende_x_pos = 300

with open(f'{PATH}Map.dat', 'rb') as file:
    MapData = pickle.load(file)

pygame.mouse.set_visible(1)
pygame.display.set_caption('My game')

movment = [False, False, False, False] # w, d, s, a
ability = [False]
attack = [False]
images = [stone]
while True:
    #print(fiende_x_pos, player_x_pos)

    clock.tick(60)

    screen.blit(bg, (0, 0))

    #print(player_y_pos, player_x_pos)
    #print(pygame.key.get_mods())

    x, y = pygame.mouse.get_pos()


    for entity in MapData:
        screen.blit(images[entity[0]], (entity[1][0] - player_x_pos + 252, entity[1][1] - player_y_pos + 192))

    # fiende
    screen.blit(fiende, (fiende_x_pos - player_x_pos + 252, fiende_y_pos - player_y_pos + 192))
    if math.fabs(player_x_pos - fiende_x_pos) < 300 and math.fabs(player_y_pos - fiende_y_pos) < 300:
        if fiende_x_pos > player_x_pos:
            fiende_x_pos = fiende_x_pos - 2
        if fiende_x_pos < player_x_pos:
            fiende_x_pos = fiende_x_pos + 2

        if fiende_y_pos > player_y_pos:
            fiende_y_pos = fiende_y_pos - 2
        if fiende_y_pos < player_y_pos:
            fiende_y_pos = fiende_y_pos + 2

    # hp
    if player_hp <= 3:
        screen.blit(hp, (70, 10))
    if player_hp <= 2:
        screen.blit(hp, (40, 10))
    if player_hp <= 1:
        screen.blit(hp, (10, 10))

    if fiende_x_pos == player_x_pos and fiende_y_pos == player_y_pos:
        player_hp = player_hp - 1
        print(player_hp)

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
        if player_last == 1:
            screen.blit(sword_slash_right, (348, 192))
        if player_last == 2:
            screen.blit(sword_slash_down, (252, 288))
        if player_last == 3:
            screen.blit(sword_slash_left, (156, 192))


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





    pygame.display.update()