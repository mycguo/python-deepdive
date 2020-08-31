from time import perf_counter

v = range(100_000_000)
b = 100


def testslice(values, batch_size):
    # using loop
    start_time = perf_counter()
    out = []
    for elem in values:
        out.append(elem)
        if len(out) == batch_size:
            # yield out
            out = []
    if out:
        # yield out
        pass
    print('Took {} seconds using loop '.format(perf_counter() - start_time))

    # using slice
    start_time = perf_counter()
    while True:
        out = values[0:batch_size]
        if len(out) == batch_size:
            # yield out
            values = values[batch_size:]
        else:
            break
    if out:
        # yield out
        pass

    print('Took {} seconds using slice '.format(perf_counter() - start_time))


testslice(v, b)

