# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame
from constants import WINDOWWIDTH, WINDOWHEIGHT

global FPSCLOCK, DISPLAY

FPSCLOCK = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))