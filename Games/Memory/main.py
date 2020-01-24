# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame, sys, random 
from pygame.locals import *

# CONSTANTS
FPS = 30
WINDOWHEIGHT = 480
WINDOWWIDTH  = 640
REVEALSPEED  =   8 # Time of reveal animation
BOXSIZE      =  40
GAPSIZE      =  10
COLUMNS      =   4 
ROWS         =   4
assert (COLUMNS * ROWS) % 2 == 0 , 'The number of boxes must be even'
XMARGIN = int((WINDOWWIDTH - (ROWS * (BOXSIZE + GAPSIZE))) / 2) # Divided by 2 because XMARGIN seems the left and right margin
YMARGIN = int((WINDOWHEIGHT - (COLUMNS * (BOXSIZE + GAPSIZE))) / 2) 

# COLORS 
#         R    G    B
GRAY = (192, 192, 192)
BLUE = (  0,   0, 255)
CYAN = (  0, 255, 255)

BGCOLOR = GRAY
HIGHLIGHTCOLOR = CYAN
BOXCOLOR = BLUE

DISPLAY = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Memory puzzle!')

# SPRITES 
pokeball    = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/pokeball.png')
greatball   = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/greatball.png')
ultraball   = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/ultraball.png')
premierball = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/premierball.png')
masterball  = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/masterball.png')
safariball  = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/safariball.png')

balls = [pokeball, greatball, ultraball, premierball, masterball, safariball]

# MAIN LOOP
while True:

    pygame.init()
    DISPLAY.fill(BGCOLOR)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY.blit(pokeball, (100, 100))
    DISPLAY.blit(greatball, (200, 200))
    DISPLAY.blit(ultraball, (300, 300))
    DISPLAY.blit(premierball, (400, 400))
    DISPLAY.blit(masterball, (400, 200))
    DISPLAY.blit(safariball, (100, 200))

    pygame.display.update()
