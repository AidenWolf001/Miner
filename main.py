import pygame
import sys
import math
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

points = [(200, 175), (300, 125), (400, 175), (450, 125), (450, 225), (400, 175), (300, 225)]

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Miner")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (0, 0, 30, 30), 0)


    pygame.display.flip()

    clock.tick(10)