import pygame, sys
from pygame.locals import *

pygame.init() # That function must be the first to be initialized
DISPLAY = pygame.display.set_mode((500, 500)) # Set the size of the screen
pygame.display.set_caption("Hello World!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()