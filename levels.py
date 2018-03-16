import pygame

import constants
import platforms
import enemy
import main


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = []

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -3000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        #screen.fill(constants.PINK)
        screen.blit(self.background,(self.world_shift,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

#<<<<<<< HEAD
#=======
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

#>>>>>>> 7a4167d5f863197206f6ca89fe91e6437f8fcee1
#Development of a main menu
class Level_main_menu(Level):
    def __init__(self):
        super(Level_menu_main, self).__init__()

        self.create_gradient_background((0, 0, 0), (255, 255, 255))

        self.menu = Main_menu(self)
        self.list_draw.append(self.menu)
        self.list_update.append(self.menu)

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("backgroundNew.png").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        #self.level_limit = -2500


        # Array with type of platform, and x, y location of the platform.
        #x value is a difference of 70
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 420],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 420],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 420],

                  [platforms.STONE_PLATFORM_LEFT, 740, 290],
                  [platforms.STONE_PLATFORM_MIDDLE, 810, 290],
                  [platforms.STONE_PLATFORM_MIDDLE, 880,290],
                  [platforms.STONE_PLATFORM_RIGHT, 850,290],

                  [platforms.STONE_PLATFORM_LEFT, 990, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 1060, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 1130, 400],

                  [platforms.STONE_PLATFORM_LEFT, 1820, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1890, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1960, 280],

                  [platforms.STONE_PLATFORM_LEFT, 2250, 360],
                  [platforms.STONE_PLATFORM_MIDDLE, 2320, 360],
                  [platforms.STONE_PLATFORM_RIGHT, 2390, 360],

                  [platforms.STONE_PLATFORM_LEFT, 2610, 430],
                  [platforms.STONE_PLATFORM_MIDDLE, 2680, 430],
                  [platforms.STONE_PLATFORM_RIGHT, 2750, 430],

                  #Azhar's Platforms
                  [platforms.STONE_PLATFORM_LEFT, 3000, 510],
                  [platforms.STONE_PLATFORM_MIDDLE, 3070, 510],
                  [platforms.STONE_PLATFORM_RIGHT, 3140, 510],

                  [platforms.STONE_PLATFORM_LEFT, 2100, 300],
                  [platforms.STONE_PLATFORM_MIDDLE, 2800, 300],
                  [platforms.STONE_PLATFORM_RIGHT, 3500, 300],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


# Create platforms for the level



#Implements tiles into the game



#def load_tileset(tileset3.png, 30, 30):

#    image = pygame.image.load(tileset3.png).convert()
#    image.width. image.height = image.get_size()
#    tileset = []
#    for tile_x in range(0, image_width//30):

    #image = pygame.image.load(tileset3.png).convert()
    #image.width. image.height = image.get_size()
    #tileset = []
    #for tile_x in range(0, image_width//30):

#        line = []
#        tileset,append(line)
#    for tile_y in range(0, image_height//30):
#        rect = (tile_x*width, tile_y*height, 30, 30)
#        line.append(image.subsurface(rect))
#    return tileset

#def draw_background(screen, tile_img, field_rect)
