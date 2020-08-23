# Jython

# Interning: reusing objects on demand, Singletons objects

a = 10
b = 10

import sys

def compare_using_equals(n):
    a = 'a long string not interned ' * 2000
    b = 'a long string not interned ' * 2000
    for i in range(n):
        if a == b:
            pass


def compare_internal(n):
    a = sys.intern('a long string not interned ' * 2000)
    b = sys.intern('a long string not interned ' * 2000)
    for i in range(n):
        if a == b:
            pass

import time
start = time.perf_counter()
compare_using_equals(10000)
end = time.perf_counter()
print('equality', end - start)

start = time.perf_counter()
compare_internal(10000)
end = time.perf_counter()
print('interning=', end - start)


def my_func():
    a = 24 * 60
    aa = 1440
    b = (1, 2) * 5
    c = 'abc' * 110
    d = [1, 2, 3]


print(my_func.__code__.co_consts)
