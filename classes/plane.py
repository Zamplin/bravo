# ceci est un avion

from constants import *

class Plane():
    """
    Avion
    """
    def __init__(self, color, speed, lengh, width):
       self.speed = speed
       self.color = COLOR[color]
       self.lengh = lengh
       self.width = width
