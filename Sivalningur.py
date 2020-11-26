from Form import Form
from math import pi
class Sivalningur(Form):
    def __init__(self,radius, height):
        Form.__init__(self,radius)
        self.height = height

    def Flatarmal(self):
        r = self.radius
        h = self.height
        return round(2*pi*r*h+2*pi*r**2, 3)

    def Rummal(self):
        r = self.radius
        h = self.height
        return round(pi*r**2*h, 3)
