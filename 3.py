def fun(n):
    return lambda a: a * n

doubler = fun(2) # lambda a: a * 2

print(doubler(3))
print(doubler(6)) # in this doubler it;s lambda 

triple = fun(3) # lambda a: a * 3

print(triple(3))
print(triple(6))

multiple_100 = func(100) # lambda a: a *  100 

print(multiple_100(5))
print(multiple_100(6))