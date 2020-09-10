from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps

d = {}

result = d.get('a')
print(result)
result = d.get('a', 100)
print(result)

counts = {}
sentence = "able was I ere I saw elba"
for c in sentence:
    counts[c] = counts.get(c, 0) + 1
print(counts)

counts = defaultdict(lambda: 0)

for c in sentence:
    counts[c] += 1

print(counts)


def function_stats():
    di = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            di[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)
        return wrapper
    return Stats(decorator, di)


stats = function_stats()
print(stats.data)
print(stats.decorator)


@stats.decorator
def func_1():
    pass


@stats.decorator
def func_2():
    pass


func_1()
func_2()
func_1()
print(stats.data)

