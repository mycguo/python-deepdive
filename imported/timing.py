""" time the code takes to run """
from time import perf_counter
from collections import namedtuple
import argparse
print('loading timing')

Timing = namedtuple('Timing', 'repeats, elapsed, average')


def timeit(code, repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    elapsed = perf_counter() - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)


if __name__ == '__main__':
    print('running command line')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', type=str, help='python code')
    parser.add_argument('-r', '--repeats', type=int,
                        default=10, help='Number of times')
    args = parser.parse_args()
    print(args.code)
    print(args.repeats)
    timeit(code=args.code, repeats=args.repeats)
