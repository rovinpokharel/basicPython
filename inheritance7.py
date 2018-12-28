from  __future__ import print_function
import math

class Shape: #parents
    def __init__(self):
        self.Color = "red"
        self.Sides = 0

    def calArea(self):
            return 0

class Quadilateral(Shape):
    def __init__(self,w,l,c):
        self.sides = 4
        self.width = w
        self.length = l
        self.Color = c

    def calArea(self):
        return self.width*self.length

class Square(Quadilateral):
    def __init__(self,w,c):
        Quadilateral.__init__(self,w,w,c)

class Circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius = r
        self.Color = c
    def calArea(self):
        return self.radius**2*math.pi

class Triangle(Shape):
    def __init__(self,s1,s2,s3,c):
        Shape.__init__(self)
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.Color = c

def printArea(s):
    print(s.calArea())

sq1 = Square(5,"Green")
sq2 = Square(9,"Black")
c1 = Circle(10,"Orange")
t1 = Triangle(3,4,5,"Purple")

print("Square Size",sq1.width,"X",
      sq1.Sides,sq1.Color,",",sq2.width,
      "X",sq2.Sides,sq2.Color)
print("Circle",c1.radius,c1.Color)

print(sq1.calArea())
print(c1.calArea())
print("Triangle Area:",printArea(t1))