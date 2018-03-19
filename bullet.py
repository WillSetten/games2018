import constants
import pygame
from vector import Vector
from spritesheet_functions import SpriteSheet

class Bullet(pygame.sprite.Sprite):
    """"Takes in two vectors and an integer at initialisation. First vector is current rectition of the character, second
    vector is the direction of the bullet"""
    level = None
    type=1
    """Count is used to track number of frames that the bullet is active for - if over x amount bullet despawns"""
    count=0
    bounces = 5
    change_x=0
    change_y=0
    def __init__(self, p, d, t, level):
        self.level=level
        if(t==4):
            self.change_x = d[0]*5
            self.change_y = d[1]*6
        self.change_x = d[0]
        self.change_y = d[1]
        self.destroyed = False
        """0=Enemy bullets 1 = Standard, 2 = Bouncy (will reflect off platforms/walls, 3= Rapid Fire, 4 = Grenade (travels in a parabola then damages enemies in a radius after a set time)"""
        self.type = t
        if self.type == 2:
            self.bounces=5
        super().__init__() #adding super call to make Bullet a pygame Sprite
        self.image = pygame.Surface([10, 10])
        sprite_sheet = SpriteSheet("assets\\bullets.png")
        if self.type == 0:
            self.image = sprite_sheet.get_image(0,0,10,10)
        else:
            self.image = sprite_sheet.get_image(10,0,10,10)
            if self.type == 4:
                self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
    """Bullets will be sorted into two arrays - player and enemy bullets. If"""
    def draw(self, canvas):
        if self.destroyed is False:
            canvas.draw_circle(constants.WHITE, self.rect, self.radius, 0)
    """Bullet will travel in set direction until it interacts with a character"""
    def update(self,player):
        """self.count increments so that each bullet is on screen for no more than 10 seconds"""
        block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list, False)
        if self.count<600:
            self.rect.x = self.rect.x+self.change_x
            self.rect.y = self.rect.y+self.change_y
            if player.rect.x >= 500:
                diff = player.rect.x-500
                self.rect.x-=diff

            if player.rect.x <= 120:
                diff = 120 - player.rect.x
                self.rect.x+=diff

            if self.type == 2 or self.type == 4:
                if self.type == 4:
                    self.change_y += .35
                if self.bounces == 0:
                    self.destroyed = True
                else:
                    if self.rect.y > constants.SCREEN_HEIGHT or self.rect.y < 0:
                            self.change_y = -self.change_y
                            self.bounces -= 1
                    elif self.rect.x < 0:
                            self.change_x = -self.change_x
                            self.bounces -= 1
                    for block in block_hit_list:
                        if self.rect.y > block.rect.top and self.rect.y < block.rect.bottom:
                            self.change_y = -self.change_y
                            self.bounces -= 1
                        elif self.rect.x > block.rect.left and self.rect.x < block.rect.right:
                            self.change_x = -self.change_x
                            self.bounces -= 1
            self.count+=1
        else:
            self.rect.x = -100
            self.rect.y = -100
            self.direction = (0,0)
