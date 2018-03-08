# rect or self.rect is the varibale used for the player itself. If another variable name has been used in other sheets please updated.
# Also note that rect has been used as it has been taken from the link excample provided by Tom.
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import pygame
import constants
import levels

class player():

    def __init__ (self):
        self.changeX = 0
        self.changeY = 0
        self.direction = "R"

        self.bump = None

        #A lot of stuff needs to be done for when we have selected the spritesheet, am aware
    def update(self):
        self.calcGrav()

        self.rect.X += self.changeX #Move Left and right
        pos = self.rect.x + self.level.world_shift #Considers movement of the world with the movement of the player

        self.rect.Y += self.changeY #Move up and down (jump and gravity)

        if self.direction == "R":
            frame = (pos//30) % len(self.walkingFramesRight)
            self.image = self.walkingFramesRight[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

    def calcGrav(self): #Occurs when the user is not standing on the ground
        if self.changeY == 0:
            self.changeY = 1
        else self.changeY += 0.35

        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.changeY >= 0:
            self.changeY = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self): #When the user wants to jump
        #A check may need to be implemented to allow for the jump, will be made soon™

        self.changeY = -10

    def moveLeft(self): #When the user selects the key to move left (would say to use "A")
        self.changeX = -5
        self.direction = "L"

    def moveRight(self): #When the user selects the key to move right (would say to use "D")
        self.changeX = 5
        self.direction = "R"

    def stop(self): # When the user is not pressing a button to move either left or right
        self.changeX = 0
