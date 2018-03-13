import constants
from vector import Vector


class Bullet:
    """"Takes in two vectors and an integer at initialisation. First vector is current position of the character, second
    vector is the direction of the bullet"""
    def __init__(self, p, d, t):
        self.position = p
        self.direction = d
        self.destroyed = False
        """1 = Standard, 2 = Bouncy (will reflect off platforms/walls, 3= Shotgun (slightly weaker bullet, to be shot in
        groups), 4 = Grenade (travels in a parabola then damages enemies in a radius after a set time)"""
        self.type = t
        if self.type == 2:
            self.bounces=5
    """Bullets will be sorted into two arrays - player and enemy bullets. If"""
    def draw(self, canvas):
        if self.destroyed is False:
            canvas.draw.circle(constants.WHITE, self.position, 3, 0)
    """Bullet will travel in set direction until it interacts with a character"""
    def update(self):
        self.position.add(self.direction)
        if self.type == 2:
            if self.bounces == 0:
                self.destroyed = True
            else:
                "Code for dealing with reflecting off platforms"
        if self.type == 4:
            self.position.subtract(Vector(0, constants.GRAVITY))
