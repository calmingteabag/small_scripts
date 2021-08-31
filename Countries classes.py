class Country:

    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.states = []

    def add_state(self, state):
        if state in self.states:
            print(state + " already exists")
        else:
            self.states.append(state)

    def remove_state(self, state):
        if state not in self.states:
            print(state + " not found")
        else:
            self.states.remove(state)

# this is a new comment

class Estate(Country):

    def __init__(self, name, population, area):
        super().__init__(name, population)
        self.area = area
        self.cities = []

    def add_city(self, city):
        if city in self.cities:
            print(city + " already exists")
        else:
            self.cities.append(city)

    def remove_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
        else:
            print(city + " not found")


bra = Country("Brasil", 210)
bra.add_state("Bahia")
bra.add_state("Alagoas")
bra.add_state("Pernambuco")
bra.add_state("Bahia")
bra.add_state("Amazonas")
bra.add_state("Amazonas")

print(bra.states)

sp = Estate("Sao Paulo", 40, 24444)
sp.add_city("Garca")
sp.add_city("Bauru")
sp.add_city("Ourinhos")

ms = Estate("Mato Gross", 233, 244242)
ms.add_city("Campo Grande")
ms.remove_city("Manaus")
ms.remove_city("Campo Grande")
print(f"The cities of {sp.name} are {sp.cities}")
print(f"The cities of {ms.name} are {ms.cities}")

print(sp.area)

