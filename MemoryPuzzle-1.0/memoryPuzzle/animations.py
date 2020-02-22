# Memory puzzle by Adrian Morales Dato
# GitHub : Adri-md-1208
# E-mail : a.morales.2019@alummos.urjc.es
# Released under a "GPLv3" license

import pygame, random

from constants import *
from board import generateRevealedBoxesData, drawBoard
from utils import positionalToCartesian, splitList

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
    elif ball == SAFARIBALL:
        DISPLAY.blit(safariball, (left, top))
    elif ball == MOONBALL:
        DISPLAY.blit(moonball, (left, top))
    elif ball == HEAVYBALL:
        DISPLAY.blit(heavyball, (left, top))

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
    for coverage in range(BOXSIZE, (- REVEALSPEED) - 1, - REVEALSPEED): # The minimum value to the speed must be 1
        drawBoxCovers(board, boxesToReveal, coverage)

def coverBoxesAnimation(board, boxesToCover):
    '''
    This function uses the drawBoxCovers function to reveal the boxes in order to increase the cover paramether from
    the minimum to a value over the maximum (box covered)
    '''
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED): # The minimum value to the speed must be 1
        drawBoxCovers(board, boxesToCover, coverage)

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
    for x in range(COLUMNS):
        for y in range(ROWS):
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
    pygame.time.wait(3000)