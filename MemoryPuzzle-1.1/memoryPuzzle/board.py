# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import random
import pygame

import constants as cts

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
    for i in range(cts.COLUMNS):
        revealedBoxes.append([data] * cts.ROWS)
    return revealedBoxes

def generateRandomizedBoard():
    '''
    That function return a 2 dimensional list with the icons placed in random sites
    We use a copy of BALLS list and then duplicate them to get the pairs of icons
    '''
    icons = []
    for i in cts.BALLS:
        icons.append(i) # That list is a copy of the BALLS list
    random.shuffle(icons)

    numberIconsUsed = int((cts.ROWS * cts.COLUMNS) / 2) # The number of icons that we need to use
    icons = icons[:numberIconsUsed] * 2 # Shorting the list for taking only the number of icons that we need (now, the pair of icons)
    random.shuffle(icons)
    
    board = [] # This is similar to the generateRevealedBoxesData function, but the elements are elements of the icons list
    for x in range(cts.COLUMNS):
        column = []
        for y in range(cts.ROWS):
            column.append(icons[0])
            del icons[0] # Making the list short by deleting the icons that are already used
        board.append(column)
    return board

def getBall(board, boxx, boxy):
    '''
    This function only return the ball that is in the position
    '''
    return board[boxx][boxy]