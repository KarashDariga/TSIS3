class Fib:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 0
        self.y = 1
        return self

    def __next__(self): 
        x, y = self.x, self.y
        self.x, self.y = self.y, self.x + self.y 
        return x + y

a = Fib(100)
it = iter(a)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))