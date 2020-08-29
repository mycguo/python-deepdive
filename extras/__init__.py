def audit(f):
    def inner(*args, **kwargs):
        print(f'called {f.__name__}')
        return f(*args, **kwargs)
    return inner


@audit
def say_hello(name):
    return f'Hello, {name}'


from operator import mul
from functools import reduce


@audit
def product(*values):
    return reduce(mul, values)


print(say_hello("charles"))

