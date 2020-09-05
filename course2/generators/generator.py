import math


def my_func():
    yield 1
    yield 2
    yield 3


gen = my_func()
next(gen)
next(gen)
print(next(gen))


def factorials(n):
    for i in range(n):
        yield math.factorial(i)


fact_generator = factorials(10)
print(next(fact_generator))
print(next(fact_generator))
for g in fact_generator:
    print(g)

