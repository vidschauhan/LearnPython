# Created by vidit.singh at 04-03-2022

# Q1.  LIne class takes pair of tuple and return the slope and distance of the line.

class Line:

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):
        from math import sqrt
        c1 = (self.cord2[0] - self.cord1[0]) ** 2
        c2 = (self.cord2[1] - self.cord1[1]) ** 2
        return sqrt(c1 + c2)

    def slope(self):
        return (self.cord2[1] - self.cord1[1]) / (self.cord2[0] - self.cord1[0])


coord1 = (3, 2)
coord2 = (8, 10)

line = Line(coord1, coord2)
print(line.distance())
print(line.slope())
