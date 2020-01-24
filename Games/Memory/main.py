# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame, sys, random 
from pygame.locals import *

# CONSTANTS
#################################################################################################################################
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
#################################################################################################################################
#         R    G    B
GRAY = (192, 192, 192)
BLUE = (  0,   0, 255)
CYAN = (  0, 255, 255)

BGCOLOR = GRAY
HIGHLIGHTCOLOR = CYAN
BOXCOLOR = BLUE

# DISPLAY
#################################################################################################################################
DISPLAY = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Memory puzzle!')

# SPRITES 
#################################################################################################################################
POKEBALL    = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/pokeball.png')
GREATBALL   = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/greatball.png')
ULTRABALL   = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/ultraball.png')
PREMIERBALL = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/premierball.png')
MASTERBALL  = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/masterball.png')
SAFARIBALL  = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/safariball.png')
MOONBALL    = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/moonball.png')
HEAVYBALL   = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/heavyball.png')

BALLS = (POKEBALL, GREATBALL, ULTRABALL, PREMIERBALL, MASTERBALL, SAFARIBALL, MOONBALL, HEAVYBALL)

assert (len(BALLS) * 2) == (COLUMNS * ROWS), 'The number of sprites must be equal to the number of boxes' 

# MAIN LOOP
#################################################################################################################################
while True:

    pygame.init()
    DISPLAY.fill(BGCOLOR)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
