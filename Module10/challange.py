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
        self.__name = name

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
        return contact_info={
            "Digital School":"049123456"
        }