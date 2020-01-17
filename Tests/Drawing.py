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
VIOLET = (120,  40, 140)

# DRAWING

DISPLAY.fill(GREY)
pygame.draw.polygon(DISPLAY, GREEN, ((50, 50), (100, 100), (50, 100)))
pygame.draw.line(DISPLAY, RED, (150, 100), (175, 50), 5)
pygame.draw.line(DISPLAY, RED, (200, 100), (175, 50), 5)
pygame.draw.line(DISPLAY, RED, (150, 75), (200, 75), 5)
pygame.draw.line(DISPLAY, YELLOW, (250, 100), (250, 50), 5)
pygame.draw.line(DISPLAY, YELLOW, (250, 50), (275, 75), 5)
pygame.draw.line(DISPLAY, YELLOW, (300, 50), (275, 75), 5)
pygame.draw.line(DISPLAY, YELLOW, (300, 100), (300, 50), 5)
pygame.draw.line(DISPLAY, VIOLET, (350, 100), (350, 50), 5)
pygame.draw.arc(DISPLAY, VIOLET, (325, 50, 50, 50), (3*pi)/2, pi/2, 5)

# MAIN LOOP

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()