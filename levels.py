try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import pygame


class Level():
 #This will be used as a super-class to define a level.

    constant.canvas_height = 720
    constant.canvas_width = 1280

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
        frame = simplegui.create_frame("Dash ‘em ‘n’ Smash ‘em", CANVAS_WIDTH, CANVAS_HEIGHT)

        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we will be using
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x)
    # This will relate to the movement of left/right when side scrolling

    #Keep track of shift amount
    self.world_shift += shift_x

    #Go through all the sprite lists and shift
    for platform in self.platform_list:
        platfor.rect.x += shift_x

    for enemy in self.enemy_list:
        enemy.rect.x += shift_x


class Level_1(Level):

    def __init__(self,player):

        Level.__init__(self,player)
        frame = simplegui.create_frame("Dash ‘em ‘n’ Smash ‘em", CANVAS_WIDTH, CANVAS_HEIGHT)
        self.background = pygame.image.load(#Add image file here)
        self.background.set_colourkey(constant.WHITE)


frame.start()
