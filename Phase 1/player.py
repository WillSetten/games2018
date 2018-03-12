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
    #aiming tells us which direction in which the player is aiming
    aiming = "MID"
    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    jumping_frames_l = []
    jumping_frames_r = []
    aim_up_running_r = []
    aim_up_running_l = []

    aim_down_running_r = []
    aim_down_running_l = []

    idle_frame_l = None
    idle_frame_r = None
    prone_frame_r = None
    prone_frame_l = None

    direct_upaim_l = None
    direct_upaim_r = None
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

        #load the right facing jumping frames
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

        #load the sprites for aiming upwards whilst running right
        image = sprite_sheet.get_image(323, 310, 35, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(362, 310, 34, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(402, 310, 32, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(439, 310, 31, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(474, 310, 29, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(509, 310, 29, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(544, 309, 29, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(324, 367, 36, 48)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(368, 368, 38, 47)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(411, 365, 36, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(451, 365, 35, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(490, 365, 34, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(529, 365, 31, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(564, 365, 29, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(596, 365, 29, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(323, 310, 35, 50)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(323, 417, 29, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(355, 417, 30, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(389, 417, 33, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(425, 422, 36, 46)
        self.aim_up_running_r.append(image)
        #load the sprites for aiming upwards whilst running left
        for x in self.aim_up_running_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.aim_up_running_l.append(image)

        #load the sprites for aiming downwards whilst running right
        image = sprite_sheet.get_image(323, 472, 34, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(360, 473, 33, 44)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(396, 473, 31, 44)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(431, 473, 31, 44)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(467, 473, 31, 44)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(502, 473, 31, 44)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(535, 472, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(568, 472, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(602, 472, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(323, 523, 32, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(359, 523, 36, 45)
        self.aim_down_running_r.append(image)

        for x in self.aim_down_running_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.aim_down_running_l.append(image)

        #load the idle aiming up frames
        self.direct_upaim_r = sprite_sheet.get_image(613, 3, 24, 57)
        self.direct_upaim_l = pygame.transform.flip(self.direct_upaim_r, True, False)
        #load the idle frames
        self.idle_frame_r = sprite_sheet.get_image(324, 93, 35, 42)
        self.idle_frame_l = pygame.transform.flip(self.idle_frame_r, True, False)
        #load the prone frames
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
            self.framespeed = 2
            if self.direction == "L":
                frame = (self.count) % len(self.jumping_frames_l)
                self.image = self.jumping_frames_l[frame]
            else:
                frame = (self.count) % len(self.jumping_frames_r)
                self.image = self.jumping_frames_r[frame]
        elif(self.change_x!=0):
            self.framespeed = 3
            if self.aiming == "UP":
                if self.direction == "L":
                    frame = (self.count) % len(self.aim_up_running_l)
                    self.image = self.aim_up_running_l[frame]
                else:
                    frame = (self.count) % len(self.aim_up_running_r)
                    self.image = self.aim_up_running_r[frame]
            elif self.isprone == True:
                if self.direction == "L":
                    frame = (self.count) % len(self.aim_down_running_l)
                    self.image = self.aim_down_running_l[frame]
                else:
                    frame = (self.count) % len(self.aim_down_running_r)
                    self.image = self.aim_down_running_r[frame]
            else:
                if self.direction == "L":
                    frame = (self.count) % len(self.walking_frames_l)
                    self.image = self.walking_frames_l[frame]
                else:
                    frame = (self.count) % len(self.walking_frames_r)
                    self.image = self.walking_frames_r[frame]
        elif self.isprone:
            if self.direction == "L":
                self.image = self.prone_frame_l
            else:
                self.image = self.prone_frame_r
        else:
            if self.aiming == "UP":
                if self.direction == "L":
                    self.image = self.direct_upaim_l
                else:
                    self.image = self.direct_upaim_r
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
            # set our right side to the left side of the item we hit
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

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
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

    def shoot_left(self):
        self.direction = "L"
    def shoot_Right(self):
        self.direction = "R"
    def shoot_Up(self):
        # All 4 of these need their respective spites and bullet link
    def shoot_down(self):

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.isprone = False
        self.change_x = -5
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.isprone = False
        self.change_x = 5
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 00
        self.isprone = False
        self.aiming = "MID"

    def prone(self):
        self.aiming = "MID"
        self.isprone = True

    def aimup(self):
        self.aiming = "UP"

    def resetaim(self):
        self.aiming = "MID"
        self.isprone = False
