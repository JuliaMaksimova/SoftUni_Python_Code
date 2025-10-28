class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal (self, species, animals):
        if species == "mammals":
            self.mammals.append(animals)
            Zoo.__animals +=1
        elif species == "fishes":
            self.fishes.append(animals)
            Zoo.__animals += 1
        elif species == "birds":
            self.birds.append(animals)
            Zoo.__animals += 1

    def get_info(self, species):

        if species == "mammals":
            return f"{species} in {self.name}: {' ,'.join(self.mammals)}\nTotal animals: {len(Zoo.__animals)}"
        elif species == "fishes":
            return f"{species} in {self.fishes}: {' ,'.join(self.fishes)}\nTotal animals: {len(Zoo.__animals)}"
        elif species == "birds":
            return f"{species} in {self.birds}: {' ,'.join(self.birds)}\nTotal animals: {len(Zoo.__animals)}"

name = input()
zoo = Zoo(name)
number = int(input())

for animal in range (number):
    species, animals = input().split()
    zoo.add_animal(species,animals)

final_species = input()

print(zoo.get_info(final_species))
