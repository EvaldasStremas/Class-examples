
class Shape:

    drawType = "BasicShape"

    def draw(self):
        print("Drawing a: {}".format(self.drawType))

class Circle(Shape):

    def __init__(self):
        self.drawType = "Circle"

class Square(Shape):

    def __init__(self):
        self.drawType = "Square"

shapelist = []
shapelist.append(Shape())
shapelist.append(Circle())
shapelist.append(Square())

for i in shapelist:
    i.draw()