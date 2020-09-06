from datetime import datetime
import json
from pythondeepdive.course3.json.jsonserilization import Person
from decimal import Decimal
from functools import singledispatch

current = datetime.utcnow()
print(current)


def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


print(format_iso(current))
print(current.isoformat())

log_record = {'time': datetime.utcnow().isoformat(),
              'message': 'testing'}

print(json.dumps(log_record, indent=2))

log_record = {'time': datetime.utcnow(),
              'message': 'testing'}

print(json.dumps(log_record, default=format_iso))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    else:
        try:
            return arg.toJson()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)


point1 = Point(1, 2)
person1 = Person('John', 18)
point2 = Point(Decimal('10.5'), Decimal(100.5))

log_record = dict(
    time=datetime.utcnow(),
    point_1=point1,
    created=person1,
    point_2=point2
)

print(json.dumps(log_record, default=custom_json_formatter, indent=2))


@singledispatch
def json_format(arg):
    print(arg)
    try:
        print("trying to toJSON")
        return arg.toJson()
    except AttributeError:
        try:
            return vars(arg)
        except TypeError:
            return str(arg)


@json_format.register(datetime)
def _(arg):
    return arg.isoformat()


@json_format.register(set)
def _(arg):
    return list(arg)


print(json.dumps(log_record, indent=2, default=json_format))



