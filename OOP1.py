class Student:
    def __init__(self,firstname,age,course,gender):
        self.firstname = firstname
        self.age = age
        self.course = course
        self.gender = gender


    def study(self):
        print(self.firstname,"is studying")


student1 = Student("John","18","Python","Male")
student1.study()

student2 = Student("Anne",23,"MIT","Female")
student2.study()

student3 = Student("Joe",27,"Cyber-Security","Male")
student3.study()


