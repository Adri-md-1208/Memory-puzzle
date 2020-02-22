# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame, sys, random 
from pygame.locals import *

from constants import * 
from board import generateRevealedBoxesData, generateRandomizedBoard, drawBoard, getBall
from animations import startGameAnimation, drawHighlightBox, revealedBoxesAnimation, coverBoxesAnimation, gameWonAnimation
from utils import cartesianToPositional, hasWon

# MAIN LOOP
def main():
    global FPSCLOCK, DISPLAY
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Memory puzzle [pokeball version]')

    mousex = 0
    mousey = 0
    mainBoard = generateRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)
    firstSelection = None # Boolean type variable that set if the first box was revealed

    DISPLAY.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        DISPLAY.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos # Get the mouse position
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos # Get the mouse position when the mouse is clicked
                mouseClicked = True
            
        boxx, boxy = cartesianToPositional(mousex, mousey)
        if boxx != None and boxy != None: # When the mouse is over a box
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealedBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True
                if firstSelection == None:
                    firstSelection = (boxx, boxy) # Set the box as the first selection
                else: # That is the second selection
                    firstIcon = getBall(mainBoard, firstSelection[0], firstSelection[1])
                    secondIcon = getBall(mainBoard, boxx, boxy)
                    if firstIcon != secondIcon:
                        pygame.time.wait(500) # Retard of 0'5 seconds (500 milliseconds)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes): 
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        drawBoard(mainBoard, revealedBoxes) # Show the board unrevealed
                        pygame.display.update()
                        pygame.time.wait(1000)

                    firstSelection = None

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()