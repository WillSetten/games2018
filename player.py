"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame
import sys
import time
import constants
from spritesheet_functions import SpriteSheet
import main
from bullet import Bullet
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    onPlatform = False#
    bullet_list = []
    # Set speed vector of player
    deathcount = 0
    dead = False
    change_x = 0
    change_y = 0
    count=1
    guncount=0
    lives = 5
    score = 0
    #framespeed is the number of iterations the sprite will stay on the same frame so 0=fastest animation
    flag = 0
    framespeed=4
    #jumping tells us if the player is jumping.
    jumping = False
    #isprone tells us if the player is prone.
    isprone = False
    #shooting tells us if the player is shooting
    shooting = False
    #aiming tells us which direction in which the player is aiming
    # Holds the cooldown of the shot being fired
    cooldown = 0
    aiming = "MID"
    #playerscale is the multiplier by which the size of the player sprite is increased
    playerscale = 3
    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    jumping_frames_l = []
    jumping_frames_r = []
    aim_up_running_r = []
    aim_up_running_l = []

    aim_mid_running_r = []
    aim_mid_running_l = []
    aim_down_running_r = []
    aim_down_running_l = []

    dead_anim = []

    idle_frame_l = None
    idle_frame_r = None
    prone_frame_r = None
    prone_frame_l = None

    direct_upaim_l = None
    direct_upaim_r = None
    # What direction is the player facing?
    direction = "R"
    bullet_list = pygame.sprite.Group()
    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("player1.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(324, 261, 30, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(358, 262, 26, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(388, 262, 24, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(414, 260, 33, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(451, 259, 38, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(324, 210, 39, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(367, 211, 36, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(408, 211, 32, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(444, 210, 28, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(476, 212, 35, 47)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(515, 212, 38, 47)
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
        image = sprite_sheet.get_image(323, 310, 35, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(362, 310, 34, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(402, 310, 32, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(439, 310, 31, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(474, 310, 29, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(509, 310, 29, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(544, 309, 29, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(324, 366, 36, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(368, 368, 38, 49)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(411, 365, 36, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(451, 365, 35, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(490, 365, 34, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(529, 365, 31, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(564, 365, 29, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(596, 365, 29, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(323, 417, 29, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(355, 417, 30, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(389, 417, 33, 51)
        self.aim_up_running_r.append(image)
        image = sprite_sheet.get_image(425, 422, 36, 51)
        self.aim_up_running_r.append(image)
        #load the sprites for aiming upwards whilst running left
        for x in self.aim_up_running_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.aim_up_running_l.append(image)

        #load the sprites for aiming downwards whilst running right
        image = sprite_sheet.get_image(323, 579, 40, 46)
        self.aim_mid_running_r.append(image)
        image = sprite_sheet.get_image(368, 575, 36, 46)
        self.aim_mid_running_r.append(image)
        image = sprite_sheet.get_image(406, 574, 35, 46)
        self.aim_mid_running_r.append(image)
        image = sprite_sheet.get_image(444, 574, 35, 46)
        self.aim_mid_running_r.append(image)

        for x in self.aim_mid_running_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.aim_mid_running_l.append(image)

        image = sprite_sheet.get_image(323, 472, 34, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(360, 473, 33, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(396, 473, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(431, 473, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(467, 473, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(502, 473, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(535, 472, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(568, 472, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(602, 472, 31, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(323, 523, 32, 45)
        self.aim_down_running_r.append(image)
        image = sprite_sheet.get_image(359, 528, 36, 45)
        self.aim_down_running_r.append(image)

        for x in self.aim_down_running_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.aim_down_running_l.append(image)

        image = sprite_sheet.get_image(323, 950, 29, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(355, 950, 28, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(386, 950, 32, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(421, 950, 38, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(462, 950, 38, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(503, 950, 37, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(543, 950, 32, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(578, 950, 32, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(613, 950, 29, 42)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(323, 998, 30, 30)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(355, 995, 33, 33)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(391, 997, 36, 31)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(430, 1010, 40, 18)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(473, 1017, 41, 11)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(323, 1031, 43, 11)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(369, 1032, 48, 10)
        self.dead_anim.append(image)
        image = sprite_sheet.get_image(420, 1033, 45, 9)
        self.dead_anim.append(image)

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

        self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.playerscale,self.image.get_height()*constants.playerscale))
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self, enemy_list):
        if (self.dead is False):
            self.calc_grav()
            """ Move the player. """
            self.bullet_list.update(self)
            # Gravity
            # Move left/right
            self.rect.x += self.change_x
            if self.jumping:
                self.framespeed = 2
                if self.direction == "L":
                    frame = (self.count) % len(self.jumping_frames_l)
                    self.image = self.jumping_frames_l[frame]
                else:
                    frame = (self.count) % len(self.jumping_frames_r)
                    self.image = self.jumping_frames_r[frame]
            elif(self.aiming == "UP"):
                if self.change_x != 0:
                    self.framespeed = 2
                    if self.direction == "L":
                        frame = (self.count) % len(self.aim_up_running_l)
                        self.image = self.aim_up_running_l[frame]
                    else:
                        frame = (self.count) % len(self.aim_up_running_r)
                        self.image = self.aim_up_running_r[frame]
                else:
                    self.framespeed = 4
                    if self.direction == "L":
                        self.image = self.direct_upaim_l
                    else:
                        self.image = self.direct_upaim_r
            elif(self.aiming == "DOWN"):
                if self.change_x != 0:
                    self.framespeed = 2
                    if self.direction == "L":
                        frame = (self.count) % len(self.aim_down_running_l)
                        self.image = self.aim_down_running_l[frame]
                    else:
                        frame = (self.count) % len(self.aim_down_running_r)
                        self.image = self.aim_down_running_r[frame]
                else:
                    if self.direction == "L":
                        self.image = self.prone_frame_l
                    else:
                        self.image = self.prone_frame_r
            elif(self.aiming == "MID"):
                self.framespeed = 3
                if self.change_x != 0:
                    if self.shooting is True:
                        if self.direction == "L":
                            frame = (self.count) % len(self.aim_mid_running_l)
                            self.image = self.aim_mid_running_l[frame]
                        else:
                            frame = (self.count) % len(self.aim_mid_running_r)
                            self.image = self.aim_mid_running_r[frame]
                    else:
                        if self.direction == "L":
                            frame = (self.count) % len(self.walking_frames_l)
                            self.image = self.walking_frames_l[frame]
                        else:
                            frame = (self.count) % len(self.walking_frames_r)
                            self.image = self.walking_frames_r[frame]
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
            self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.playerscale,self.image.get_height()*constants.playerscale))
            self.rect.height = self.image.get_height()

            #if on top of platform, stop jumping around

            #check bullet collisions

            # See if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:

                #if self.change_y == 0:
                if self.onPlatform == False:
                    if self.change_x>0:
                        self.rect.right = block.rect.left
                    elif self.change_x<0:
                        self.rect.left = block.rect.right

            # Move up/down
            self.rect.y += self.change_y

            # Check and see if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
                    # Reset our position based on the top/bottom of the object.
                    #THIS IS WHERE WE CODE LANDING ON PLATFORM
                    #previous moves player into platform
                    #when new collision occurs, as change_y is set to 1 re. calc_grav
                    #the player will move up

                if self.change_y > -1:
                    self.rect.bottom = block.rect.top
                    self.jumping = False
                    self.onPlatform = True

                elif self.change_y < 0:
                    pass
                    #self.rect.top = block.rect.bottom

                # Stop our vertical movement
                self.change_y = 0
            if self.shooting is True:
                if self.guncount%constants.PLAYERFIRERATE==0:
                    aimdirection = (0,0)
                    origin = (self.rect.x,self.rect.y)
                    if self.aiming == "UP":
                        if self.change_x!=0:
                            if self.direction == "L":
                                #spawn bullet travelling up and left
                                #vector will be (-1,-1)
                                aimdirection = (-1,-1)
                                origin = (self.rect.x,self.rect.y)
                            else:
                                #spawn bullet travelling up and right
                                #vector will be (1,-1)
                                aimdirection = (1,-1)
                                origin = (self.rect.x+self.rect.width,self.rect.y)
                        else:
                                #spawn bullet travelling upwards
                                #vector will be (0,-1)
                                aimdirection = (0,-1)
                                origin = (self.rect.x,self.rect.y)
                                if self.direction == "L":
                                    #spawn bullet travelling up character facing left
                                    origin = (self.rect.x+35,self.rect.y)
                                else:
                                    #spawn bullet travelling up character facing right
                                    origin = (self.rect.x+30,self.rect.y)
                    elif self.aiming == "MID":
                        if self.direction == "L":
                            #spawn bullet travelling left
                            #vector will be (-1,0)
                            aimdirection = (-1,0)
                            origin = (self.rect.x,self.rect.y+42)
                        else:
                            #spawn bullet travelling right
                            #vector will be (1,0)
                            aimdirection = (1,0)
                            origin = (self.rect.x+self.rect.width,self.rect.y+42)
                    elif self.aiming == "DOWN":
                        if self.change_x!=0:
                            if self.direction == "L":
                                #spawn bullet travelling down and left
                                #vector will be (-1,1)
                                aimdirection = (-1,1)
                                origin = (self.rect.x,self.rect.y+95)
                            else:
                                #spawn bullet travelling down and right
                                #vector will be (1,1)
                                aimdirection = (1,1)
                                origin = (self.rect.x+self.rect.width,self.rect.y+95)
                        else:
                            if self.direction == "L":
                                #spawn bullet travelling left
                                #vector will be (-1,0)
                                aimdirection = (-1,0)
                                origin = (self.rect.x,self.rect.y+2+self.rect.width/3)
                            else:
                                #spawn bullet travelling right
                                #vector will be (1,0)
                                aimdirection = (1,0)
                                origin = (self.rect.x+self.rect.width+50,self.rect.y+2+self.rect.width/3)
                    self.bullet_list.add(Bullet(origin,(aimdirection[0]*8,aimdirection[1]*8),1, self.level))
                    for b in self.bullet_list:
                        if b.count >600:
                            self.bullet_list.remove(b)
            self.guncount = self.guncount+1

            for enemy in enemy_list:
                if enemy.type ==0:
                    if(self.rect.colliderect(enemy.rect)):
                        self.lives-=1
                        self.deathcount+=1
                        self.dead = True
                        self.change_y=-10
                        enemy.rect.x+=(constants.SCREEN_WIDTH)
                        enemy.bullet_list = pygame.sprite.Group()
                        self.bullet_list = pygame.sprite.Group()
                else:
                    block_hit_list = pygame.sprite.spritecollide(self,enemy.bullet_list,False)
                    for block in block_hit_list:
                        self.lives-=1
                        self.deathcount+=1
                        self.dead = True
                        enemy.bullet_list = pygame.sprite.Group()
                        self.bullet_list = pygame.sprite.Group()
                        self.change_y=-10

        else:
            if(self.deathcount<120):
                self.calc_grav()
                self.rect.y+=self.change_y
                if self.rect.x<121:
                    self.change_x=0
                else:
                    self.change_x=-constants.SCREEN_WIDTH/120
                    self.rect.x+=self.change_x

                if(self.deathcount<51):
                    if(self.deathcount==0):
                        self.image = self.dead_anim[0]
                        self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.playerscale,self.image.get_height()*constants.playerscale))
                        self.rect.height = self.image.get_height()
                        self.calc_grav()
                    elif(self.deathcount%3==0):
                        frame = self.deathcount/3
                        self.image = self.dead_anim[int(frame)]
                        self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.playerscale,self.image.get_height()*constants.playerscale))
                        self.rect.height = self.image.get_height()
                        self.calc_grav()
                else:
                    self.image = self.dead_anim[len(self.dead_anim)-1]
                    self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.playerscale,self.image.get_height()*constants.playerscale))
                    self.rect.height = self.image.get_height()
                    self.calc_grav()
            #Death animation
            else:
                #move the player back
                self.deathcount = 0
                self.dead = False
                self.change_x=0
            self.deathcount+=1

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1

        else:
            self.change_y += .35

        # See if we are on the ground.

        if (self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0):
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            self.jumping = False
            self.onPlatform = False

        if self.prone == True:
            self.rect.y = self.rect.y + 10

    def jump(self):
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        self.jumping = True
        self.onPlatform = False
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -15

    def shoot(self): #To be called with the user hits the shoot button, "x"?
        self.shooting=True
        self.guncount = 0

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

    def prone(self):
        self.aiming = "DOWN"

    def aimup(self):
        self.aiming = "UP"

    def resetaim(self):
        self.aiming = "MID"

    def stopshooting(self):
        self.shooting=False
