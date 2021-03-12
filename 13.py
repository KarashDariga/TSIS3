class Person:

    # def __init__(self, name, surname): 
    #     self.name = name
    #     self.surname = surname

    def show(self):
        #print("{} - {}".format(self.name, self.surname ))
        print(f'{self.name} - {self.surname}')

    def __str__(self):
        return f'{self.name} - {self.surname}'
# a = Person("Askar", "Akshabayev")
# b = Person("Aaa", "Bbb")
 
a = Person()
a.name = "Askar"
a.surname = "Akshabayev"

b = Person()
b.name = "nnn"
b.surname = "bbb"
print(a)
print(b)
