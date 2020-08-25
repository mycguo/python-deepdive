from functools import reduce
import operator

l1 = [2, 3, 4]
l2 = [10, 20, 30]


def sq(x):
    return x**2


def add(x, y):
    return x + y


print(list(map(sq, l1)))
print(list(map(add, l1, l2)))

print([x**2 for x in l1])
print([x + y for x, y in zip(l1, l2)])

l = [1, 2, 3, 4]
print([x for x in l if x % 2 == 0])

l = range(10)
list(filter(lambda y: y < 25, map(lambda x: x**2, l)))

print([x**2 for x in range(10) if x**2 < 25])

print(reduce(lambda a, b: a if a < b else b, l))

print(reduce(add, l))
print(reduce(operator.mul, l))
operator.mul(1, 2)

