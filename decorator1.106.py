from functools import wraps

def counter(fn):
    cnt = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        """ documentation string """
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        inner.__name__ = fn.__name__
        inner.__doc__ = fn.__doc__
        return fn(*args, **kwargs)
    return inner


@counter
def add(a, b):
    """ documentation string for original function"""
    return a + b


print(add(1, 2))
print(add.__name__)


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{0}({1}) took {2}s to run'.format(fn.__name__, args_str, elapsed))
        return result
    return inner


# recursion
@timed
def fab(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fab(n-1) + fab(n-2)


# loop
@timed
def fabloop(n):
    result_1 = 1
    result_2 = 1
    for i in range(3, n+1):
        result_1, result_2 = result_2, result_1 + result_2
    return result_2


# reduce
@timed
def fabreduce(n):
    from functools import reduce
    init = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, init)
    return fib_n[0]


fab(29)
fabloop(29)
fabreduce(29)


def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0} called {1}'.format(run_dt, fn.__name__))
        return result

    return inner


@timed
@logged
def func_1():
    pass


@timed
@logged
def func_2():
    pass


func_1()
func_2()





