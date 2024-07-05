# Class-Blueprint of an object
#Object is an instance of class


class Person:
    #Properties/Attributes/Variable/Characteristics

    name ="Morris"
    age = 20
    gender = "Male"

    #Behaviour/Method/Function
    def walk(self):
        print("Person is walking")


person1 = Person()
print(person1.gender)
print(person1.name)

person1.walk()



