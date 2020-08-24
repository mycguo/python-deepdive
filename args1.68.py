import time
def func(a, b, *c):
    print(a)
    print(b)
    print(c)


func(10, 20)
l = (1, 2, 3)
func(*l)
l2 = [1, 2, 3, 4]
func(*l2)


def avg(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total/count


print(avg(2, 2, 4, 4))
print(avg(1))


def func2(*, d, **kwargs):
    print(d)
    print(kwargs)
    print('end of line\n')


func2(d=1, a=2, b=3)


def time_it(fn, *args, rep=1, **kwargs):
    # print(args)
    # print(kwargs)
    for i in range(rep):
        fn(*args, **kwargs)


time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=3)


def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}'.format(n))
        result = n * factorial(n-1)
        cache[n] = result
        return result


factorial(3)
factorial(4)
