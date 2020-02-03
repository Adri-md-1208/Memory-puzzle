# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame, sys, random 
from pygame.locals import *

# CONSTANTS
FPS = 15
WINDOWHEIGHT = 640
WINDOWWIDTH  = 480
REVEALSPEED  =   8 # Time of reveal animation, only orientative
BOXSIZE      =  40
GAPSIZE      =  10 # Size between boxes
COLUMNS      =   4 
ROWS         =   4
assert (COLUMNS * ROWS) % 2 == 0 , 'The number of boxes must be even'
XMARGIN = int((WINDOWHEIGHT - (ROWS * (BOXSIZE + GAPSIZE))) / 2) # Divided by 2 because XMARGIN seems the left and right margin
YMARGIN = int((WINDOWWIDTH - (COLUMNS * (BOXSIZE + GAPSIZE))) / 2) 

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
pokeball    = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/pokeball.png')
GREATBALL   = 'greatball'
greatball   = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/greatball.png')
ULTRABALL   = 'ultraball'
ultraball   = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/ultraball.png')
PREMIERBALL = 'premierball'
premierball = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/premierball.png')
MASTERBALL  = 'masterball'
masterball  = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/masterball.png')
SAFARIBALL  = 'safariball'
safariball  = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/safariball.png')
MOONBALL    = 'moonball'
moonball    = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/moonball.png')
HEAVYBALL   = 'heavyball'
heavyball   = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/heavyball.png')

BALLS = (POKEBALL, GREATBALL, ULTRABALL, PREMIERBALL, MASTERBALL, SAFARIBALL, MOONBALL, HEAVYBALL)

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
    mainBoard = generateRandomizedBoard() # in line 137
    revealedBoxes = generateRevealedBoxesData(False) # in line 123
    firstSelection = None # Boolean type variable that set if the first box was revealed

    DISPLAY.fill(BGCOLOR)
    startGameAnimation(mainBoard) # in line 275

    while True:
        mouseClicked = False

        DISPLAY.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes) # in line 254

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos() # Get the mouse position
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = pygame.mouse.get_pos() # Get the mouse position when the mouse is clicked
                mouseClicked = True
            
        boxx, boxy = cartesianToPositional(mousex, mousey)
        if boxx != None and boxy != None: # When the mouse is over a box
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy) # in line 268
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealedBoxesAnimation(mainBoard, [(boxx, boxy)]) # in line 238
                revealedBoxes[boxx][boxy] = True
                if firstSelection == None:
                    firstSelection = (boxx, boxy) # Set the box as the first selection
                else: # That is the second selection
                    firstIcon = getBall(mainBoard, firstSelection[0], firstSelection[1]) # in line 218
                    secondIcon = getBall(mainBoard, boxx, boxy) # in line 218
                    if firstIcon != secondIcon:
                        pygame.time.wait(1000) # Retard of 1 second (1000 milliseconds)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard) # in line 292
                        pygame.time.wait(2000)

                        mainBoard = generateRandomizedBoard() # Restart the game 
                        revealedBoxes = generateRevealedBoxesData(False) # in line 123

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
    for i in range(COLUMNS):
        column = []
        for i in range(ROWS):
            column.append(icons[0])
            del icons[0] # Making the list short by deleting the icons that are already used
        board.append(column)
    return board

def splitList(step, theList):
    '''
    This function split a list into a list of lists. The sublist have a size of step paramether
    This function is used in the startGameAnimation() function
    For example, the list [1, 2, 3, 4] passed with a step = 2, will return:
        [[1, 2], [3, 4]] as the result
    '''
    result = []
    for i in range(0, len(theList), step):
        result.append(theList[i:i + step])
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
    elif ball == GREATBALL:
        DISPLAY.blit(greatball, (left, top))
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

def getBall(board, boxx, boxy):
    '''
    This function only return the ball that is in the position
    '''
    return board[boxx][boxy]

def drawBoxCovers(board, boxes, cover):
    '''
    This function cover the icons if is needed
    '''
    for box in boxes:
        left, top = positionalToCartesian(box[0], box[1])
        pygame.draw.rect(DISPLAY, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        ball = getBall(board, box[0], box[1])
        drawIcon(ball, box[0], box[1])
        if cover > 0: 
            pygame.draw.rect(DISPLAY, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def revealedBoxesAnimation(board, boxesToReveal):
    '''
    This function uses the drawBoxCovers function to reveal the boxes in order to decrease the cover paramether from
    the maximum to a negative value (box revealed)
    '''
    for coverage in range(BOXSIZE, - REVEALSPEED - 1, - REVEALSPEED): # The minimum value to the speed must be 1
        drawBoxCovers(board, boxesToReveal, coverage)

def coverBoxesAnimation(board, boxesToCover):
    '''
    This function uses the drawBoxCovers function to reveal the boxes in order to increase the cover paramether from
    the minimum to a value over the maximum (box covered)
    '''
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED): # The minimum value to the speed must be 1
        drawBoxCovers(board, boxesToCover, coverage)

def drawBoard(board, revealed):
    '''
    That function draw the entire board with the revealed and unrevealed boxes. The function know if a box is 
    revealed by passing a list of revealed boxes as an argument
    '''
    for boxx in range(ROWS):
        for boxy in range(COLUMNS):
            left, top = positionalToCartesian(boxx, boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAY, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE)) # Draw a box
            else:
                ball = getBall(board, boxx, boxy)
                drawIcon(ball, boxx, boxy) # Draw a ball

def drawHighlightBox(boxx, boxy):
    '''
    This function draw a perimether around the box passed with the highlightcolor
    '''
    left, top = positionalToCartesian(boxx, boxy)
    pygame.draw.rect(DISPLAY, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4) # 4 is for the width of the line

def startGameAnimation(board):
    '''
    This function show and cover all the boxes in groups of 4 to show the player an intuition of the icons disposition
    '''
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(ROWS):
        for y in range(COLUMNS):
            boxes.append((x, y))
    random.shuffle(boxes)
    boxGroups = splitList(4, boxes) # That is for make groups of 4 boxes to show at once

    drawBoard(board, coveredBoxes)
    for group in boxGroups:
        revealedBoxesAnimation(board, group)
        coverBoxesAnimation(board, group)

def gameWonAnimation(board):
    '''
    This function fills the background with a different color to show that the player wins the game. 
    Then, the game is restarted after a little break
    '''
    coveredBoxes = generateRevealedBoxesData(True)
    DISPLAY.fill(WINCOLOR)
    drawBoard(board, coveredBoxes)
    pygame.display.update()
    pygame.time.wait(300)

def hasWon(revealedBoxes):
    '''
    Return True if all the boxes are uncovered
    '''
    for i in revealedBoxes:
        if False in i: # The in is beacause the revealedBoxes is a list of lists
            return False
    return True

if __name__ == '__main__':
    main()