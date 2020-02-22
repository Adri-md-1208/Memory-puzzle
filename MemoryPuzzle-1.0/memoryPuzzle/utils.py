# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame

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