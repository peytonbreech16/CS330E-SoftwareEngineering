def my_islice_generator(iterable, start = 0, stop = None, step = 1):
    lengthOfIter = len(iterable)

    if (lengthOfIter < stop) or (lengthOfIter < start):
        return
    itera = iter(range(start,stop,step))
    total = start
    enum = next(itera)

    while total <= stop:
        yield iterable[total]
        for i in range(step):
            try:
                enum = next(itera)
            except StopIteration:
                return
        total += step