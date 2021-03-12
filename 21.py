class MyNumber:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        x = self.x
        self.x += 1
        return x

n = MyNumber()

it = iter(n) # __iter__ x = 1

print(next(it)) # __next__
print(next(it))
print(next(it))

