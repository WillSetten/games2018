try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Level():
 #This will be used as a super-class to define a level.

    constant.canvas_height = 720
    constant.canvas_width = 1280

    def __init__(self,player):
        #DATA WILL BE ADDED

    def update(self):
        #DATA WILL BE ADDDED

    def draw(self,screen):
        #Drawing bakground for this level.


        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we will be using
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x)
    # This will relate to the movement of left/right when side scrolling

    #Keep track of shift amount
    self.world_shift += shift_x



class Level_1(Level):

    def __init__(self,player):

        Level.__init__(self,player)
        frame = simplegui.create_frame("Dash ‘em ‘n’ Smash ‘em", CANVAS_WIDTH, CANVAS_HEIGHT)
        self.background = pygame.image.load(#Add image file here)
        self.background.set_colourkey(constant.WHITE)


frame.start()
