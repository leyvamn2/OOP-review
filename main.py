import math

# object
mylist = [1, 2, 3]
myset = set()
print(type(myset))
print(type(mylist))


# blueprints to define objects
class Animal:
    def __init__(self):
        print("I'm an animal")

    def sleepy(self):
        print("zzz...")


class Dog:
    ## add atributes, representa al objeto y pasa el atributo
    def __init__(self, mybreed, name, spots):
        Animal.__init__(self)
        # herencia, se pasa la clase inicial de animal a la clase hija
        # Atributo
        # Pasamos el argumento,
        # Se asigna usando el self.<nombreatributo
        self.breed = mybreed
        self.name = name
        # Boolean
        self.spots = spots

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return 'Account Owner'

    def deposit(self, add):
        self.balance += add

    def withdraw(self, quitr):
        self.balance -= quitr


acct = Account('Osito', 1000)

coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.slope())
print(li.distance())
my_dog = Dog(mybreed='Shitzu', name='sfsdf', spots=False)
print(my_dog.spots)
print(my_dog.name)
print(my_dog.breed)
