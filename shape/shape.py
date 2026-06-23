class shape:
    def __init__(self, areas):
        self.areas = areas


class Circle(shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14*self.r**2


class Rectangle(shape):
    def __init__(self, d, h):
        self.d = d
        self.h = h

    def area(self):
        return self.h*self.d


class Triangle(shape):
    def __init__(self, d, h):
        self.d = d
        self.h = h

    def area(self):
        return self.d*self.h//2


c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)
print(c.area())
print(r.area())
print(t.area())
