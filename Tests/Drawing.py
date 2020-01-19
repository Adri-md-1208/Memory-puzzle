import pygame, sys
from pygame.locals import *

from math import pi

pygame.init()

# DISPLAY

DISPLAY = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Drawing with pygame")

# COLORS    R    G    B

GREY   = (128, 128, 128)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
YELLOW = (255, 255,   0)
BLUE   = (  0,   0, 255)
VIOLET = (120,  40, 140)
WHITE  = (255, 255, 255)

# DRAWING

DISPLAY.fill(GREY)
pygame.draw.polygon(DISPLAY, GREEN, ((50, 50), (100, 100), (50, 100)))
pygame.draw.aaline(DISPLAY, RED, (150, 100), (175, 50), 5)
pygame.draw.aaline(DISPLAY, RED, (200, 100), (175, 50), 5)
pygame.draw.aaline(DISPLAY, RED, (150, 75), (200, 75), 5)
pygame.draw.aaline(DISPLAY, YELLOW, (250, 100), (250, 50), 5)
pygame.draw.aaline(DISPLAY, YELLOW, (250, 50), (275, 75), 5)
pygame.draw.aaline(DISPLAY, YELLOW, (300, 50), (275, 75), 5)
pygame.draw.aaline(DISPLAY, YELLOW, (300, 100), (300, 50), 5)
pygame.draw.aaline(DISPLAY, VIOLET, (350, 100), (350, 50), 5)
pygame.draw.arc(DISPLAY, VIOLET, (325, 50, 50, 50), (3*pi)/2, pi/2, 5)
pygame.draw.circle(DISPLAY, BLUE, (250, 250), 25, 5)
pygame.draw.polygon(DISPLAY, RED, ((450, 450), (400, 450), (300, 350), (250, 300), (500, 120)))
pygame.draw.ellipse(DISPLAY, GREEN, (30, 430, 220, 15), 5)

pixObj = pygame.PixelArray(DISPLAY)
pixObj[30][30] = WHITE
pixObj[50][67] = WHITE
pixObj[122][234] = WHITE
pixObj[98][344] = WHITE
del pixObj

# MAIN LOOP

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()