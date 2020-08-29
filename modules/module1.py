print('running {0}'.format(__name__))


def pprint_dict(header, c):
    print('****header= {0}'.format(header))
    for key, value in c.items():
        print(key, value)
    print('*******\n')


pprint_dict('module.globals', globals())
