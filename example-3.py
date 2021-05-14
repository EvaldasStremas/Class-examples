class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")
    
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        # Polygon.display_info(self)
        super().display_info()

class Quadilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5, 6, 7])
t1_perimeter = t1.get_perimeter()
print("The perimeter is:", t1_perimeter)
t1.display_info()

t2 = Quadilateral([2, 3, 2, 3])
t2_perimeter = t2.get_perimeter()
print("The perimeter is:", t2_perimeter)