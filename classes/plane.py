# ceci est un avion

from constants import *

class Plane():
    """
    Avion
    """
    def __init__(self, color, speed, length, width):
       self.speed = speed
       self.color = COLOR[color]
       self.length = length
       self.width = width
