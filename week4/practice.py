import math

class Point:

    def __init__(self, initX, initY):
        """Create a new point at the given coordinates."""
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.getX() ** 2) + (self.getY() ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


def distance(point1, point2):
    x_diff = point2.getX() - point1.getX()
    y_diff = point2.getY() - point1.getY()
    dist = math.sqrt(x_diff**2 + y_diff**2)
    return dist


# first object
p = Point(7, 6)
q = Point(0, 0)
print(p.distanceFromOrigin())
print(distance(p, q))
print(p)
