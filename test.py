import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((640, 480))


pokeball = pygame.image.load('C:/Users/Adrián/Desktop/Memory-puzzle/sprites/masterball.png')


while True:
    DISPLAY.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAY.blit(pokeball, (50,50))
    pygame.display.update()
    
        