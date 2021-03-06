# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import os
import pygame
import tkinter as tk
from tkinter import messagebox

import utils as utl

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

pygame.font.init()
FONT = pygame.font.SysFont('Consolas', 35)

# COLORS 
#             R    G    B
BLACK    = (  0,   0,   0)
GRAY     = (192, 192, 192)
BLUE     = (  0,   0, 255)
CYAN     = (  0, 255, 255)
RED      = (255,   0,   0)
RED_SOFT = (255, 120, 120)

BGCOLOR = GRAY
HIGHLIGHTCOLOR = CYAN # The color around a box when the mouse is over
BOXCOLOR = BLUE
WINCOLOR = RED
TIMERCOLOR = RED_SOFT

# SPRITES
dirname = os.path.dirname(__file__)
try:
    pokeball    = utl.scaleImage(pygame.image.load(open(os.path.join(dirname, 'sprites/pokeball.png'), 'r')), (BOXSIZE, BOXSIZE))
    greatball   = utl.scaleImage(pygame.image.load(open(os.path.join(dirname, 'sprites/greatball.png'), 'r')), (BOXSIZE, BOXSIZE))
    ultraball   = utl.scaleImage(pygame.image.load(open(os.path.join(dirname, 'sprites/ultraball.png'), 'r')), (BOXSIZE, BOXSIZE))
    premierball = utl.scaleImage(pygame.image.load(open(os.path.join(dirname, 'sprites/premierball.png'), 'r')), (BOXSIZE, BOXSIZE))
    masterball  = utl.scaleImage(pygame.image.load(open(os.path.join(dirname, 'sprites/masterball.png'), 'r')), (BOXSIZE, BOXSIZE))
    safariball  = utl.scaleImage(pygame.image.load(open(os.path.join(dirname, 'sprites/safariball.png'), 'r')), (BOXSIZE, BOXSIZE))
    moonball    = utl.scaleImage(pygame.image.load(open(os.path.join(dirname, 'sprites/moonball.png'), 'r')), (BOXSIZE, BOXSIZE))
    heavyball   = utl.scaleImage(pygame.image.load(open(os.path.join(dirname, 'sprites/heavyball.png'), 'r')), (BOXSIZE, BOXSIZE))
except FileNotFoundError:
    root = tk.Tk()
    root.withdraw() # Hide the tk root window, we only need to show the alert box
    messagebox.showwarning("FileNotFoundError", "The sprite you want to display are in a wrong path")

# CONSTANT NAMES
POKEBALL    = 'pokeball'
GREATBALL   = 'greatball'
ULTRABALL   = 'ultraball'
PREMIERBALL = 'premierball'
MASTERBALL  = 'masterball'
SAFARIBALL  = 'safariball'
MOONBALL    = 'moonball'
HEAVYBALL   = 'heavyball'

BALLS =   [POKEBALL, GREATBALL, ULTRABALL, PREMIERBALL, MASTERBALL, SAFARIBALL, MOONBALL, HEAVYBALL]

assert (len(BALLS) * 2) == (COLUMNS * ROWS), 'The number of sprites must be equal to the number of boxes' 