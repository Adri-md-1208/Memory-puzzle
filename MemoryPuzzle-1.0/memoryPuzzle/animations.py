# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame, random

import constants as cts
from globals import DISPLAY, FPSCLOCK
from board import generateRevealedBoxesData, getBall
from utils import positionalToCartesian, splitList

def drawIcon(ball, boxx, boxy):
    '''
    This function draw the ball passed by argument
    '''
    left, top = positionalToCartesian(boxx, boxy)

    if ball == cts.POKEBALL:
        DISPLAY.blit(cts.pokeball, (left, top))
    elif ball == cts.GREATBALL:
        DISPLAY.blit(cts.greatball, (left, top))
    elif ball == cts.ULTRABALL:
        DISPLAY.blit(cts.ultraball, (left, top)) 
    elif ball == cts.PREMIERBALL:
        DISPLAY.blit(cts.premierball, (left, top))
    elif ball == cts.MASTERBALL:
        DISPLAY.blit(cts.masterball, (left, top))
    elif ball == cts.SAFARIBALL:
        DISPLAY.blit(cts.safariball, (left, top))
    elif ball == cts.MOONBALL:
        DISPLAY.blit(cts.moonball, (left, top))
    elif ball == cts.HEAVYBALL:
        DISPLAY.blit(cts.heavyball, (left, top))

def drawBoard(board, revealed):
    '''
    That function draw the entire board with the revealed and unrevealed boxes. The function know if a box is 
    revealed by passing a list of revealed boxes as an argument
    '''
    for boxx in range(cts.COLUMNS):
        for boxy in range(cts.ROWS):
            left, top = positionalToCartesian(boxx, boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAY, cts.BOXCOLOR, (left, top, cts.BOXSIZE, cts.BOXSIZE)) # Draw a box
            else:
                ball = getBall(board, boxx, boxy)
                drawIcon(ball, boxx, boxy) # Draw a ball

def drawBoxCovers(board, boxes, cover):
    '''
    This function cover the icons if is needed
    '''
    for box in boxes:
        left, top = positionalToCartesian(box[0], box[1])
        pygame.draw.rect(DISPLAY, cts.BGCOLOR, (left, top, cts.BOXSIZE, cts.BOXSIZE))
        ball = getBall(board, box[0], box[1])
        drawIcon(ball, box[0], box[1])
        if cover > 0: 
            pygame.draw.rect(DISPLAY, cts.BOXCOLOR, (left, top, cts.BOXSIZE, cts.BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(cts.FPS)

def revealedBoxesAnimation(board, boxesToReveal):
    '''
    This function uses the drawBoxCovers function to reveal the boxes in order to decrease the cover paramether from
    the maximum to a negative value (box revealed)
    '''
    for coverage in range(cts.BOXSIZE, (- cts.REVEALSPEED) - 1, - cts.REVEALSPEED): # The minimum value to the speed must be 1
        drawBoxCovers(board, boxesToReveal, coverage)

def coverBoxesAnimation(board, boxesToCover):
    '''
    This function uses the drawBoxCovers function to reveal the boxes in order to increase the cover paramether from
    the minimum to a value over the maximum (box covered)
    '''
    for coverage in range(0, cts.BOXSIZE + cts.REVEALSPEED, cts.REVEALSPEED): # The minimum value to the speed must be 1
        drawBoxCovers(board, boxesToCover, coverage)

def drawHighlightBox(boxx, boxy):
    '''
    This function draw a perimether around the box passed with the highlightcolor
    '''
    left, top = positionalToCartesian(boxx, boxy)
    pygame.draw.rect(DISPLAY, cts.HIGHLIGHTCOLOR, (left - 5, top - 5, cts.BOXSIZE + 10, cts.BOXSIZE + 10), 4) # 4 is for the width of the line

def startGameAnimation(board):
    '''
    This function show and cover all the boxes in groups of 4 to show the player an intuition of the icons disposition
    '''
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(cts.COLUMNS):
        for y in range(cts.ROWS):
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
    DISPLAY.fill(cts.WINCOLOR)
    drawBoard(board, coveredBoxes)
    pygame.display.update()
    pygame.time.wait(3000)