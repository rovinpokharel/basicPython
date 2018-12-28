class Shape: #parents
    def __init__(self):
        self.Color = "red"
        self.Sides = 0
class Square(Shape): #child
    def __init__(self,w): #method overwritinf function
        Shape.__init__(self)
        self.width = w

sq1 = Square(5)
sq2 = Square(9)

print("Square Size",sq1.width,"X",
      sq1.Sides,sq1.Color,",",sq2.width,
      "X",sq2.Sides,sq2.Color)