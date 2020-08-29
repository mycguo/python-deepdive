import sys
from types import ModuleType


def func():
    pass


globals()
globals()['func']()

mod = ModuleType('test', "this is a test module")
print(mod.__dict__)

mod.pi = 3.14
mod.hello = lambda x: print('hello' + x)

print(sys.prefix)
print(sys.exec_prefix)
print(sys.path)
