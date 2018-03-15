import pygame
import random
import levels
import constants
from vector import Vector
from spritesheet_functions import SpriteSheet

class Enemy(pygame.sprite.Sprite):
    location = 0
    def __init__(self, type):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("enemies1.png")

        if (type=="Infantry"):
            self.health = 1
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = None #set as null for now while working on other areas
        elif (type=="Heavy"):
            self.health = 3
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = None
        else:
            self.health = 40
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = None

        self.image = sprite_sheet.get_image(30,0,60,40)
        self.rect = self.image.get_rect()

    def update(self):
        if (self.health>0):
            if (self.type=="Infantry"):
                self.move()
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

    def move(self):
        self.pos.x=self.pos.x+1
        #only triggered if the enemy type is infantry
        #if distance between enemy and player is less than x
        #attack user - infantry attack needs to be run

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
