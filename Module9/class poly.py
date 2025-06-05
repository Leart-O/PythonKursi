class dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} nake the sound: ham")


class cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} nake the sound: miau")


class bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} nake the sound: ciu")

qeni = dog("Reksi")
macja = cat("Tom")
zogu = bird("Tweet")

for kafsha in (qeni, macja, zogu):
    kafsha.sound()
