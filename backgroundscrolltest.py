import pygame
from pygame.locals import *
import sys
import os


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


#defining display
W, H = 1080, 240
HW, HH = W/2, H/2
AREA = W * H


os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

#setup pygame

pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W,H))
pygame.display.set_caption("Background Trial")
FPS = 60

bkgd = pygame.image.load("ContraMapStage1BG.png").convert()
x = 0


#main loop

while True:
    events()


    DS.blit(bkgd, (x,0))
    x -=1

    pygame.display.update()
    CLOCK.tick(FPS)
