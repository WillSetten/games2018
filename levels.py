try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import pygame
import constants

class Level():
 #This will be used as a super-class to define a level.

    def __init__(self,player):
        #list of all sprites need to be added here, after we have decided the sprites to be utilised
        self.platform_list = None
        self.enemy_list = None

        self.background = None

        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player



    def update(self):
        #all sprites need to be updated at this stage
        self.platform_list.update()
        self.enemy_list.update()


    def draw(self,screen):
        #Drawing background for this level.
        frame = simplegui.create_frame("Dash ‘em ‘n’ Smash ‘em", constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we will be using
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        # This will relate to the movement of left/right when side scrolling

        #Keep track of shift amount
        self.world_shift += shift_x

        #Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


class Level_1(Level):
    def __init__(self,player):

        Level.__init__(self,player)
        frame = simplegui.create_frame("Dash ‘em ‘n’ Smash ‘em", constants.SCREEN_WIDTH, constants.CANVAS_HEIGHT)
        self.background = pygame.image.load("ContraMapStage5BG.png")
        self.background.set_colourkey(constants.WHITE)
        #Application of moving platforms needs to be added
        #Array with type of platform, and x, y location of the platform, needs to be added
frame.start()
