import sys

print('running main - module name {0}'.format(__name__))
import pythondeepdive.modules.module1 as m1

print(m1)
print(x + '\n' for x in sys.path)

import pythondeepdive.modules.module1 as m1
m1.pprint_dict('main.globals', globals())

# del m1
# m1.pprint_dict('main.globals', globals())

sys.modules['test'] = lambda: 'test'
import test
print(test)
print(test())


