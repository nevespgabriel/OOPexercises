from random import choice

class Student:
    educational_platform = "Udemy"
    def __init__(self, nome, idade=18):
        self.name = nome
        self.age = idade


    def greet(self):
        greetings = [f"Hi, I'm {self.name}.",
                     f"Hey there, my name is {self.name}!",
                     f"Hi. Oh, my name is {self.name}.",
                     f"Hello everyone, I am {self.name}.",
                     f"{self.name} is my name, hi."]
        return choice(greetings)


names = ["João","Matheus","Pedro","Maria","Ana"]
students = []
c = 0
for c in range(0,5):
    students.append(Student(names[c]))
    print(students[c].greet())

