import json
from pprint import pprint

d1 = {'a': 100, 'b': 200}
d1_json = json.dumps(d1)
print(d1_json)
print(type(d1_json))
print(json.dumps(d1, indent=2))

d2 = json.loads(d1_json)

d1 = {1: 100, 2: 200}
d1_json = json.dumps(d1)
print(d1_json)
d2_json = json.loads(d1_json)
print(d2_json)

print(d1 == d2)

d_json = '''
{
    "name": "john",
    "age": 82,
    "height": 1.68,
    "walksFunny": true,
    "sketches": [
        {
            "title": "Dead Parrot",
            "costars": ["Michael Pan"]
        },
        {
            "title": "Dead Parrot 2",
            "costars": ["Michael Pan", "Terry Jones"]
        }
    ],     
    "boring": null
}
'''
d = json.loads(d_json)


pprint(d)
print(type(d["walksFunny"]))


class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age}'

    def toJson(self):
        return vars(self)


p = Person("john", 82)
print(json.dumps({'john': p.toJson()}, indent=2))
