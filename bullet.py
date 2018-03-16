import constants
from vector import Vector
import main


class Bullet:
    """"Takes in two vectors and an integer at initialisation. First vector is current position of the character, second
    vector is the direction of the bullet"""
    def __init__(self, p, d, t):
        self.pos = p
        self.direction = d
        self.destroyed = False
        """1 = Standard, 2 = Bouncy (will reflect off platforms/walls, 3= Shotgun (slightly weaker bullet, to be shot in
        groups), 4 = Grenade (travels in a parabola then damages enemies in a radius after a set time)"""
        self.type = t
        if self.type == 2:
            self.bounces=5

        main.bullet_list.add(self)

    def draw(self, canvas):
        if self.destroyed is False:
                canvas.draw_circle(constants.WHITE, self.pos, self.radius, 0)
    """Bullet will travel in set direction until it interacts with a character"""

    def update(self):
        self.pos.add(self.direction)
        if self.type == 2:
            if self.bounces == 0:
                self.destroyed = True
            else:
                """Bouncy bullets are all coded algorithmically, just need sprites and retexturing """
                block_hit_list = pygame.sprite.spritecollide(self,Level.levels.platform_list, False)
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
