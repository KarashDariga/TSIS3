class Person:

    def __init__(self, name, surname): # init function - constructor
        self.name = name
        self.surname = surname

    def show(self): # show it's object methods
        #print("{} - {}".format(self.name, self.surname ))
        print(f'{self.name} - {self.surname}')

    def __str__(self):
        return f'{self.name} - {self.surname}'
a = Person("Askar", "Akshabayev")
b = Person("Aaa", "Bbb")

print(a)
print(b)
