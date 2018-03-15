import pygame

import constants
class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
        """Best way to use this module is at initialisation, where you can create the SpriteSheet then use the get_image
        function in a for loop of some kind to add all the frames in a set animation to an array, then you can just
        iterate through the array at initialisation"""
    def get_image(self, x, y, width, height):
        """x and y correspond to the position of the pixel in the top left of the image, width and height
        are its width and height obvs."""
        image = pygame.Surface([width, height]).convert()
        "copies the sprite in the constrained area into the new image"
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        """if the SpriteSheet has a colour in the background then you can use this line to make that colour transparent
        but we'll probably just"""
        image.set_colorkey(constants.PINK)
        return image
