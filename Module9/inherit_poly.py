import math


class shape:
    def area(self):
        pass


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class rectangle(shape):
    def __init__(self, width, hight):
        self.width = width
        self.height = hight

    def area(self):
        return self.width * self.width


class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class parallelogram(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


rrethi = circle(2)
drejtkendshi = rectangle(3,4)
trekendeshi = triangle(6,4)
paralelogrami = parallelogram(5, 3)

print(rrethi.area())
print(drejtkendshi.area())
print(trekendeshi.area())
print(paralelogrami.area())


