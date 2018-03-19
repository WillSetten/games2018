import pygame
import constants
import levels
from spritesheet_functions import SpriteSheet
import random
import time
class PowerUp(pygame.sprite.Sprite):
    type = 2
    level = None
    change_y=0
    def __init__(self,type):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("assets\\powerups.png")
        super().__init__()
        self.type = type
        if(type == 4):
            self.image = sprite_sheet.get_image(1,1,26,18)
            self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.powerupscale,self.image.get_width()*constants.powerupscale))
        elif(type == 3):
            self.image = sprite_sheet.get_image(2,21,25,10)
            self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.powerupscale,self.image.get_width()*constants.powerupscale))
        else:
            self.image = sprite_sheet.get_image(1,34,20,12)
            self.image = pygame.transform.scale(self.image,(self.image.get_width()*constants.powerupscale,self.image.get_width()*constants.powerupscale))
        self.rect = self.image.get_rect()
    def update(self,player):
        self.calc_grav()
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
        self.rect.y += self.change_y
        if player.rect.x >= 500:
            diff = player.rect.x-500
            self.rect.x+=-diff

        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            self.rect.x+=diff
        if(self.rect.colliderect(player.rect)):
            if(self.type == 4):
                player.changebullet4()
            elif(self.type ==3):
                player.changebullet3()
            else:
                player.changebullet2()
            self.rect.x = self.rect.x -2000
            print("Picked up powerup type "+str(self.type))

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
    def spawn(self,x,y):
        self.rect.x = x
        self.rect.y = y
