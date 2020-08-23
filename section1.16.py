# garbage collection
import ctypes
import gc


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "object exists"
    return "Not found"


class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(id(self), id(self.b)))


class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, A: {1}'.format(id(self), id(self.a)))


gc.disable()
my_var = A()
a_id = id(my_var)
b_id = id(my_var.b)

print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))

gc.collect()
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))
