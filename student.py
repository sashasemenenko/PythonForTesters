class Student:
    def __init__(self, name, age=None, grade=None):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("Oleksandr")
student2 = Student("Dmytrii", 25)
student3 = Student("Nadiia", grade="A")
student4 = Student("Bob", 35, "B")