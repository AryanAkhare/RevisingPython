class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")

    def get_make_model(self):
        print(f"I am a {self.make} {self.model}")

# Class and Objects
print(f"{'-'*10}\nClass and Objects\n")

print("Object1")
car1 = Vehicle('Tesla', 'Model 3')
car1.moves()
car1.get_make_model()
print(car1.make)
print(car1.model)

print(f"{'-'*10}")

print("Object2")
car2 = Vehicle('Hyundai', 'Swift')
car2.moves()
car2.get_make_model()
print(car2.make)
print(car2.model)

# Inheritance
print(f"{'-'*10}\nInheritance\n")

class Airplane(Vehicle):
    def moves(self):  # Overwritten method
        print('Flies along...')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

class Bike(Vehicle):
    def moves(self):
        print('Vrooms along...')

class Golfkart(Vehicle):
    pass  # Uses parent's move() method

boeing = Airplane('Boeing', '747')
leyland = Truck('Ashok', 'Leyland')
redbull = Bike('Redbull', 'BMX')
caddy = Golfkart('Caddy', 'Model Vice')

boeing.get_make_model()
boeing.moves()

leyland.get_make_model()
leyland.moves()

redbull.get_make_model()
redbull.moves()  # Uses its own function

caddy.get_make_model()
caddy.moves()  # Uses parent function

# Super keyword
print(f"{'-'*10}\nSuper\n")

class Car(Vehicle):
    def __init__(self, make, model, date_of_manufacture):
        super().__init__(make, model)  # Calls parent constructor
        self.date_of_manufacture = date_of_manufacture

    def moves(self):
        return super().moves()

    def intro(self):
        print(f"I am {self.make} {self.model}, made in {self.date_of_manufacture}.")

ford = Car('Ford', 'Model 2', '1987')
ford.intro()

# Polymorphism
print(f"{'-'*10}\nPolymorphism\n")

for v in (car1, car2, boeing, leyland, redbull, caddy):
    v.get_make_model()
    v.moves()

# Method Overriding
print(f"{'-'*10}\nMethod Override\n")

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Bark, Meow

# Method Overloading (Using Default Arguments)
print(f"{'-'*10}\nMethod Overloading\n")

class Math:
    def add(self, a, b, c=0):
        return a + b + c  # Works for both two and three arguments

obj = Math()
print(obj.add(2, 3))      # Output: 5
print(obj.add(2, 3, 4))   # Output: 9

# Abstraction
print(f"{'-'*10}\nAbstraction\n")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return pow(self.side, 2)  # Corrected exponentiation

c = Circle(5)
print(c.area())  # Output: 78.5

sq = Square(5)
print(sq.area())  # Output: 25
