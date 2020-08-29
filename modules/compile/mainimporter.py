import sys
import importlib

mod_name = 'math'
importlib.import_module(mod_name)

print(id(mod_name))

print('math' in sys.modules)

math2 = sys.modules['math']
print(id(mod_name))

print(sys.meta_path)
print(math2.__spec__)