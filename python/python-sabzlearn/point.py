import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("The point is at position " + str(self.x) + " and " + str(self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def distance(self, other):
        return math.sqrt(pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2))


p1 = Point(4, 5)
p2 = Point(7, 9)

p1.show()
p2.show()

p3 = p1 + p2
p3.show()

print("The distance between two points is " + str(p1.distance(p2)))
