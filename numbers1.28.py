import sys
print(sys.getsizeof(0))
print(sys.getsizeof(1))


def from_base10(n, b):
    if b < 2:
        raise ValueError('Base must be bigger than 2')
    if n < 0:
        raise ValueError('Value must be bigger than 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        m, n = n % b, n // b
        digits.insert(0, m)
    return digits


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit map is not enough")
    encoding = ''
    for d in digits:
        encoding += digit_map[d]
    return encoding


print(from_base10(10, 2))
print(from_base10(10, 10))
print(encode([15,15], '0123456789abcdef'))


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEF'
    if base < 2 or base > 16:
        raise ValueError("base must be between 2 and 16")
    sign = -1 if number < 0 else 1
    number = sign * number

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


print(rebase_from10(11, 11))
