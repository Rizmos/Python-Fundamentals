
#Inbuilt Functions/Standard Library Functions
number = max(56,78,100)
print(number)

y= min(67,23,3,90)
print("The minimum value is ",y)


#User-defined functions

def name():
    print("Glory")
name()#CALLING A FUNCTION

def Student():
    firstname= "Mark"
    course = "MIT"
    age = 27
    print(firstname,course,age)

Student()

#Parameters and arguments

def add(num1,num2):
    print(num1 + num2)

add(12,26)
add(25,96)
add(17,57)
add(32,28)
add(22,29)


def employee(fullname , age , salary ,position,marital_status):
    print(fullname,age,salary,position,marital_status)


employee("Mary Muthoni", 56 , 70000 , "Receptionist", "Single")
employee("James Kamau", 36 , 700000 , "CEO", "Single")
employee("Mary Muthoni", 56 , 170000 , "Receptionist", "Single")
employee("Mary Muthoni", 56 , 50000 , "Receptionist", "Single")
employee("Mary Muthoni", 56 , 30000 , "Receptionist", "Single")

def product (x,y):
    print(x * y)

product(12,6)
product(13,14)
product(9,84)
product(18,87)
product(22,23)





