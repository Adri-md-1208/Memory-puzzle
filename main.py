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
GAPSIZE      =  10 # Size between boxes
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
HIGHLIGHTCOLOR = CYAN # The color around every box
BOXCOLOR = BLUE

# SPRITES 
POKEBALL    = 'pokeball'
pokeball    = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/pokeball.png')
GREATBALL   = 'greatball'
greatball   = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/greatball.png')
ULTRABALL   = 'ultraball'
ultraball   = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/ultraball.png')
PREMIERBALL = 'premierball'
premierball = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/premierball.png')
MASTERBALL  = 'masterball'
masterball  = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/masterball.png')
SAFARIBALL  = 'safariball'
safariball  = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/safariball.png')
MOONBALL    = 'moonball'
moonball    = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/moonball.png')
HEAVYBALL   = 'heavyball'
heavyball   = pygame.image.load('C:/Users/Adrián/Desktop/Python-games/Games/Memory/sprites/heavyball.png')

BALLS = (pokeball, greatball, ultraball, premierball, masterball, safariball, moonball, heavyball)

assert (len(BALLS) * 2) == (COLUMNS * ROWS), 'The number of sprites must be equal to the number of boxes' 

# MAIN LOOP
def main():
    global FPSCLOCK, DISPLAY
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))
    pygame.display.set_caption('Memory puzzle [pokeball version]')

    mousex = 0
    mousey = 0
    mainBoard = generateRandomizedBoard() # in line 127
    revealedBoxes = generateRevealedBoxesData(False) # in line 113
    firstSelection = None # Boolean type variable that set if the first box was revealed

    DISPLAY.fill(BGCOLOR)
    startGameAnimation(mainBoard) # in line 

    while True:
        mouseClicked() = False

        DISPLAY.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes) # in line 

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos # Get the mouse position
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos # Get the mouse position when the mouse is clicked
                mouseClicked = True
            
            boxx, boxy = getBoxAtPixel(mousex, mousey)
            if boxx != None and boxy != None: # When the mouse is over a box
                if not revealedBoxes([boxx][boxy]):
                    drawHighlightBox(boxx, boxy)
                if not revealedBoxes([boxx][boxy]) and mouseClicked:
                    revealedBoxesAnimation(mainBoard, [(boxx, boxy)]) # in line
                    revealedBoxes[boxx][boxy] = True
                    if firstSelection == None:
                        firstSelection = (boxx, boxy) # Set the box as the first selection
                    else: # That is the second selection
                        firstIcon = getIcons(mainBoard, firstSelection[0], firstSelection[1]) # in line
                        secondIcon = getIcons(mainBoard, boxx, boxy) # in line
                        if firstIcon != secondIcon:
                            pygame.time.wait(1000) # Retard of 1 second (1000 milliseconds)
                            coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                            revealedBoxes(firstSelection[0], firstSelection[1]) = False
                            revealedBoxes(boxx, boxy) = False
                        elif hasWon(revealedBoxes):
                            gameWonAnimation(mainBoard) # in line
                            pygame.time.wait(2000)

                            mainBoard = generateRandomizedBoard() # Restart the game 
                            revealedBoxes = setRevealedBoxes(False) # in line

                            drawBoard(mainBoard, revealedBoxes) # Show the board unrevealed
                            pygame.display.update()
                            pygame.time.wait(1000)

                            startGameAnimation(mainBoard)
                        firstSelection = None

                        pygame.display.update()
                        FPSCLOCK.tick(FPS)

def generateRevealedBoxesData(data):
    '''
    In that function I generate a 2 dimensional list that represents the boxes distribution over the board
    Is something like
      [ [][][][],
        [][][][],
        [][][][],
        [][][][] ]
        '''
    revealedBoxes = []
    for i in range(ROWS):
        revealedBoxes.append([data] * COLUMNS)
    return revealedBoxes

def generateRandomizedBoard():
    '''
    That function return a 2 dimensional list with the icons placed in random sites
    We use a copy of BALLS list and then duplicate them to get the pairs of icons
    '''
    icons = []
    for i in BALLS:
        icons.append(i) # That list is a copy of the BALLS list
    random.shuffle(icons)

    numberIconsUsed = int((ROWS * COLUMNS) / 2) # The number of icons that we need to use
    icons = icons[:numberIconsUsed] * 2 # Shorting the list for taking only the number of icons that we need (now, the pair of icons)
    random.shuffle(icons)
    
    board = [] # This is similar to the generateRevealedBoxesData function, but the elements are elements of the icons list
    for i in range(ROWS):
        column = []
        for i in range(COLUMNS):
            column.append(icons[0])
            del icons[0] # Making the list short by deleting the icons that are already used
        board.append(column)
    return board

def splitList(step, list):
    '''
    This function split a list into a list of lists. The sublist have a size of step paramether
    This function is used in the startGameAnimation() function
    For example, the list [1, 2, 3, 4] passed with a step = 2, will return:
        [[1, 2], [3, 4]] as the result
    '''
    result = []
    for i in range(0, len(list), step):
        result.append(list[i:i + step])
    return result

def positionalToCartesian(boxx, boxy):
    '''
    This function pass from the positional system ,that we are using to refer the boxes in the 2D list [boxx][boxy],
    to a cartesian system that are refered in pixel and is useful to blit the sprites
    The return is a tuple of left, top pixels of the box
    '''
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)

def cartesianToPositional(x, y):
    '''
    That function is used to check if the mouse is over a box. In that case, the function return the position of the 
    box on which is over in the 2D list positional order
    '''
    for boxx in range(ROWS):
        for boxy in range(COLUMNS):
            left, top = positionalToCartesian(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y): # That method is used to check if the x, y position is colliding with the boxRect
                return (boxx, boxy)
        return (None, None)

def drawIcon(ball, boxx, boxy):
    '''
    This function draw the ball passed by argument
    '''
    left, top = positionalToCartesian(boxx, boxy)

    if ball == POKEBALL:
        DISPLAY.blit(pokeball, (left, top))
    elif ball == SUPERBALL:
        DISPLAY.blit(superball, (left, top))
    elif ball == ULTRABALL:
        DISPLAY.blit(ultraball, (left, top)) 
    elif ball == PREMIERBALL:
        DISPLAY.blit(premierball, (left, top))
    elif ball == MASTERBALL:
        DISPLAY.blit(masterball, (left, top))
    elif safariball == POKEBALL:
        DISPLAY.blit(safariball, (left, top))
    elif ball == MOONBALL:
        DISPLAY.blit(moonball, (left, top))
    elif ball == HEAVYBALL:
        DISPLAY.blit(heavyball, (left, top))



if __name__ = '__main__':
    main()