# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

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