import pygame
import random
import levels
import constants
from vector import Vector
from spritesheet_functions import SpriteSheet
class Enemy(pygame.sprite.Sprite):
    #Attributes
    #Melee type animations
    walk_r = []
    walk_l = []
    die_M_r = []
    die_M_l = []
    #Ranged type frames
    up_r=None
    up_l= None
    upangle_r = None
    upangle_r = None
    mid_r = None
    mid_l = None
    downangle_r = None
    downangle_l = None
    down_r = None
    down_l = None
    die_R_r = []
    die_R_l = []
    count = 0
    location = 0
    onPlatform = False
    change_x = 0
    change_y = 0
    level = None
    direction = "L"
    health = 0
    type = 0
    flag=0
    framespeed = 4
    nokill=True
    def __init__(self, type):

        pygame.sprite.Sprite.__init__(self)

        self.type = type

        sprite_sheet = SpriteSheet("enemies1.png")
        image = sprite_sheet.get_image(321, 1, 32, 47)
        self.walk_r.append(image)
        image = sprite_sheet.get_image(356, 1, 21, 47)
        self.walk_r.append(image)
        image = sprite_sheet.get_image(380, 1, 28, 47)
        self.walk_r.append(image)
        image = sprite_sheet.get_image(411, 1, 38, 47)
        self.walk_r.append(image)
        image = sprite_sheet.get_image(452, 1, 36, 47)
        self.walk_r.append(image)
        image = sprite_sheet.get_image(491, 1, 28, 47)
        self.walk_r.append(image)
        image = sprite_sheet.get_image(522, 1, 21, 47)
        self.walk_r.append(image)
        image = sprite_sheet.get_image(546, 1, 32, 47)
        self.walk_r.append(image)
        image = sprite_sheet.get_image(581, 1, 37, 47)
        self.walk_r.append(image)
        for x in self.walk_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.walk_l.append(image)

        self.up_r=sprite_sheet.get_image(321, 246, 25, 60)
        self.up_l=pygame.transform.flip(self.up_r, True, False)
        self.upangle_r = sprite_sheet.get_image(405, 250, 31, 56)
        self.upangle_r = pygame.transform.flip(self.up_r, True, False)
        self.mid_r = sprite_sheet.get_image(507, 261, 36, 45)
        self.mid_l = pygame.transform.flip(self.up_r, True, False)
        self.downangle_r = sprite_sheet.get_image(321, 312, 32, 45)
        self.downangle_l = pygame.transform.flip(self.up_r, True, False)
        self.down_r = sprite_sheet.get_image(426, 312, 25, 45)
        self.down_l = pygame.transform.flip(self.up_r, True, False)

        image = sprite_sheet.get_image(528, 216, 49, 38)
        self.die_R_r.append(image)
        image = sprite_sheet.get_image(528, 178, 49, 38)
        self.die_R_r.append(image)
        for x in self.die_R_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.die_R_l.append(image)

        image = sprite_sheet.get_image(321, 109, 37, 39)
        self.die_M_r.append(image)
        image = sprite_sheet.get_image(358, 109, 37, 39)
        self.die_M_r.append(image)
        for x in self.die_M_r[:]:
            image = x
            image = pygame.transform.flip(image, True, False)
            self.die_M_l.append(image)

        #0 = Melee 1 = Ranged
        if (self.type==0):
            self.speed = 4
            self.health = 1
            self.pos = Vector(0,0)
            self.image = self.walk_l[0]

        elif (self.type==1):
            self.health = 3
            self.pos = Vector(0,0)
            self.sprite = None
            self.image = self.mid_l
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.enemyscale,self.image.get_height()*constants.enemyscale))
        self.rect = self.image.get_rect()

    def update(self, player):
        if (self.health<1):
            #death animation
            if (self.type==0):
                if self.direction == "R":
                    frame = (self.count) % len(self.die_M_r)
                    self.image = self.die_M_r[frame]
                else:
                    frame = (self.count) % len(self.die_M_l)
                    self.image = self.die_M_l[frame]
            else:
                if self.direction == "R":
                    frame = (self.count) % len(self.die_R_r)
                    self.image = self.die_R_r[frame]
                else:
                    frame = (self.count) % len(self.die_R_l)
                    self.image = self.die_R_l[frame]
        else:
            if (self.type==0):
                self.move(player)
                if(self.direction =="R"):
                    frame = (self.count) % len(self.walk_r)
                    self.image = self.walk_r[frame]
                else:
                    frame = (self.count) % len(self.walk_l)
                    self.image = self.walk_l[frame]
                if(self.rect.colliderect(player.rect)):
                    self.nokill=False
                self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.enemyscale,self.image.get_height()*constants.enemyscale))
            elif(self.type==1):
                self.calc_grav()
                if(self.count%constants.ENEMYFIRERATE==0):
                    aim_direction = Vector(self.rect.x-(player.rect.x+player.change_x),self.rect.y-(player.rect.y+player.change_y))
                    compare = self.normaliseAngle(aim_direction.angle(Vector(0,self.rect.y)))
                    if compare=="0,-1":
                        if self.direction == "R":
                            self.image = self.up_r
                        else:
                            self.image = self.up_l
                    if compare=="1,-1":
                        self.direction = "R"
                        self.image = self.upangle_r
                    if compare=="1,0":
                        self.direction = "R"
                        self.image = self.mid_r
                    if compare=="1,1":
                        self.direction = "R"
                        self.image = self.downangle_r
                    if compare=="0,1":
                        if self.direction == "R":
                            self.image = self.down_r
                        else:
                            self.image = self.down_l
                    if compare=="-1,1":
                        self.direction = "L"
                        self.image = self.upangle_l
                    if compare=="-1,0":
                        self.direction = "L"
                        self.image = self.mid_l
                    if compare=="-1,-1":
                        self.direction = "L"
                        self.image = self.downangle_l
                        #add a bullet to the enemy bullet list in main travelling in the direction aim_direction
                    self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.enemyscale,self.image.get_height()*constants.enemyscale))
        if self.flag == 0:
            self.count += 1
            self.flag=self.framespeed
        else:
            self.flag-=1
    def spawn(self,x,y):
        self.rect.x = x
        self.rect.y = y


    def move(self, player):
        #gives them gravity physics so they fall if spawn in the sky
        self.calc_grav()

        #sets them to follow the user wherever they go
        if(self.nokill):
            if player.rect.x > self.rect.x:
                self.change_x = self.speed
                self.direction = "R"
            else:
                self.change_x = -self.speed
                self.direction = "L"
        else:
            self.change_x = -self.speed
        self.rect.x+=self.change_x

    #NEXT SECTION: collisions with platforms, means that enemies can sit on platforms if they wish to do so
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            #stops left/right collisions with platforms when on the ground
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
            #if they collide with a platform, this stops user and makes them stand on top

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.jumping = False
                self.onPlatform = True

            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

        #only triggered if the enemy type is infantry
        #if distance between enemy and player is less than x
        #attack user - infantry attack needs to be run

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

    def decreaseHealth(self):
        pass

    def normaliseAngle(self,angle):
        if(angle>22.5 or angle<=67.5):
            return "1,-1"
        if(angle>67.5 or angle<=112.5):
            return "1,0"
        if(angle>112.5 or angle<=157.5):
            return "1,1"
        if(angle>157.5 or angle<=202.5):
            return "0,1"
        if(angle>202.5 or angle<=247.5):
            return "-1,1"
        if(angle>247.5 or angle<=292.5):
            return "-1,0"
        if(angle>292.5 or angle<=337.5):
            return "-1,-1"
        else:
            return "0,-1"
