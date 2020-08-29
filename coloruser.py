from pythondeepdive.tuples1118 import random_color

color = random_color()
color.red

data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

keys = set()

for d in data_list:
    for key in d.keys():
        keys.add(key)
print(keys)

keys = {key for dict_ in data_list for key in dict_.keys()}
print(keys)