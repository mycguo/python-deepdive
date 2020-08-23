# immutable
# numbers, string, tuple
# frozen set

# mutable
# list
# set
# dict

a = [1, 2]
b = [3, 4]
t = (a, b)

print(id(t))
a.append(5)
print(id(t))

