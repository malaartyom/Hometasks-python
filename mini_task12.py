def cycle(itr):
    while True:
        yield from itr

def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break

    return res

print(take(cycle([1,2,3]), 10))