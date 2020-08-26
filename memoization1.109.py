
class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
            return self.cache[n]
        else:
            return self.cache[n]


f = Fib()
print(f.fib(8))


def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib


g = fib()
print(g(7))


def mem_fn(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner


@mem_fn
def fib(n):
    return 1 if n < 3 else fib(n-2) + fib(n-1)


def timed(reps):
    def dec(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(10):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start
            avg_elapsed = total_elapsed / 10

            args_ = [str(a) for a in args]
            kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
            all_args = args_ + kwargs_
            args_str = ','.join(all_args)

            print('{0}({1}) took {2}s to run'.format(fn.__name__, args_str, avg_elapsed))
            return avg_elapsed

        return inner
    return dec


@mem_fn
@timed(5)
def fib(n):
    return 1 if n < 3 else fib(n-2) + fib(n-1)


print(fib(7))
