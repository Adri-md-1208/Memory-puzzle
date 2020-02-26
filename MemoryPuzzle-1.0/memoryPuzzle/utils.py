# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame
import constants as cts

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

def scaleImage(image, size):
    '''
    This function scale a group of image to the size specified
    Be aware because the output will be another image
    '''
    return pygame.transform.scale(image, size)

def positionalToCartesian(boxx, boxy):
    '''
    This function pass from the positional system ,that we are using to refer the boxes in the 2D list [boxx][boxy],
    to a cartesian system that are refered in pixel and is useful to blit the sprites
    The return is a tuple of left, top pixels of the box
    '''
    left = boxx * (cts.BOXSIZE + cts.GAPSIZE) + cts.XMARGIN
    top = boxy * (cts.BOXSIZE + cts.GAPSIZE) + cts.YMARGIN
    return (left, top)

def cartesianToPositional(x, y):
    '''
    That function is used to check if the mouse is over a box. In that case, the function return the position of the 
    box on which is over in the 2D list positional order
    '''
    for boxx in range(cts.COLUMNS):
        for boxy in range(cts.ROWS):
            left, top = positionalToCartesian(boxx, boxy)
            boxRect = pygame.Rect(left, top, cts.BOXSIZE, cts.BOXSIZE)
            if boxRect.collidepoint(x, y): # That method is used to check if the x, y position is colliding with the boxRect
                return (boxx, boxy)
    return (None, None)

def hasWon(revealedBoxes):
    '''
    Return True if all the boxes are uncovered
    '''
    for i in revealedBoxes:
        if False in i: # The in is beacause the revealedBoxes is a list of lists
            return False
    return True