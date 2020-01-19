import pygame, sys, random
from pygame.locals import *

pygame.init()

# TIME
FPS = 2
fpsClock = pygame.time.Clock()

# SCREEN
DISPLAY = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Animations")
BLACK = (0, 0, 0)

# MOVEMENT
boo = pygame.image.load("C:/Users/Adrián/Desktop/Python-games/Tests/boo.png")
booX = 300
booY = 200
direction = ("R", "L", "U", "D") # Right, left, up and down

# MUSIC
pygame.mixer.music.load("C:/Users/Adrián/Desktop/Python-games/Tests/music.mp3")
pygame.mixer.music.play(-1, 0.0)

# MAIN LOOP
while True:

    DISPLAY.fill(BLACK)

    move = random.choice(direction)

    if move == "R":
        booX += 20
        if booX > 600:
            booX = 600
    elif move == "L":
        booX -= 20
        if booX < 0:
            booX = 0
    elif move == "D":
        booY += 20
        if booY > 400:
            booY = 400
    elif move == "U":
        booY -= 20
        if booY < 0:
            booY = 0

    DISPLAY.blit(boo, (booX, booY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)