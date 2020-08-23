c = int('101', base=2)
print(c)


def square(a):
    return a ** 2


f = square
print(f is square)


def cube(a):
    return a ** 3


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


f = select_function(1)
print(f is square)

print(select_function(2)(3))
