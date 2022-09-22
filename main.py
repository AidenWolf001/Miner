import pygame
import sys
import math
from pygame.locals import *

import mathcore

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (233, 233, 232)

points = [(200, 175), (300, 125), (400, 175), (450, 125), (450, 225), (400, 175), (300, 225)]

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Miner")

clock = pygame.time.Clock()


def display_word(screen, word, x, y):
    font = pygame.font.Font('simhei.ttf', 20)
    font_surface = font.render(str(word), True, 'white')
    screen.blit(font_surface, (x, y))


def display_block(color, x, y):
    pygame.draw.rect(screen, color, (x, y, x + 20, y + 20), 2)

Mine = mathcore.Minefield()
field_list = Mine.field_list
print(field_list)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(WHITE)


    for i in range(Mine.field_size[1]):
        for j in range(Mine.field_size[0]):
            font = pygame.font.Font('simhei.ttf', 20)
            font_surface = font.render(str(field_list[i][j]), True, 'black')
            display_block(GRAY, j * 25, i * 25)
            screen.blit(font_surface, (j*25+15, i*25+5))



    #display_block(GRAY, 0, 0)


    pygame.display.flip()

    clock.tick(10)

