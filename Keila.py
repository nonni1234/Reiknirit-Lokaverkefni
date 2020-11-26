from Form import Form
from math import pi,sqrt

class Keila(Form):
    def __init__(self,radius, height):
        Form.__init__(self,radius)
        self.height = height

    def Flatarmal(self):
        r = self.radius
        h = self.height
        return round(pi*r*(r+sqrt(h**2+r**2)), 3)

    def Rummal(self):
        r = self.radius
        h = self.height
        return round(pi*r**2*h/3, 3)
