class MyClass:
    #fields
    x = 5
    y = 6

    # methods
    def sum(self):
        return self.x + self.y

a = MyClass() # a.x, a.y
b = MyClass()  #b.x, b.y

print(a.x, a.y)
print(b.x, b.y)