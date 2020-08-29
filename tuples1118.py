from collections import namedtuple
from random import randint, random

var = (1, 2, 3,4, 5, 6, 7, 'something else')
var1, var2, *_, last = var
print(*_)

CityClass = namedtuple('city', ("city", "country"))
city1 = CityClass('xian', 'China')
city2 = CityClass('beijing', 'China')
city3 = CityClass(city='SFO', country='USA')

Person = namedtuple('Person', 'name age _SSN', rename=True)
person1 = Person('charles', 30, '123456890')
print(Person._fields)
# print(Person._source)
print('print dict')
print(person1._asdict())

*current, _ = person1
person1 = Person(*current, '234567890')
print(person1)
print(person1._replace(age='31'))

new_fields = Person._fields + ('last_name',)
ExtPerson = namedtuple('ExtPerson', new_fields, rename=True)
# print(ExtPerson._fields)
ext_person1 = ExtPerson(*person1 + ('guo',))
print(ext_person1)
print(Person.__doc__, Person.name.__doc__)

Color = namedtuple('Color','red, green, blue, alpha')


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)


color = random_color()








