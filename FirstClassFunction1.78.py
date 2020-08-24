import random
def myfunc(a: 'info on int') -> 'should be int':
    """documentation of my_func"""
    return a


myfunc('1')
help(myfunc)

print(myfunc.__annotations__)


my_func2 = lambda x: x**2
print(my_func2(2))

my_func3 = lambda : 'hello'
my_func4 = lambda x, y: x + y

print(my_func4(1,2))

l = [ 1, 5, 4 ,10, 9, 6]
print(sorted(l))

l = ['c', 'B', 'D', 'a']
print(sorted(l))

print(sorted(l, key=lambda s: s.upper()))
print(sorted(l, key=lambda s: s.upper(), reverse=True))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.sort(key=lambda x: random.random())
print(l)

