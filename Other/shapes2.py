shapeIds = []

class Shape:

    id

    def __init__(self):
        pass
        self.id = self.generateId()

    def generateId(self):
        global shapeIds
        newId = 1
        foundNew = False
        while foundNew == False:
            if newId in shapeIds:
                newId += 1
            else:
                foundNew = True

        shapeIds.append(newId)
        return newId


    def draw(self):
        print("Drawing a shape with id {}".format(self.id))

class Circle(Shape):

    def draw(self):
        print("Drawing a circle with id {}".format(self.id))

class Square(Shape):

    def draw(self):
        print("Drawing a square with id {}".format(self.id))

shapelist = []
shapelist.append(Shape())
shapelist.append(Circle())
shapelist.append(Square())
shapelist.append(Circle())


for item in shapelist:
    item.draw()