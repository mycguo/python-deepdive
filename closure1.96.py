a = 10


def my_func():
    print('global a: ', a)
    # a = 'hello'
    print(a)


my_func()


def out_func():
    x = 'python'
    print(id(x))
    a = 10

    def inner_func():
        print(x)
        print(id(x))
        nonlocal a
        a = a + 1
        print(a)

    return inner_func


f = out_func()
f2 = out_func()
print('free variable ',  f.__code__.co_freevars)
print('closure ',  f.__closure__)
f()
f()

f2()
f2()
