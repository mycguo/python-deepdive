print(dir(sorted))


def my_func(a, b=2, c=3, *, kw1, kw2=2):
    pass


print(dir(my_func))
print('new line')
print(dir(my_func.__code__))

print(callable(print))