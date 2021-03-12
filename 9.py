class MyClass:
    #fields
    x = 5
    y = 6

    # methods
    def sum(self):
        return self.x + self.y # a.x + a .y

a = MyClass() # a.x, a.y
a.x = 10
a.y = 20
b = MyClass()  #b.x, b.y
b.x = 7
b.y = 30
print(a.x, a.y)
print(b.x, b.y)
print(a.sum()) # 
print(b.sum()) #  b.x + b.y