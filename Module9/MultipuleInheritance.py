class Vertebrate():
    def __init__(self, backBone=True):
        self.has_Backbone=backBone
    def vertabrate_info(self):
        print("Vertebrates have a backbone")

class Aquatic:
    def __init__(self, habitat="water"):
        self.habitat=habitat
    def aquatic_info(self):
        print("Aquatic animals live in water")

class Fish(Vertebrate,Aquatic):
    def __init__(self, species, backBone=True,habitat="water"):
        super().__init__(backBone=backBone)
        self.species=species
        self.habitat=habitat
    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}")
    def swim(self):
        print("The fish is swimming")

goldfish = Fish("goldfish")
print(goldfish.has_Backbone)
print(goldfish.habitat)
goldfish.vertabrate_info()
