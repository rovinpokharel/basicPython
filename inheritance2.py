from __future__ import print_function

class Shape: #parents
    def __init__(self):
        self.Color = "red"
        self.Sides = 0
class Square(Shape): #child
    def __init__(self,w,c): #method overwritinf function
        Shape.__init__(self)
        self.width = w
        self.Color = c

sq1 = Square(5,"green")
sq2 = Square(9,"black")

print("Square Size",sq1.width,"X",
      sq1.Sides,sq1.Color,",",sq2.width,
      "X",sq2.Sides,sq2.Color)