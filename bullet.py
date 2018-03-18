import constants
import pygame
from vector import Vector


class Bullet(pygame.sprite.Sprite):
    """"Takes in two vectors and an integer at initialisation. First vector is current position of the character, second
    vector is the direction of the bullet"""
    level = None
    type=1
    """Count is used to track number of frames that the bullet is active for - if over x amount bullet despawns"""
    count=0
    bounces = 5
    def __init__(self, p, d, t, level):
        self.level=level
        self.direction = d
        self.destroyed = False
        """0=Enemy bullets 1 = Standard, 2 = Bouncy (will reflect off platforms/walls, 3= Rapid Fire, 4 = Grenade (travels in a parabola then damages enemies in a radius after a set time)"""
        self.type = t
        if self.type == 2:
            self.bounces=5
        super().__init__() #adding super call to make Bullet a pygame Sprite
        self.image = pygame.Surface([10, 10])
        self.rect = self.image.get_rect()
        if self.type == 0:
<<<<<<< HEAD
            self.image = sprite_sheet.get_image(0,0,10,10)
        else:
            self.image = sprite_sheet.get_image(10,0,10,10)
=======
            self.image.fill(constants.WHITE)
        if self.type == 1:
            self.image.fill(constants.PINK)
>>>>>>> d5304ee1b4ade8917b15262eee219d6ed46fd4f6
        self.rect.x=p[0]
        self.rect.y=p[1]
    """Bullets will be sorted into two arrays - player and enemy bullets. If"""
    def draw(self, canvas):
        if self.destroyed is False:
            canvas.draw_circle(constants.WHITE, self.pos, self.radius, 0)
    """Bullet will travel in set direction until it interacts with a character"""
    def update(self,player):
        """self.count increments so that each bullet is on screen for no more than 10 seconds"""
        if self.count<600:
            self.rect.x = self.rect.x+self.direction[0]
            self.rect.y = self.rect.y+self.direction[1]
            if player.rect.x >= 500:
                diff = player.rect.x-500
                self.rect.x+=-diff

            if player.rect.x <= 120:
                diff = 120 - player.rect.x
                self.rect.x+=diff

            if self.type == 2:
                if self.bounces == 0:
                    self.destroyed = True
                else:
                    block_hit_list = pygame.sprite.spritecollide(self,self.level.platform_list, False)
                    if block_hit_list == None:
                        if self.pos.y == constants.SCREEN_HEIGHT or self.pos.y == 0:
                            self.direction.y = -self.direction.y
                        elif self.pos.x == constants.SCREEN_WIDTH or self.pos.x == 0:
                            self.direction.x = -self.direction.x
                    for block in block_hit_list:
                        if self.pos.y == block.rect.top or self.pos.y == block.rect.bottom:
                            self.direction.y = -self.direction.y
                        else:
                            self.direction.x = -self.direction.x

                    self.bounces -= 1
            "Code for dealing with reflecting off platforms"
            if self.type == 4:
                self.pos.subtract(Vector(0, constants.GRAVITY))
            self.count+=1
        else:
            self.rect.x = -100
            self.rect.y = -100
            self.direction = (0,0)
