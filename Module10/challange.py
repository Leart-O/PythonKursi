class DigitalSchool:
    def __init__(self, name, city, state, courses):
        self.__name=name
        self.__city=city
        self.__state=state
        self.__courses=courses

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.name = name
        self.__name = self.name

    @property
    def city(self):
        return self.__city

    @city.setter
    def name(self, city):
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    def show_school_info(self):
        return {
            "name":self.__name,
            "city":self.__city,
            "state":self.__state,
            "courses":self.__courses
        }
    def organize_hackathon(self):
        print("Organizing a generic hackathon...")

#define a subclass called DS Prishtina where it has a private attribute called student_number and 2 methods organize hackathon and SCF
class DS_Prishtina(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name,city,state,courses)
        self.__student_number=student_number
    def SCF(self):
        print("First Edition")
    def organize_hackathon(self):
        print("We are doing a beta analysis hackathon")


class DS_Ferizaj(DigitalSchool):
    def __init__(self, name, city, state, courses, student_number):
        super().__init__(name,city,state,courses)
        self.__student_number=student_number
    def Internship(self):
        print("Looking for interns!")
    def organize_hackathon(self):
        print("We are doing a hackathon!")

prishtina_obj=DS_Prishtina("DS_Prishtina", "Prishtina", "Kosova", ["PHP","Python","Java"], 3000)
print(prishtina_obj.show_school_info())

ferizaj_obj=DS_Ferizaj("DS_Ferizaj", "Ferizaj", "Kosova", ["HTML", "CSS", "JavaScript"], 2400)
ferizaj_obj.Internship()