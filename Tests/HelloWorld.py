import pygame, sys
from pygame.locals import *

pygame.init() # That function must be the first to be initialized
DISPLAY = pygame.display.set_mode((500, 500)) # Set the size of the screen
pygame.display.set_caption('Hello World!')

RED  = (255,  0,   0)
BLUE = (  0,  0, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello World!', True, RED, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (250, 250)

while True:
    DISPLAY.fill(BLUE)
    DISPLAY.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()