"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame
import time
import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0
    count=1
    #framespeed is the number of iterations the sprite will stay on the same frame so 0=fastest animation
    flag = 0
    framespeed=4
    #jumping tells us if the player is jumping.
    jumping = False
    #isprone tells us if the player is prone.
    isprone = False
    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    jumping_frames_l = []
    jumping_frames_r = []
    idle_frame_l = None
    idle_frame_r = None
    prone_frame_r = None
    prone_frame_l = None
    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("player1.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(324, 261, 30, 45)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(358, 262, 26, 44)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(388, 262, 24, 44)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(414, 260, 33, 46)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(451, 259, 38, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(324, 210, 39, 45)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(367, 211, 36, 44)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(408, 211, 32, 44)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(444, 210, 28, 45)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(476, 212, 35, 43)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(515, 212, 38, 43)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        for x in self.walking_frames_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)

        #load the right facing jumping frame
        image = sprite_sheet.get_image(324, 63, 22, 22)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(349, 65, 23, 20)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(375, 64, 22, 22)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(400, 64, 20, 25)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(423, 64, 22, 22)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(448, 66, 25, 20)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(476, 64, 20, 23)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(499, 64, 20, 25)
        self.jumping_frames_r.append(image)
        #load the left facing jumping frame
        for x in self.jumping_frames_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.jumping_frames_l.append(image)

        self.idle_frame_r = sprite_sheet.get_image(324, 93, 35, 42)
        self.idle_frame_l = pygame.transform.flip(self.idle_frame_r, True, False)

        self.prone_frame_r = sprite_sheet.get_image(324, 139, 50, 19)
        self.prone_frame_l = pygame.transform.flip(self.prone_frame_r, True, False)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift

        #checks if jumping
        if self.jumping and (self.change_y>1 or self.change_y<1):
            self.framespeed = 3
            if self.direction == "L":
                frame = (self.count) % len(self.jumping_frames_l)
                self.image = self.jumping_frames_l[frame]
            else:
                frame = (self.count) % len(self.jumping_frames_r)
                self.image = self.jumping_frames_r[frame]
        elif(self.change_x!=0):
            self.framespeed = 3
            if self.direction == "R":
                frame = (self.count) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            elif self.direction == "L":
                frame = (self.count) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]
        elif self.isprone:
            if self.direction == "L":
                self.image = self.prone_frame_l
            else:
                self.image = self.prone_frame_r
        else:
            if self.direction == "L":
                self.image = self.idle_frame_l
            else:
                self.image = self.idle_frame_r
        if self.flag == 0:
            self.count += 1
            self.flag=self.framespeed
        else:
            self.flag-=1
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom


            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1

        else:
            self.change_y += .35

        #see if we are on top of the platform


        # See if we are on the ground.
        if (self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0): #add in trigger for on platform or ():
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            self.jumping = False

    def jump(self):
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        self.jumping = True
        self.isprone = False
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.isprone = False
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.isprone = False
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 00
        self.isprone = False

    def prone(self):
        self.change_x = 0
        self.isprone = True
