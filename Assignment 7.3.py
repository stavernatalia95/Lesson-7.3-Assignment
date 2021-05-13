class Zoo:
    animals = {}
    zooEmployees = []

    def __init__(self):
        self.animals["squirrels"] = 3
        self.zooEmployees.append("John")

    def add_animal(self, animal="squirrels", num=0):

        numEmployees = len(self.zooEmployees)
        numAnimals = 0
        for n in self.animals.values():
            numAnimals += n

        if ((numAnimals / 10) > numEmployees):
            print("Not enough employees! Can't take care of a new animal!")
            return

        if (num == 0):
            quantity = self.animals[animal]
            quantity = quantity + 1
            self.animals[animal] = quantity
        else:
            self.animals[animal] = num
            numAnimals += num
            if ((numAnimals / 10) > numEmployees):
                print("Not enough employees for all animals! Hire someone new!")

    def remove_animal(self, name):
        self.animals.pop(name)

    def hire_employee(self, name):
        self.zooEmployees.append(name)

    def fire_employee(self, name=""):
        if name == "":
            self.zooEmployees.pop()
        else:
            self.zooEmployees.remove(name)

    def __str__(self):
        speciesAndemployees = "animals: \n"
        for a, n in self.animals.items():
            speciesAndemployees += str(a) + ": " + str(n) + "\n"

        speciesAndemployees += "\nemployees: \n"
        for e in self.zooEmployees:
            speciesAndemployees += e + "\n"

        return speciesAndemployees


z1 = Zoo()
z1.add_animal("cat", 5)
print(z1)
z1.add_animal("dogs", 10)
print(z1)
z1.hire_employee("Mitch")
print(z1)
z1.fire_employee()
print(z1)