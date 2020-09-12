def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print("inner function called a={0}, b={1}".format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec


@my_dec(10, 20)
def my_func(s):
    print('Hello, {0}'.format(s))


my_func('charles')


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print("inner function called a={0}, b={1}".format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner


@MyClass(30, 40)
def my_func(s):
    print('Hello, {0}')


my_func('charles guo')