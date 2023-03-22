import math
class Rocket:

    def __init__(self, name, paliwo, x=0, y=0):
        self.x = x
        self.y = y
        self.name = name
        self.paliwo = paliwo

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.paliwo -= math.sqrt(dx**2 + dy**2)

    def get_position(self):
        return (self.x, self.y, self.name)

    def get_distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (math.sqrt(dx**2 + dy**2), self.name, other.name)
