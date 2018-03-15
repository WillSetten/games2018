import pygame

import constants
import platforms
import enemy

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.PINK)
        screen.blit(self.background,(self.world_shift,0))#

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        #for enemy in self.enemy_list:
        #    enemy.rect.x += shift_x

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

        self.background = pygame.image.load("newBac.jpg").convert_alpha()
        self.background.set_colorkey(constants.WHITE)
        #self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 580],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 580],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 580],

                  [platforms.STONE_PLATFORM_LEFT, 740, 510],
                  [platforms.STONE_PLATFORM_MIDDLE, 810, 510],
                  [platforms.STONE_PLATFORM_RIGHT, 880, 510],

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

                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


# Create platforms for the level

class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("newBac.jpg").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 580],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 580],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 580],

                  [platforms.STONE_PLATFORM_LEFT, 740, 510],
                  [platforms.STONE_PLATFORM_MIDDLE, 810, 510],
                  [platforms.STONE_PLATFORM_RIGHT, 880, 510],

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

                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
