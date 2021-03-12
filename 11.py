class Person: # class object

    def __init__(self, name, surname): # Конструктор
        self.name = name
        self.surname = surname

    def show(self):
        #print("{} - {}".format(self.name, self.surname ))
        print(f'{self.name} - {self.surname}')

a = Person("Askar", "Akshabayev")
b = Person("Aaa", "Bbb")

a.show()
b.show()