import pickle
import math

class Shape:
    def __init__(self):
        self.info = {}

    def show(self):
        print(self.info)

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.info, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as f:
            return cls(**pickle.load(f))


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__()
        self.info = {'shape': 'Square', 'x': x, 'y': y, 'side': side}


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.info = {'shape': 'Rectangle', 'x': x, 'y': y, 'width': width, 'height': height}


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.info = {'shape': 'Circle', 'x': x, 'y': y, 'radius': radius}

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        return Circle(self.x, self.y, self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.x, self.y, self.radius - other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __isub__(self, other):
        self.radius -= other.radius
        return self


class Ellipse(Shape):
    def __init__(self, x1, y1, width2, height2):
        super().__init__()
        self.info = {'shape': 'Ellipse', 'x1': x1, 'y1': y1, 'width2': width2, 'height2': height2}


shapes = [Square(0, 0, 10), Rectangle(10, 10, 5, 5), Circle(15, 15, 3), Ellipse(20, 20, 4.5, 6.7)]

for shape in shapes:
    shape.save('shapes.pkl')

loaded_shapes = []
for i in range(len(shapes)):
    loaded_shapes.append(Shape.load('shapes.pkl'))

for shape in loaded_shapes:
    shape.show()

circle1 = Circle(0.0, 0.0, 5)
circle2 = Circle(10.0, 10.0, 5)

print(circle1 == circle2)  
print(circle1 > circle2)
print(circle1 <= circle2)
print(circle1 >= circle2)

new_circle = circle1 + circle2
print(new_circle.radius)
circle1 -= circle2
print(circle1.radius)

circle1 += circle2
print(circle1.radius)
circle1 -= circle2
print(circle1.radius)
