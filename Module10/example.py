#decorators getters and setters
class Student:
    def __init__(self,name,age): #konstruktori i klases e clia eshte pjesa qe beher run e para
        self.__name=name #ketu deklarohen te gjitha atributet e klases
        self.__age=age
    # deklarimi i metodes get
    @property
    def name(self):
        return self.__name

    #deklarimi i metodes set

    @name.setter
    def name(self, name):
        self.__name=name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age=age

studenti = Student("Alice", 17)
print("Name", studenti.name)

studenti.name="Bob"
studenti.age=18
print("Name:",studenti.name)