import math

class Node:

    def __init__(self, id, x, y, radius = 20):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius

    def contains_point(self, px, py):
        distance = math.sqrt((self.x - px)**2 + (self.y - py)**2)
        return distance <= self.radius

