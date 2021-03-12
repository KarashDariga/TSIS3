class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname 

    def show(self):
        print(f'{self.name} - {self.surname}')

class Student(Person):
    def __init__(self, name, surname, gpa, faculty):
        super().__init__(name, surname)
        self.gpa = gpa
        self.faculty = faculty

    def show(self):
        print(f'{self.name} - {self.surname}')
        print(f'{self.gpa} - {self.faculty}')     

a = Student("Aaa", "Bbb", 3.9, "FIT")
a.show()     
b = Student("Bbb", "Ccc", 4.0, "FIT")
b.show()   


