class Shape:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return color
    def area(self):
        pass
        
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

rec = Rectangle("red", 2, 3)
cir = Circle("Blue", 2)

print(rec.area())
print(cir.area())
