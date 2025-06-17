from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.__name=name
        self.__age=age
        self.__weight=weight
        self.__height=height

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.name = name
        self.__name = self.name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.age = age
        self.__age = self.age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.weight = weight
        self.__weight = self.weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.height = height
        self.__height = self.height

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    @abstractmethod
    def print_info(self):
        pass

class Adult(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)

    def calculate_bmi(self):
        return (self.weight / self.height) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if (bmi < 19.5):
            print("Underweight")
        elif (18.5 <= bmi > 24.9):
            print("Normal")
        elif (24.9 < bmi > 29.9):
            print("Overweight")
        else:
            print("Obese")

    def print_info(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Weight": self.weight,
            "Height": self.height,
        }


class Child(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)

    def calculate_bmi(self):
        return  (self.weight / self.height)*1.3

    def get_bmi_category(self):
        bmi=self.calculate_bmi()
        if (bmi < 14):
            print("Underweight")
        elif (14.4<bmi>18):
            print("Normal")
        elif (28 <= bmi > 29.9):
            print("Overweight")
        else:
            print("Obese")

    def print_info(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Weight": self.weight,
            "Height": self.height,
        }

# adult1=Adult("John", 46, 195, 106)
# print(adult1.print_info())
# print(adult1.calculate_bmi())
# adult1.get_bmi_category()
#
#
# kid1=Child("John", 16, 175, 66)
# print(kid1.print_info())
# print(kid1.calculate_bmi())
# kid1.get_bmi_category()


class BMI_app(Person):
    def __init__(self):
        self.person = []


    def add_person(self, person):
        person.append("Name")
