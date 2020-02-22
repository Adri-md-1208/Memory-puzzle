# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame

from utils import scaleImage

# CONSTANTS
FPS = 30
WINDOWHEIGHT = 480
WINDOWWIDTH  = 640
REVEALSPEED  =   6 # Time of reveal animation, only orientative
BOXSIZE      =  40
GAPSIZE      =  10 # Size between boxes
COLUMNS      =   4 
ROWS         =   4
assert (COLUMNS * ROWS) % 2 == 0 , 'The number of boxes must be even'
XMARGIN = int((WINDOWWIDTH - (COLUMNS * (BOXSIZE + GAPSIZE))) / 2) # Divided by 2 because XMARGIN seems the left and right margin
YMARGIN = int((WINDOWHEIGHT - (ROWS * (BOXSIZE + GAPSIZE))) / 2) 

# COLORS 
#         R    G    B
GRAY = (192, 192, 192)
BLUE = (  0,   0, 255)
CYAN = (  0, 255, 255)
RED  = (255,   0,   0)

BGCOLOR = GRAY
HIGHLIGHTCOLOR = CYAN # The color around a box when the mouse is over
BOXCOLOR = BLUE
WINCOLOR = RED

# SPRITES 
POKEBALL    = 'pokeball'
pokeball    = scaleImage(pygame.image.load('c:/Users/Adrián/Desktop/Memory-puzzle/MemoryPuzzle-1.0/memoryPuzzle/sprites/pokeball.png'), (BOXSIZE, BOXSIZE))
GREATBALL   = 'greatball'
greatball   = scaleImage(pygame.image.load('c:/Users/Adrián/Desktop/Memory-puzzle/MemoryPuzzle-1.0/memoryPuzzle/sprites/greatball.png'), (BOXSIZE, BOXSIZE))
ULTRABALL   = 'ultraball'
ultraball   = scaleImage(pygame.image.load('c:/Users/Adrián/Desktop/Memory-puzzle/MemoryPuzzle-1.0/memoryPuzzle/sprites/ultraball.png'), (BOXSIZE, BOXSIZE))
PREMIERBALL = 'premierball'
premierball = scaleImage(pygame.image.load('c:/Users/Adrián/Desktop/Memory-puzzle/MemoryPuzzle-1.0/memoryPuzzle/sprites/premierball.png'), (BOXSIZE, BOXSIZE))
MASTERBALL  = 'masterball'
masterball  = scaleImage(pygame.image.load('c:/Users/Adrián/Desktop/Memory-puzzle/MemoryPuzzle-1.0/memoryPuzzle/sprites/masterball.png'), (BOXSIZE, BOXSIZE))
SAFARIBALL  = 'safariball'
safariball  = scaleImage(pygame.image.load('c:/Users/Adrián/Desktop/Memory-puzzle/MemoryPuzzle-1.0/memoryPuzzle/sprites/safariball.png'), (BOXSIZE, BOXSIZE))
MOONBALL    = 'moonball'
moonball    = scaleImage(pygame.image.load('c:/Users/Adrián/Desktop/Memory-puzzle/MemoryPuzzle-1.0/memoryPuzzle/sprites/moonball.png'), (BOXSIZE, BOXSIZE))
HEAVYBALL   = 'heavyball'
heavyball   = scaleImage(pygame.image.load('c:/Users/Adrián/Desktop/Memory-puzzle/MemoryPuzzle-1.0/memoryPuzzle/sprites/heavyball.png'), (BOXSIZE, BOXSIZE))

BALLS =   [POKEBALL, GREATBALL, ULTRABALL, PREMIERBALL, MASTERBALL, SAFARIBALL, MOONBALL, HEAVYBALL]

assert (len(BALLS) * 2) == (COLUMNS * ROWS), 'The number of sprites must be equal to the number of boxes' 