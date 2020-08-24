l = [1, 2, 3, 4, 5, 6]

a = l[0]
b = l[1:]

a, *b = l
print(a)
print(b)

a, *b = 'XYZ'
print(a)
print(b)

l1 = [1, 2, 3]
l2 = [4, 5, 6]

ll = [*l1, *l2]
print(ll)

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}

d = {**d1, **d2, **d3}
print(d)

lnest = [1, 2, [3, 4]]
a, b, (c, d) = lnest

a, *b, (c, *d) = [1, 2, 3, 'python']
print(d)

d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key4': 4}

d4 = {*d1, *d2}
print(d4)
d5 = {**d1, **d2}
print(d5)
