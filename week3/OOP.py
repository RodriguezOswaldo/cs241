class Point:
    """Point class for representing and manipulating "x,y" coordinates."""

    def __init__(self, initX, initY):
        """Create a new point at the origin."""
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(7, 6)  # Instantiate an object of type Point
print(p.distanceFromOrigin())
print(p.getX())
print(p.getY())
