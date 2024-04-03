

class animal:
    def __init__(self, species, type):
        self.species = species
        self.type = type


class bear(animal):
    def __init__(self, size, gender, species):
        super().__init__(species=species, type="Mammal")
        self.size = size
        self.gender = gender


Bear1 = bear(50, 'male','brown bear')

print(Bear1.size)
print(Bear1.gender)
print(Bear1.species)
print(Bear1.type)
