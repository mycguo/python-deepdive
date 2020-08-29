import os.path
import types
import sys

module_name = 'newmodule'
module_file = 'module1.source'
module_path = '.'

real_path = os.path.join(module_path, module_file)
real_path = os.path.abspath(real_path)

# read source
with open(real_path) as code_file:
    source_code = code_file.read()

mod = types.ModuleType(module_name)
mod.__file__ = real_path

# set a ref in sys module
sys.modules[module_name] = mod

# compile
code = compile(source_code, filename=real_path, mode='exec')

# exec
exec(code, mod.__dict__)
