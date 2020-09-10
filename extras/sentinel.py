_sentinel = object()


def validate(a=object()):
    default_a = validate.__defaults__[0]
    if a is not default_a:
        print('argument was not provided')
    else:
        print("argument was NOT provided")


def validate(a=object(), b=object(), *, kw=object()):
    default_a = validate.__defaults__[0]
    default_b = validate.__defaults__[1]
    default_c = validate.__kwdefaults__['kw']

    if a is not default_a:
        print('argument a is provided')
    else:
        print('argument a is not provided')

    if b is not default_b:
        print('argument b is provided')
    else:
        print('argument b is not provided')

    if kw is not default_c:
        print('argument kw is provided')
    else:
        print('argument kw is not provided')


def switcher(fn):
    registry = dict()
    registry['default'] = fn

    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn
        return inner

    def decorator(case):
        fn = registry.get(type(case), registry['default'])
        return fn(case)

    decorator.register = register
    return decorator


@switcher
def dow():
    return 'invalid day of week'


@dow.register(1)
def dow_1():
    return 'Monday'


dow.register(2)(lambda: 'Tuesday')
dow.register(3)(lambda: 'Wednesday')
dow.register(4)(lambda: 'Thursday')
dow.register(5)(lambda: 'Friday')
dow.register(6)(lambda: 'Saturday')
dow.register(7)(lambda: 'Sunday')

