from  __future__ import print_function
class Shape: #parents
    def __init__(self):
        self.Color = "red"
        self.Sides = 0

    def calArea(self):
            return 0
class Square(Shape): #child
    def __init__(self,w,c): #method overwritinf function
        Shape.__init__(self)
        self.width = w
        self.color = c
class Circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius = r
        self.Color = c

sq1 = Square(5,"Green")
sq2 = Square(9,"Black")
c1 = Circle(10,"Orange")

print("Square Size",sq1.width,"X",
      sq1.Sides,sq1.Color,",",sq2.width,
      "X",sq2.Sides,sq2.Color)
print("Circle",c1.radius,c1.Color)

print(sq1.calArea())
print(c1.calArea())