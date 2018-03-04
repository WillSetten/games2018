# Help link - https://youtu.be/US3HSusUBeI


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

#Contra map has been currently utilised in order to experiment whether this is succesful or not.
bkgd = pygame.image.load("ContraMapStage1BG.png").convert()
x = 0


#main loop

while True:
    events()


    DS.blit(bkgd, (x,0))
    x -=1

    pygame.display.update()
    CLOCK.tick(FPS)

# The code that has been commented out below is an expansion on the above True loop. Instead, a red line is drawn every time the image is repeated.

# while True:
#	events()

#	rel_x = x % bkgd.get_rect().width
#	DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
#	if rel_x < W:
#		DS.blit(bkgd, (rel_x, 0))
#	x -= 1
#	pygame.draw.line(DS, (255, 0, 0), (rel_x, 0), (rel_x, H), 3)

#	pygame.display.update()
#	CLOCK.tick(FPS)
