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
print('internaling=', end - start)