# coercing
import decimal
from decimal import Decimal
import math
import sys
import time


ctx = decimal.getcontext()
print(ctx.rounding)
print(ctx.prec)

x = Decimal('1.25')
y = Decimal('1.35')


with decimal.localcontext() as ctx:
    ctx.prec = 8
    ctx.rounding = decimal.ROUND_DOWN
    print(decimal.localcontext())
    print(type(ctx))
    print(ctx)
    print(round(x, 1))
    print(round(y, 1))

print(Decimal((0, (3, 1, 4), -2)))

x = 0.01
x_dec = Decimal('0.01')
print(format(math.sqrt(x), '0.27f'))
print(x_dec.sqrt())

a = 3.1415
b = Decimal('3.1415')

print(sys.getsizeof(a))
print(sys.getsizeof(b))

def run_float(n):
    for i in range(n):
        a = 3.1415


def run_deimal(n):
    for i in range(n):
        a = Decimal('3.1415')


n = 1000000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float:', end - start)

start = time.perf_counter()
run_deimal(n)
end = time.perf_counter()
print('decimal:', end - start)