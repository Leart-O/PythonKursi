from abc import ABC, abstractmethod


class ClassName(ABC): #this is the final definition of an abstract class
    pass

class Shape(ABC):#KLAS ABSTRAKTE
    #metod abstrakte
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius

class Square(Shape):
    def __init__(self, a):
        self.a=a
    def area(self):
        return self.a*self.a

#objektet per keto dy klasa
circle_1=Circle(7)
square_1=Square(18)

print(circle_1.area())
print(square_1.area())

#klasat abstrakte mund te kene edhe metoda te thjeshta edhe abstrakte
#interface jane klasa abstrakte qe kane vetem metoda abstrakte