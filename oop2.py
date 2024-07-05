class Animal:
    def __init__(Self,type,hasScales,hasWings,Color) :
        self.type = type
        self.hasScales = hasScales
        self.hasWings = hasWings
        self.color = Color

    def movement(self):
        print(self.type,"is moving")

animal1 = Animal("Fish",True,False,"red")
animal1.movement()

animal2 = Animal("Bird",True,True,"red")
animal2.movement()

animal3 = Animal("Lion",False,False,"red")
animal3.movement()