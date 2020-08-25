from time import perf_counter

class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


a = Averager()
print(a.add(10))
print(a.add(20))


def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        total = total + number
        nonlocal count
        count = count + 1
        return total / count
    return add


a = averager()
print(a.__closure__)
print(a(10))
print(a(20))


class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start


print('timer using function')
t1 = Timer()
print(t1())


def timer():
    start = perf_counter()

    def pool():
        return perf_counter() - start
    return pool


print('timer using closure')
t2 = timer()
print(t2())

print('closure for counter')


def counter(init_value=0):
    def inc(increment=1):
        nonlocal init_value
        init_value += increment
        return init_value
    return inc


counter1 = counter()
print(counter1())


def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner


def add(a, b):
    return a + b


counter_add = counter(add)
counter_add(1, 2)
counter_add(2, 3)


