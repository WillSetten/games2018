import pygame
import random
import levels
import constants
from vector import Vector
from spritesheet_functions import SpriteSheet

class Enemy(pygame.sprite.Sprite):

    #Attributes
    location = 0
    onPlatform = False
    change_x = 0
    change_y = 0
    level = None

    def __init__(self, type):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("enemies1.png")

        if (type=="Infantry"):
            self.speed = 1
            self.health = 1
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = None #set as null for now while working on other areas
        elif (type=="Heavy"):
            self.speed = 0.5
            self.health = 3
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = None
        else:
            self.speed = 0.02
            self.health = 40
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = None

        self.image = sprite_sheet.get_image(30,0,30,40)#
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.enemyscale,self.image.get_height()*constants.enemyscale))
        self.rect = self.image.get_rect()

    def update(self, player):
        if (self.type=="Infantry"):
            self.move(player)
            self.checkIfHit()

        else:
            self.attack()
            self.checkIfHit()

    def spawn(self,x,y):
        self.rect.x = x
        self.rect.y = y


    def attack(self):
        pass
            #work out vector from enemy to player
            #fire shot, work out sprite/object to be fired
            #need to consider power ups etc.

    def move(self, player):
        #gives them gravity physics so they fall if spawn in the sky
        self.calc_grav()

        #sets them to follow the user wherever they go
        if player.rect.x > self.rect.x:
            self.change_x = self.speed
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

    def checkIfHit(self):
    #need to set up code to work out whether enemy has been hit or not
    #    block_hit_list = pygame.sprite.spritecollide(self, levels.Level.platform_list, False)
    #    if block_hit_list != None:

    #IF (Enemy has been hit)
        self.health=self.health-1
        if (self.health<1):
            self.remove()
        #if the enemy is dead, remove it from the game
            if (self.type=="Boss"):
                pass
            #score = score + 5000
            elif (self.type=="Heavy"):
                pass
                #score = score + 500
            else:
                pass
                    #score = score + 100
            #increment score since the user has killed an enemy
        #potentially display different sprite if hit / blur sprite for x amount of time to indicate hit

    def remove(self):
        self.sprite = None #set to a blank sprite so it no longer appears
        #will run if the enemy is dead, to remove them from the environment
