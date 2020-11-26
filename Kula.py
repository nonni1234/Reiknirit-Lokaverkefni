from Form import Form
from math import pi
class Kula(Form):
    def __init__(self,radius):
        Form.__init__(self,radius)

    def Flatarmal(self):
        return round(4*pi*self.radius**2, 3)

    def Rummal(self):
        return round(4/3*pi*self.radius**3, 3)
