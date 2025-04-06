# ------------------------- Vehicle Class -------------------------
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")

    def get_make_model(self):
        print(f"I am a {self.make} {self.model}")

# ------------------------- Class and Objects -------------------------
print(f"{'-'*10}\nClass and Objects\n")

car1 = Vehicle('Tesla', 'Model 3')
car2 = Vehicle('Hyundai', 'Swift')

for car in (car1, car2):
    print(f"\nObject: {car.make}")
    car.moves()
    car.get_make_model()

# ------------------------- Inheritance -------------------------
print(f"\n{'-'*10}\nInheritance\n")

class Airplane(Vehicle):
    def moves(self):
        print('Flies along...')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')

class Bike(Vehicle):
    def moves(self):
        print('Vrooms along...')

class Golfkart(Vehicle):
    pass

vehicles = [
    Airplane('Boeing', '747'),
    Truck('Ashok', 'Leyland'),
    Bike('Redbull', 'BMX'),
    Golfkart('Caddy', 'Model Vice')
]

for v in vehicles:
    v.get_make_model()
    v.moves()

# ------------------------- Super Keyword -------------------------
print(f"\n{'-'*10}\nSuper\n")

class Car(Vehicle):
    def __init__(self, make, model, date_of_manufacture):
        super().__init__(make, model)
        self.date_of_manufacture = date_of_manufacture

    def moves(self):
        return super().moves()

    def intro(self):
        print(f"I am {self.make} {self.model}, made in {self.date_of_manufacture}.")

ford = Car('Ford', 'Model 2', '1987')
ford.intro()

# ------------------------- Polymorphism -------------------------
print(f"\n{'-'*10}\nPolymorphism\n")

for v in [car1, car2] + vehicles:
    v.get_make_model()
    v.moves()

# ------------------------- Method Overriding -------------------------
print(f"\n{'-'*10}\nMethod Override\n")

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
    print(animal.speak())

# ------------------------- Method Overloading -------------------------
print(f"\n{'-'*10}\nMethod Overloading\n")

class Math:
    def add(self, a, b, c=0):
        return a + b + c

calc = Math()
print(calc.add(2, 3))      # 5
print(calc.add(2, 3, 4))   # 9

# ------------------------- Abstraction -------------------------
print(f"\n{'-'*10}\nAbstraction\n")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

circle = Circle(5)
square = Square(5)

print(circle.area())  # 78.5
print(square.area())  # 25
