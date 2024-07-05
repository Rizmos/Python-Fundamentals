#Parent class/Super class
class Animal:
    def speak(self):
        print('Animal is speaking')

    def move(self):
        print('Animal is moving')

#Child class/Sub class
class Duck(Animal):
    def Quack(self):
        print("Duck is quacking")

class Bee (Animal):
    def Buzz(self):
        print("Bee is buzzing")

class Dog(Animal):
    def Bark(self):
        print("Dog is barking")

a = Animal()
a.speak()
a.move()
d = Duck ()
d.Quack()
d.move()

b = Bee ()
b.Buzz()
b.speak()