# variable
import sys
import ctypes

my_var_1 = [1, 2, 3]
print(hex(id(my_var_1)))

# reference counting
my_var_2 = my_var_1
print(hex(id(my_var_2)))

print(sys.getrefcount(my_var_1))
print(sys.getrefcount(my_var_2))

a = [1, 2, 3]


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(a)))
b = a
print(ref_count(id(a)))
b = None
print(ref_count(id(a)))